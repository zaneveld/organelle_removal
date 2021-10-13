import glob
from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import merge
from qiime2.plugins.feature_table.methods import merge_seqs


working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for study in ['human_gut']:#'GCMP', 'GSMP', 'milk', 'peru_ants']:
    for denoiser in ['dada2', 'deblur']:
        seqs = []
        for seq_path in glob.glob(working_dir + '/output/' + study + '_*_' + denoiser + '_rep_seqs.qza'):
            seqs.append(Artifact.load(seq_path))
        merged_seqs, = merge_seqs(seqs)
        seqs = None
        merged_seqs.save(working_dir + '/output/' + study + '_' + denoiser + '_merged_seqs.qza')
        merged_seqs = None
        fts = []
        for ft_path in glob.glob(working_dir + '/output/' + study + '_*_' + denoiser + '_ft.qza'):
            fts.append(Artifact.load(ft_path))
        merged_ft, = merge(fts)
        fts = None
        merged_ft.save(working_dir + '/output/' + study + '_' + denoiser + '_merged_ft.qza')
