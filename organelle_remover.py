#run organelle removal pipeline
#ensure qiime conda environment is active
#biopython must be installed in the conda environment
#it can be installed with
#conda install -c conda-forge biopython -y

import argparse
from os.path import isfile, join
import shutil
import subprocess
import tarfile
import tempfile
from urllib.request import urlopen

from Bio import SeqIO
from qiime2 import Artifact
from qiime2.plugins.feature_classifier.methods import classify_sklearn, extract_reads, fit_classifier_naive_bayes
from qiime2.plugins.feature_classifier.pipelines import classify_consensus_vsearch
from qiime2.plugins.feature_table.methods import merge_seqs, merge_taxa
from qiime2.plugins.taxa.methods import filter_table


def download_file(url, local_filepath):
    with urlopen(url) as response, open(local_filepath, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


parser = argparse.ArgumentParser(prog = 'Organelle Remover', description = '''Updates the SILVA reference taxonomy with additional organelle sequences, then annotates and filters a q2 feature table''')

parser.add_argument('--i-feature-table', required = True, help = '''path to QIIME2 FeatureTable[Frequency] artifact''')
parser.add_argument('--i-sequences', required = True, help = '''path to QIIME2 FeatureData[Sequence] artifact''')
parser.add_argument('--p-skip-setup', action = 'store_true', help = '''skip the downloading and merging of organelle databases and use the 'silva_extended_sequences.qza' and 'silva_extended_taxonomy.qza' files in cwd for classification''')
parser.add_argument('--p-classifier', choices = ['nb', 'vsearch'], default = 'vsearch', help = '''Use vsearch or naive bayes classifier to classify sequences. The Naive Bayes classifier will be trained first, then used (default vsearch)''')
parser.add_argument('--p-threads', default = 1, type = int, help = '''threads to use in multithreaded methods (trimming and classifying sequences)''')
parser.add_argument('--o-filtered-table', required = True, help = '''path to filtered feature table''')

args = parser.parse_args()

#check that passed paths exist:
for arg in [args.i_feature_table, args.i_sequences]:
    if not isfile(arg):
        raise OSError(f'{arg} is not a valid file path')

if not args.p_skip_setup:
    #download silva artifacts
    download_file('https://data.qiime2.org/2023.2/common/silva-138-99-seqs-515-806.qza', 'silva_138_v4_seqs.qza')

    download_file('https://data.qiime2.org/2023.2/common/silva-138-99-tax-515-806.qza', 'silva_138_v4_taxonomy.qza')

    #download and extract the metaxa2 database
    download_file('https://microbiology.se/sw/Metaxa2_2.2.1.tar.gz', 'Metaxa2_2.2.1.tar.gz')
    with tempfile.TemporaryDirectory() as temp_dir:
        with tarfile.open('Metaxa2_2.2.1.tar.gz', 'r:gz') as tar:
            tar.extractall(temp_dir)
        blast_path = join(temp_dir, 'Metaxa2_2.2.1', 'metaxa2_db', 'SSU', 'blast')
        subprocess.run(['blastdbcmd', '-entry', 'all', '-db', blast_path, '-out', 'metaxa2.fasta'])

    #download the phytoref database
    download_file('http://phytoref.sb-roscoff.fr/static/downloads/PhytoRef_with_taxonomy.fasta', 'PhytoRef_with_taxonomy.fasta')

    with open('silva_organelle_taxonomy.tsv', 'w') as silva_taxonomy:
        silva_taxonomy.write('Feature ID\tTaxon\n')
        with open('organelle_sequences.fasta', 'w') as organelle_sequences:
            for i, entry in enumerate(SeqIO.parse('metaxa2.fasta', 'fasta')):
                if 'mitochondria' in entry.description or 'Mitochondria' in entry.description:
                    organelle_sequences.write(f'>metaxa2_mitochondria_{i}\n')
                    organelle_sequences.write(f'{entry.seq}\n')
                    sequence_info = str(entry.description).split(';')[-1]
                    silva_taxonomy.write(f'metaxa2_mitochondria_{i}\td__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Rickettsiales; f__Mitochondria; g__Mitochondria; s__{sequence_info}\n')
            for i, entry in enumerate(SeqIO.parse('PhytoRef_with_taxonomy.fasta', 'fasta')):
                #one weird sequence in this database
                if not 'XXXXXXXXXX' in entry.seq:
                    organelle_sequences.write(f'>phytoref_chloroplast_{i}\n')
                    organelle_sequences.write(f'{entry.seq}\n')
                    sequence_info = str(entry.description).split(';')[-1]
                    silva_taxonomy.write(f'phytoref_chloroplast_{i}\td__Bacteria; p__Cyanobacteria; c__Cyanobacteriia; o__Chloroplast; f__Chloroplast; g__Chloroplast; s__{sequence_info}\n')

    #import, select the v4 region, merge, and save the new sequence artifact
    organelle_sequences = Artifact.import_data('FeatureData[Sequence]', 'organelle_sequences.fasta')
    forward_primer = 'GTGYCAGCMGCCGCGGTAA'
    reverse_primer = 'GGACTACNVGGGTWTCTAAT'
    trimmed_organelle_sequences, = extract_reads(organelle_sequences, forward_primer, reverse_primer, n_jobs = args.p_threads, read_orientation = 'forward')
    silva_sequences = Artifact.load('silva_138_v4_seqs.qza')
    silva_extended_sequences, = merge_seqs([trimmed_organelle_sequences, silva_sequences])
    silva_extended_sequences.save('silva_extended_sequences.qza')

    #merge the taxonomy reference
    silva_organelle_taxonomy = Artifact.import_data('FeatureData[Taxonomy]', 'silva_organelle_taxonomy.tsv')
    silva_taxonomy = Artifact.load('silva_138_v4_taxonomy.qza')
    silva_extended_taxonomy, = merge_taxa([silva_organelle_taxonomy, silva_taxonomy])
    silva_extended_taxonomy.save('silva_extended_taxonomy.qza')


query_sequences = Artifact.load(args.i_sequences)

if args.p_classifier == 'nb':
    #train the nb classifier if needed
    if not isfile('silva_extended_nb_classifier.qza'):
        reference_sequences = Artifact.load('silva_extended_sequences.qza')
        reference_taxonomy = Artifact.load('silva_extended_taxonomy.qza')
        nb_classifier, = fit_classifier_naive_bayes(reference_sequences, reference_taxonomy)
        nb_classifier.save('silva_extended_nb_classifier.qza')
    #annotate sequences with the nb classifier
    nb_classifier = Artifact.load('silva_extended_nb_classifier.qza')
    classification_taxonomy, = classify_sklearn(query_sequences, nb_classifier, n_jobs = args.p_threads)

else:
    #annotate sequences with vsearch
    reference_sequences = Artifact.load('silva_extended_sequences.qza')
    reference_taxonomy = Artifact.load('silva_extended_taxonomy.qza')
    classification_taxonomy, = classify_consensus_vsearch(query_sequences, reference_sequences, reference_taxonomy, threads = args.p_threads)

classification_taxonomy.save('silva_extended_classification_taxonomy.qza')

#use the classification taxonomy to filter organelles out of the feature table
feature_table = Artifact.load(args.i_feature_table)
filtered_table, = filter_table(feature_table, classification_taxonomy, exclude = 'mitochondria,Mitochondria,chloroplast,Chloroplast')

#make sure the output path has a qza extension
output_path = args.o_filtered_table
if not output_path.endswith('.qza'):
    output_path = f'{output_path}.qza'
filtered_table.save(output_path)
