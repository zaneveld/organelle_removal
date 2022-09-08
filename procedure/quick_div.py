from glob import glob
from os.path import join
import tempfile
import re
from ast import literal_eval
import pandas as pd
from qiime2 import Artifact, Metadata, Visualization
from qiime2.plugins.diversity.pipelines import core_metrics_phylogenetic
from qiime2.plugins.diversity.visualizers import alpha_group_significance, beta_group_significance
from qiime2.plugins.feature_table.methods import filter_samples, rarefy
from qiime2.plugins.feature_table.visualizers import summarize
from bs4 import BeautifulSoup
def parse_adiv_group_sig_jsonp_file(input_file):
    """Parse a jsonp file by crudly scraping out the H and p values for the overall analysis    
    """

    file_text = open(input_file).read()
    file_fields = re.split("[{}]",file_text)
    results = {}
    for i,field in enumerate(file_fields):    
        if '"H":' in field:
            stats_result_dict = literal_eval("{"+f"{field}"+"}")
            results.update(stats_result_dict)
            
        if '"initial"' in field:
            n_samples_dict = literal_eval("{"+f"{field}"+"}")
            results.update(n_samples_dict)
    return results

def parse_bdiv_results_html_file(input_file):
    """parse the html file from an exported beta diversity qzv, returning method name, test statistic name, sample size, number of groups, test statistic, p-value, and number of permutations"""

    results = []
    file_text = open(input_file).read()
    parsed = BeautifulSoup(file_text, 'html.parser')
    for txt in parsed.find_all('td'):
        results.append(txt.string.lstrip('<td>').rstrip('</td>'))
    
    results = tuple(results)

    return results


working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song']
denoisers = ['dada2'] 'deblur']
classifiers = ['vsearch', 'nb']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']
columns_of_interest = {'GCMP':['tissue_compartment', 'family'], 'GSMP':['host_scientific_name', 'empo_3'], 'human_gut':['life_stage', 'env_biome'], 'milk':['season', 'silo_lot_id'], 'peru_ants':['genus', 'habitat']}
filter_criteria = ['D', 'Not applicable', 'Not collected', 'not provided', 'TS', 'W', '', 'incertae sedis', 'not applicable', 'sponges', 'NA', 'Missing']
alpha_diversity_metrics = ['faiths_pd', 'obs_features', 'shannon_div', 'evenness']
beta_diversity_metrics = ['unweighted_unifrac', 'weighted_unifrac', 'jaccard', 'bray_curtis']
div_results = []

