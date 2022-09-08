from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import filter_samples
from qiime2.metadata import Metadata

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
md = Metadata.load(working_dir + '/output/comparisons/GCMP_metadata.txt')
for denoiser in ['dada2', 'deblur']:
    for classifier in ['nb', 'vsearch']:
        for reference in ['gg', 'gg_extended', 'silva', 'silva_extended']:
            ft = Artifact.load(working_dir + '/output/GCMP_' + denoiser + '_' + reference + '_' + classifier + '_filtered_ft.qza')
            for compartment in ['M', 'T', 'S']:
                where = "tissue_compartment='" + compartment + "'"
                compartment_ft, = filter_samples(ft, metadata = md, where = where)
                compartment_ft.save(working_dir + '/output/comparisons/GCMP_' + denoiser + '_' + reference + '_' + classifier + '_' + compartment + '_ft.qza')
