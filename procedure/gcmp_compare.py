from qiime2 import Artifact
from qiime2.plugins.diversity.pipelines import core_metrics
from qiime2 import Metadata
from qiime2 import Visualization

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
md = Metadata.load(working_dir + '/output/comparisons/GCMP_metadata.txt')
for reference in ['silva', 'silva_extended']:
    for compartment in ['M', 'T', 'S']:
        ft = Artifact.load(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + '_ft.qza')
        rt, obs_features, shannon, evenness, jaccard, bc, jaccard_pcoa, bc_pcoa, jaccard_emperor, bc_emperor, = core_metrics(ft, 1000, md)
        rt.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'rarefied_table.qza')
        obs_features.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'obs_features.qza')
        shannon.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'shannon.qza')
        evenness.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'evenness.qza')
        jaccard.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'jaccard.qza')
        bc.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'bray_curtis.qza')
        jaccard_pcoa.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'jaccard_pcoa.qza')
        bc_pcoa.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'bc_pcoa.qza')
        jaccard_emperor.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'jaccard_emperor.qzv')
        bc_emperor.save(working_dir + '/output/comparisons/GCMP_dada2_' + reference + '_nb_' + compartment + 'bc_emperor.qzv')
