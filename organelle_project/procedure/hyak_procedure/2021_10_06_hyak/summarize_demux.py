import glob
import os
from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.demux.visualizers import summarize

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for study in ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']:
    for seq_path in glob.glob(working_dir + '/input/' + study + '/demuxed*seqs.qza'):
        seqs = Artifact.load(seq_path)
        qza_name = os.path.basename(seq_path)
        artifact_id = qza_name.rstrip('_seqs.qza').lstrip('demuxed_')
        summary = summarize(seqs)
        summary.save(working_dir + '/input/' + study + '/' + artifact_id + '_demux_summary.qzv')
