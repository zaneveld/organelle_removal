#generate taxonomy files. BioPython must be installed
#(conda install -c conda-forge biopython)


import os
from os.path import exists, isfile, join
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request

from Bio import SeqIO
from qiime2 import Artifact
from qiime2.plugins.feature_classifier.methods import extract_reads, fit_classifier_naive_bayes
from qiime2.plugins.feature_table.methods import merge_seqs, merge_taxa

def download_file(url, local_filepath):
    with urllib.request.urlopen(url) as response, open(local_filepath, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)




working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
refs_dir = join(working_dir, 'taxonomy_references')

if not exists(refs_dir):
    os.mkdir(refs_dir)
if not isfile(join(refs_dir, 'silva_sequences.qza')):
    download_file('https://data.qiime2.org/2021.2/common/silva-138-99-seqs-515-806.qza', 
                  join(refs_dir, 'silva_sequences.qza'))
if not isfile(join(refs_dir, 'silva_taxonomy.qza')):
    download_file('https://data.qiime2.org/2021.2/common/silva-138-99-tax-515-806.qza', 
                  join(refs_dir, 'silva_taxonomy.qza'))
if not isfile(join(refs_dir, 'gg_13_8_otus.tar.gz')):
    download_file('ftp://greengenes.microbio.me/greengenes_release/gg_13_5/gg_13_8_otus.tar.gz',
                  join(refs_dir, 'gg_13_8_otus.tar.gz'))
if not isfile(join(refs_dir, 'Metaxa2_2.2.1.tar.gz')):
    download_file('https://microbiology.se/sw/Metaxa2_2.2.1.tar.gz',
                  join(refs_dir, 'Metaxa2_2.2.1.tar.gz'))
if not isfile(join(refs_dir, 'PhytoRef_with_taxonomy.fasta')):
    download_file('http://phytoref.sb-roscoff.fr/static/downloads/PhytoRef_with_taxonomy.fasta',
                  join(refs_dir, 'PhytoRef_with_taxonomy.fasta'))

with tarfile.open(join(refs_dir, 'gg_13_8_otus.tar.gz'), 'r:gz') as tar:
    tar.extractall(refs_dir)
with tarfile.open(join(refs_dir, 'Metaxa2_2.2.1.tar.gz'), 'r:gz') as tar:
    tar.extractall(refs_dir)

os.chdir(join(refs_dir, 'Metaxa2_2.2.1', 'metaxa2_db', 'SSU'))
blast_params = ['blastdbcmd', '-entry', 'all', '-db', 'blast', '-out', 'metaxa2.fasta']
subprocess.run(blast_params)
shutil.copyfile(join(refs_dir, 'Metaxa2_2.2.1', 'metaxa2_db', 'SSU', 'metaxa2.fasta'), 
                join(refs_dir, 'metaxa2.fasta'))
os.chdir(join(working_dir, 'procedure'))

with open(join(refs_dir, 'silva_organelle_taxonomy.tsv'), 'w') as silva_taxonomy:
    with open(join(refs_dir, 'gg_organelle_taxonomy.tsv'), 'w') as gg_taxonomy:
        silva_taxonomy.write('Feature ID\tTaxon\n')
        gg_taxonomy.write('Feature ID\tTaxon\n')
        with open(join(refs_dir, 'organelle_sequences.fasta'), 'w') as organelle_seqs:
            for i, entry in enumerate(SeqIO.parse(join(refs_dir, 'metaxa2.fasta'), 'fasta')):
                if 'mitochondria' in entry.description or 'Mitochondria' in entry.description:
                    organelle_seqs.write('>metaxa2_mitochondria_' + str(i) + '\n')
                    organelle_seqs.write(str(entry.seq + '\n'))
                    specific_info = str(entry.description).split(';')[-1]
                    silva_taxonomy.write('metaxa2_mitochondria_' + str(i) + '\td__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Rickettsiales; f__Mitochondria; g__Mitochondria; s__' + specific_info + '\n')
                    gg_taxonomy.write('metaxa2_mitochondria_' + str(i) + '\tk__Bacteria; p__Proteobacteria; c__Alphaproteobacteria; o__Rickettsiales; f__mitochondria; g__Mitochondria; s__' + specific_info + '\n')
            for i, entry in enumerate(SeqIO.parse(join(refs_dir, 'PhytoRef_with_taxonomy.fasta'), 'fasta')):
                if not 'XXXXXXXXXX' in entry.seq:   #ditch the weird sequence
                    organelle_seqs.write('>phytoref_chloroplast_' + str(i) + '\n')
                    organelle_seqs.write(str(entry.seq + '\n'))
                    specific_info = str(entry.description).split('|')[-1]
                    silva_taxonomy.write('phytoref_chloroplast_' + str(i) + '\td__Bacteria; p__Cyanobacteria; c__Cyanobacteriia; o__Chloroplast; f__Chloroplast; g__Chloroplast; s__' + specific_info + '\n')
                    gg_taxonomy.write('phytoref_chloroplast_' + str(i) + '\tk__Bacteria; p__Cyanobacteria; c__Chloroplast; o__Chloroplast; f__Chloroplast; g__Chloroplast; s__' + specific_info + '\n')

