from qiime2.plugins.fragment_insertion.methods import sepp
from qiime2 import Artifact

#this script hangs for days when run through sbatch, for unknown reasons
working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
sepp_ref = Artifact.load(working_dir + '/taxonomy_references/sepp-refs-silva-128.qza')
for study in ['peru_ants']:#, 'GCMP', 'GSMP', 'human_gut', 'milk', 'song']:
    for denoiser in ['dada2', 'deblur']:
        rep_seqs = Artifact.load(working_dir + '/input/' + study + '_' + denoiser + '_merged_seqs.qza')
        rooted_tree, placements = sepp(rep_seqs, sepp_ref, 40)
        rooted_tree.save(working_dir + '/output/' + study + '_' + denoiser + '_rooted_tree.qza')
        placements.save(working_dir + '/output/' + study + '_' + denoiser + 'placements.qza')
