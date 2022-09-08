from qiime2.plugins.fragment_insertion.methods import sepp
from qiime2 import Artifact

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
sepp_ref = Artifact.load(working_dir + '/taxonomy_references/sepp-refs-gg-13-8.qza')
for study in ['peru_ants']:#, 'GCMP', 'GSMP', 'human_gut', 'milk', 'song']:
    for denoiser in ['dada2', 'deblur']:
        rep_seqs = Artifact.load(working_dir + '/input/' + study + '_' + denoiser + '_unfiltered_merged_seqs.qza')
        rooted_tree, placements = sepp(rep_seqs, sepp_ref, 10)
        rooted_tree.save(working_dir + '/output/' + study + '_' + denoiser + '_unfiltered_tree.qza')
        placements.save(working_dir + '/output/' + study + '_' + denoiser + '_placements.qza')