for study in studies:
    md_path = join(working_dir, 'input', study, 'sample_metadata.txt')
    md = Metadata.load(md_path)
    for denoiser in denoisers:
        for classifier in classifiers:
            base_ft = Artifact.load(join(working_dir, 'output', (study + '_' + denoiser + '_silva_' + classifier + '_filtered_ft.qza')))
            base_rarefied_table, = rarefy(base_ft, 1000)
            base_rarefied_table.save(join(working_dir, 'output', (study + '_' + denoiser + '_silva_' + classifier + '_rarefied_table.qza')))
            base_qzv, = summarize(base_rarefied_table, md)
            extended_ft = Artifact.load(join(working_dir, 'output', (study + '_' + denoiser + '_silva_extended_' + classifier + '_filtered_ft.qza')))
            extended_rarefied_table, = rarefy(extended_ft, 1000)
            extended_rarefied_table.save(join(working_dir, 'output', (study + '_' + denoiser + '_silva_extended_' + classifier + '_rarefied_table.qza')))
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
            filtered_base_table, = filter_samples(base_rarefied_table, metadata = extended_ids)
            filtered_extended_table, = filter_samples(extended_rarefied_table, metadata = base_ids)
            for column in columns_of_interest[study]:
                #set up the SQLite WHERE clause to filter out samples with bad data
                #this is a complicated line due to the various escapes when passing through python and SQLite
                where = "'" + column + "'" + "='" + ("' OR " + "'" + column + "'" + "='").join(filter_criteria) + "'"

                filtered_base_table, = filter_samples(filtered_base_table, metadata = md, where = where, exclude_ids = True)
                filtered_extended_table, = filter_samples(filtered_extended_table, metadata = md, where = where, exclude_ids = True)
            filtered_base_table.save(join(working_dir, 'output', (study + '_' + denoiser + '_silva_' + classifier + '_harmonized_filtered_table.qza')))
            filtered_extended_table.save(join(working_dir, 'output', 'diversity', (study + '_' + denoiser + '_silva_extended_' + classifier + '_harmonized_filtered_table.qza')))            
            for reference in references:
                output_path = join(working_dir, 'output', (study + '_' + denoiser + '_' + reference + '_' + classifier + '_'))
                ft = Artifact.load(output_path + 'harmonized_table.qza')
                #observed features, gini_index, dominance
                obs_features = alpha(ft, 'observed_features')
                obs_features.save(output_path + 'obs_features.qza')
                alpha_group_significance(obs_features, md)[0].save(output_path + 'obs_features.qzv')
                gini = alpha(ft, 'gini_index')
                gini.save(output_path + 'gini_index.qza')
                alpha_group_significance(gini, md)[0].save(output_path + 'gini_index.qzv')
                dominance = (ft, 'dominance')
                dominance.save(output_path + 'dominance.qza')
                alpha_group_significance(dominance, md)[0].save(output_path + 'dominance.qzv')
                
                #rarefied_table, faiths_pd, obs_features, shannon_div, evenness, unweighted_unifrac, weighted_unifrac, jaccard, bray_curtis, unweighted_unifrac_pcoa, weighted_unifrac_pcoa, jaccard_pcoa, bray_curtis_pcoa, unweighted_unifrac_emperor, weighted_unifrac_emperor, jaccard_emperor, bray_curtis_emperor = core_metrics_phylogenetic(ft, phylogeny, 1000, md, 'auto')
                #faiths_pd.save(output_path + 'faiths_pd.qza')
                alpha_group_significance(faiths_pd, md)[0].save(output_path + 'faiths_pd.qzv')
                obs_features.save(output_path + 'obs_features.qza')
                alpha_group_significance(obs_features, md)[0].save(output_path + 'obs_features.qzv')
                shannon_div.save(output_path + 'shannon_div.qza')
                alpha_group_significance(shannon_div, md)[0].save(output_path + 'shannon_div.qzv')
                evenness.save(output_path + 'evenness.qza')
                alpha_group_significance(evenness, md)[0].save(output_path + 'evenness.qzv')
                unweighted_unifrac.save(output_path + 'unweighted_unifrac.qza')
                weighted_unifrac.save(output_path + 'weighted_unifrac.qza')
                jaccard.save(output_path + 'jaccard.qza')
                bray_curtis.save(output_path + 'bray_curtis.qza')
                unweighted_unifrac_pcoa.save(output_path + 'unweighted_unifrac_pcoa.qza')
                weighted_unifrac_pcoa.save(output_path + 'weighted_unifrac_pcoa.qza')
                jaccard_pcoa.save(output_path + 'jaccard_pcoa.qza')
                bray_curtis_pcoa.save(output_path + 'bray_curtis_pcoa.qza')
                unweighted_unifrac_emperor.save(output_path + 'unweighted_unifrac_emperor.qzv')
                weighted_unifrac_emperor.save(output_path + 'weighted_unifrac_emperor.qzv')
                jaccard_emperor.save(output_path + 'jaccard_emperor.qzv')
                bray_curtis_emperor.save(output_path + 'bray_curtis_emperor.qzv')
                with tempfile.TemporaryDirectory() as temp_dir:
                    for column in columns_of_interest[study]:
                        md_column = md.get_column(column)
                        beta_group_significance(unweighted_unifrac, md_column)[0].save(output_path + column + '_unweighted_unifrac.qzv')
                        beta_group_significance(weighted_unifrac, md_column)[0].save(output_path + column + '_weighted_unifrac.qzv')
                        beta_group_significance(jaccard, md_column)[0].save(output_path + column + '_jaccard.qzv')
                        beta_group_significance(bray_curtis, md_column)[0].save(output_path + column + '_bray_curtis.qzv')
                        
                        for a_metric in alpha_diversity_metrics:
                            qzv = Visualization.load(join(working_dir, 'output', (study + '_' + denoiser + '_' + reference + '_' + classifier + '_' + a_metric + '.qzv')))
                            qzv.export_data(temp_dir)
                            filename = 'column-' + column + '.jsonp'
                            H_and_p = parse_adiv_group_sig_jsonp_file(join(temp_dir, filename))
                            div_results.append([study, denoiser, reference, classifier, 'alpha', a_metric, column, H_and_p['H'], H_and_p['p']])
                        for b_metric in beta_diversity_metrics:
                            qzv = Visualization.load(join(working_dir, 'output', (study + '_' + denoiser + '_' + reference + '_' + classifier + '_' + column + '_' + b_metric + '.qzv')))
                            qzv.export_data(temp_dir)
                            b_div_results = parse_bdiv_results_html_file(join(temp_dir, 'index.html'))
                            div_results.append([study, denoiser, reference, classifier, 'beta', (b_metric + '_' + b_div_results[0]), column, b_div_results[4], b_div_results[5]])

pd.DataFrame(div_results, columns = ['study', 'denoiser', 'reference', 'classifier', 'diversity_type', 'diversity_metric', 'comparison_column', 'test_statistic', 'p']).to_csv(join(working_dir, 'output', 'diversity_stats_tests.csv'))
