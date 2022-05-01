#find highest-frequency unknown sequences in GCMP and BLAST them

from os.path import join
import tempfile
import subprocess

import pandas as pd

from qiime2 import Artifact, Metadata
from qiime2.plugins.feature_table.methods import relative_frequency, rename_ids
from qiime2.plugins.taxa.methods import filter_table

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

rep_seqs = Artifact.load(join(working_dir, 'input', 'GCMP_dada2_unfiltered_merged_seqs.qza'))
with tempfile.TemporaryDirectory() as temp_dir:
    rep_seqs.export_data(temp_dir)
    with open(join(temp_dir, 'dna-sequences.fasta')) as infile:
        with open(join(temp_dir, 'new_metadata.tsv'), 'w') as outfile:
            outfile.write('feature-id\tsequence\n')
            for line in infile:
                if line.startswith('>'):
                    outfile.write(line.lstrip('>').rstrip('\n') + '\t')
                else:
                    outfile.write(line)
    new_ids = Metadata.load(join(temp_dir, 'new_metadata.tsv'))
new_names = new_ids.get_column('sequence')
#this ft needs to be filtered to only include 'unknown' sequences
ft = Artifact.load(join(working_dir, 'input', 'GCMP_dada2_unfiltered_merged_ft.qza'))
taxonomy = Artifact.load(join(working_dir, 'output', 'GCMP_dada2_unfiltered_gg_vsearch_classification_taxonomy.qza'))
#first, transform to relative frequency, export as biom, import as feature table[frequency].
#this lets us filter the relative frequency table
relative_ft, = relative_frequency(ft)
with tempfile.TemporaryDirectory() as temp_dir:
    relative_ft.export_data(temp_dir)
    ft = Artifact.import_data('FeatureTable[Frequency]', join(temp_dir, 'feature-table.biom'))

unknown_ft, = filter_table(ft, taxonomy, include = 'Unassigned')
new_ft, = rename_ids(unknown_ft, new_names, 'feature')
with tempfile.TemporaryDirectory() as temp_dir:
    new_ft.export_data(temp_dir)
    fp = join(temp_dir, 'feature-table.biom')
    new_fp = join(temp_dir, 'biom_table.txt')
    params = ['biom', 'convert', '-i', fp, '-o', new_fp, '--to-tsv']
    subprocess.run(params)
    biom_df = pd.read_csv(new_fp, sep = '\t', index_col = 0, skiprows = 1)
biom_df['total_proportion'] = biom_df.sum(axis = 1) / 1439
top_seqs = []
proportions = biom_df['total_proportion'].to_frame().transpose()
for i in range(1000):
    top_seq = proportions.idxmax(axis = 1).iat[0]
    proportions = proportions.drop(top_seq, axis = 1)
    top_seqs.append(top_seq)
with open(join(working_dir, 'output', 'GCMP_top_unknown_seqs.fasta'), 'w') as file:
    for i, seq in enumerate(top_seqs):
        file.write('>' + str(i) + '\n' + seq + '\n')
#export BLASTDB=/gscratch/zaneveld/BLAST/blastdb
blast_params = ['/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn', '-db',
                'nt', '-query', join(working_dir, 'output',
                'GCMP_top_unknown_seqs.fasta'), '-num_threads', '10',
                '-max_target_seqs', '5', '-max_hsps', '1', '-outfmt',
                '6 qseqid sseqid staxids stitle evalue bitscore', '-out',
                join(working_dir, 'output', 'GCMP_top_unknowns_blast.tsv')]
subprocess.run(blast_params)
