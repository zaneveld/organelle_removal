#this takes ~44 hours on hyak

import glob
import os
from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.demux.methods import emp_single
from qiime2.plugins.demux.visualizers import summarize
from qiime2 import Visualization

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for study in ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'mocks', 'song']:
    for seq_path in glob.glob(working_dir + '/input/' + study + '/*/*seqs.qza', recursive = True):
        seqs = Artifact.load(seq_path)
        seq_id = os.path.basename(os.path.dirname(seq_path))
        md_path = working_dir + '/input/' + study + '/' + seq_id + '/barcodes.tsv'
        metadata = Metadata.load(md_path)
        barcodes = metadata.get_column('barcode')
        if study == 'GCMP' or study == 'GSMP' or study == 'peru_ants':
            demuxed_seqs, stats = emp_single(seqs, barcodes, rev_comp_mapping_barcodes = True)
        elif study == 'milk':
            demuxed_seqs, stats = emp_single(seqs, barcodes, golay_error_correction = False)
        else:
            demuxed_seqs, stats = emp_single(seqs, barcodes)
        demuxed_seqs.save(working_dir + '/input/' + study + '/' + seq_id + '/demuxed_' + seq_id + '_seqs.qza')
        stats.save(working_dir + '/input/' + study + '/' + seq_id + '/' + seq_id + '_demux_stats.qza')
        demux_summary, = summarize(demuxed_seqs)
        demux_summary.save(working_dir + '/input/' + study + '/' + seq_id + '/' + seq_id + '_demux.qzv')
