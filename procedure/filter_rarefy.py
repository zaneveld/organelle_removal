from qiime2 import Artifact
from qiime2 import Visualization
from qiime2.plugins.diversity.visualizers import alpha_rarefaction
from qiime2.plugins.taxa.methods import filter_table, filter_seqs

for study in ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song', 'mocks']:
    for denoiser in ['dada2', 'deblur']:
        ft = Artifact.load('/gscratch/zaneveld/sonettd/organelle_removal/input/' + study + '_' + denoiser + '_merged_ft.qza')
        seqs = Artifact.load('/gscratch/zaneveld/sonettd/organelle_removal/input/' + study + '_' + denoiser + '_merged_seqs.qza')
        for classifier in ['nb', 'vsearch']:
            for ref in ['gg', 'gg_extended', 'silva', 'silva_extended']:
                taxonomy = Artifact.load('/gscratch/zaneveld/sonettd/organelle_removal/output/' + study + '_' + denoiser + '_' + ref + '_' + classifier + '_classification_taxonomy.qza')
                if 'gg' in ref:
                    cp_name = 'k__Bacteria;p__Cyanobacteria;c__Chloroplast'
                    mc_name = 'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'
                else:
                    cp_name = 'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast'
                    mc_name = 'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria'
                exclude = cp_name + ',' + mc_name
                filtered_table, = filter_table(ft, taxonomy, exclude = exclude)
                filtered_table.save('/gscratch/zaneveld/sonettd/organelle_removal/output/' + study + '_' + denoiser + '_' + ref + '_' + classifier + '_filtered_ft.qza')
                filtered_seqs, = filter_seqs(seqs, taxonomy, exclude = exclude)
                filtered_seqs.save('/gscratch/zaneveld/sonettd/organelle_removal/output/' + study + '_' + denoiser + '_' + ref + '_' + classifier + '_filtered_seqs.qza')
                #rarefaction_curves, = alpha_rarefaction(filtered_table, 10000)
                #rarefaction_curves.save('/gscratch/zaneveld/sonettd/organelle_removal/output/rarefaction_curves/' + study + '_' + denoiser + '_' + ref + '_curves.qzv')