#import, select V4 region, merge, save
organelle_seqs = Artifact.import_data('FeatureData[Sequence]',
                                      join(refs_dir, 'organelle_sequences.fasta'))
v4_organelle_seqs, = extract_reads(organelle_seqs, 'GTGYCAGCMGCCGCGGTAA',
                                   'GGACTACNVGGGTWTCTAAT', n_jobs = 24,
                                   read_orientation = 'forward')
silva_extended_seqs, = merge_seqs([v4_organelle_seqs,
                                   Artifact.load(refs_dir +
                                                 '/silva_sequences.qza')])
silva_extended_seqs.save(join(refs_dir, 'silva_extended_sequences.qza'))
gg_seqs = Artifact.import_data('FeatureData[Sequence]', refs_dir +
                               '/gg_13_8_otus/rep_set/99_otus.fasta')
#did trimming greengenes break everything?
v4_gg_seqs, = extract_reads(gg_seqs, 'GTGYCAGCMGCCGCGGTAA',
                            'GGACTACNVGGGTWTCTAAT', n_jobs = 24,
                            read_orientation = 'forward')
v4_gg_seqs.save(join(refs_dir, 'gg_sequences.qza'))
gg_extended_seqs, = merge_seqs([organelle_seqs, gg_seqs])
gg_extended_seqs.save((refs_dir, 'gg_extended_sequences.qza'))

silva_organelle_taxonomy = Artifact.import_data('FeatureData[Taxonomy]',
                                                refs_dir +
                                                '/silva_organelle_taxonomy.tsv')
silva_extended_taxonomy, = merge_taxa([silva_organelle_taxonomy,
                                       Artifact.load(refs_dir +
                                                     '/silva_taxonomy.qza')])
silva_extended_taxonomy.save(join(refs_dir, 'silva_extended_taxonomy.qza'))
gg_taxonomy = Artifact.import_data('FeatureData[Taxonomy]', join(refs_dir,
                                                                 'gg_13_8_otus',
                                                                 'taxonomy',
                                                                 '99_otu_taxonomy.txt'),
                                   'HeaderlessTSVTaxonomyFormat')
gg_taxonomy.save(join(refs_dir, 'gg_taxonomy.qza'))
gg_organelle_taxonomy = Artifact.import_data('FeatureData[Taxonomy]',
                                             join(refs_dir,
                                             'gg_organelle_taxonomy.tsv'))
gg_extended_taxonomy, = merge_taxa([gg_organelle_taxonomy, gg_taxonomy])
gg_extended_taxonomy.save(join(refs_dir, 'gg_extended_taxonomy.qza'))

#generate naive bayes classifiers
for reference in ['gg', 'gg_extended', 'silva', 'silva_extended']:
    if not exists(join(working_dir, 'output', reference + '_nb_classifier.qza')):
        ref_reads = Artifact.load(join(refs_dir, reference + '_sequences.qza'))
        ref_taxonomy = Artifact.load(join(refs_dir, reference + '_taxonomy.qza'))
        classifier, = fit_classifier_naive_bayes(ref_reads, ref_taxonomy)
        classifier.save(join(working_dir, 'output', reference + '_nb_classifier.qza'))
