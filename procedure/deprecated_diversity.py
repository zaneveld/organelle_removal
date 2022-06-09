from os.path import join
import tempfile

import pandas as pd
from qiime2 import Artifact, Metadata, Visualization
from qiime2.plugins.diversity.pipelines import core_metrics_phylogenetic
from qiime2.plugins.diversity.visualizers import alpha_group_significance, beta_group_significance
from qiime2.plugins.feature_table.methods import filter_samples, rarefy
from qiime2.plugins.feature_table.visualizers import summarize


working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']
denoisers = ['dada2']#['dada2', 'deblur']
classifiers = ['vsearch', 'nb']
references = ['silva', 'silva_extended']#['gg', 'gg_extended', 'silva', 'silva_extended']


for study in studies:
    md_path = join(working_dir, 'input', study, 'sample_metadata.txt')
    md = Metadata.load(md_path)
    for denoiser in denoisers:
        phylogeny_path = join(working_dir, 'output', (study + '_' + denoiser + '_rooted_tree.qza'))
        phylogeny = Artifact.load(phylogeny_path)
        for classifier in classifiers:
            base_ft = Artifact.load(join(working_dir, 'output', (study + '_' + denoiser + '_silva_' + classifier + '_filtered_ft.qza')))
            base_rarefied_table, = rarefy(base_ft, 1000)
            base_rarefied_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_silva_' + classifier + '_rarefied_table.qza')))
            base_qzv, = summarize(base_rarefied_table, md)
            extended_ft = Artifact.load(join(working_dir, 'output', (study + '_' + denoiser + '_silva_extended_' + classifier + '_filtered_ft.qza')))
            extended_rarefied_table, = rarefy(extended_ft, 1000)
            extended_rarefied_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_silva_extended_' + classifier + '_rarefied_table.qza')))
            extended_qzv, = summarize(extended_rarefied_table, md)
            #make metadata objects with sample IDs from each rarefied table 
            with tempfile.TemporaryDirectory() as temp_dir:
                base_qzv.export_data(temp_dir)
                df = pd.read_csv(join(temp_dir, 'sample-frequency-detail.csv'), index_col = 0)
                df.index.name = '#SampleID'
                base_ids = Metadata(df)
                extended_qzv.export_data(temp_dir)
                df = pd.read_csv(join(temp_dir, 'sample-frequency-detail.csv'), index_col = 0)
                df.index.name = '#SampleID'
                extended_ids = Metadata(df)
            harmonized_base_table, = filter_samples(base_rarefied_table, metadata = extended_ids)
            harmonized_base_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_silva_' + classifier + '_harmonized_table.qza')))
            harmonized_extended_table, = filter_samples(extended_rarefied_table, metadata = base_ids)
            harmonized_extended_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_silva_extended_' + classifier + '_harmonized_table.qza')))            
            for reference in references:
                output_path = join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_' + reference + '_' + classifier + '_'))
                ft = Artifact.load(output_path + 'harmonized_table.qza')
                rarefied_table, faiths_pd, obs_features, shannon_div, evenness, unweighted_unifrac, weighted_unifrac, jaccard, bray_curtis, unweighted_unifrac_pcoa, weighted_unifrac_pcoa, jaccard_pcoa, bray_curtis_pcoa, unweighted_unifrac_emperor, weighted_unifrac_emperor, jaccard_emperor, bray_curtis_emperor = core_metrics_phylogenetic(ft, phylogeny, 1000, md, 'auto')
                #rarefied_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_' + reference + '_' + classifier + '_rarefied_table.qza')))
                faiths_pd.save(output_path + 'faiths_pd.qza')
                alpha_group_significance(faiths_pd, md)[0].save(output_path + 'faiths_pd.qzv')
                obs_features.save(output_path + 'obs_features.qza')
                alpha_group_significance(obs_features, md)[0].save(output_path + 'obs_features.qzv')
                shannon_div.save(output_path + 'shannon_div.qza')
                alpha_group_significance(shannon_div, md)[0].save(output_path + 'shannon_div.qzv')
                evenness.save(output_path + 'evenness.qza')
                alpha_group_significance(evenness, md)[0].save(output_path + 'evenness.qzv')
                unweighted_unifrac.save(output_path + 'unweighted_unifrac.qza')
                #beta_group_significance(unweighted_unifrac, md, pairwise = True)[0].save(output_path + 'unweighted_unifrac.qzv')
                weighted_unifrac.save(output_path + 'weighted_unifrac.qza')
                #beta_group_significance(weighted_unifrac, md, pairwise = True)[0].save(output_path + 'weighted_unifrac.qzv')
                jaccard.save(output_path + 'jaccard_dm.qza')
                #beta_group_significance(jaccard, md, pairwise = True)[0].save(output_path + 'jaccard.qzv')
                bray_curtis.save(output_path + 'bray_curtis_dm.qza')
                #beta_group_significance(bray_curtis, md, pairwise = True)[0].save(output_path + 'bray_curtis.qzv')
                unweighted_unifrac_pcoa.save(output_path + 'unweighted_unifrac_pcoa.qza')
                weighted_unifrac_pcoa.save(output_path + 'weighted_unifrac_pcoa.qza')
                jaccard_pcoa.save(output_path + 'jaccard_pcoa.qza')
                bray_curtis_pcoa.save(output_path + 'bray_curtis_pcoa.qza')
                unweighted_unifrac_emperor.save(output_path + 'unweighted_unifrac_emperor.qzv')
                weighted_unifrac_emperor.save(output_path + 'weighted_unifrac_emperor.qzv')
                jaccard_emperor.save(output_path + 'jaccard_emperor.qzv')
                bray_curtis_emperor.save(output_path + 'bray_curtis_emperor.qzv')

