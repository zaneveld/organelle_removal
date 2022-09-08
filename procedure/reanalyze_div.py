from glob import glob
from os.path import join
import re
import tempfile


from ast import literal_eval
from bs4 import BeautifulSoup
import pandas as pd
from qiime2 import Artifact, Metadata, Visualization
from qiime2.plugins.diversity.pipelines import core_metrics_phylogenetic
from qiime2.plugins.diversity.visualizers import alpha_group_significance, beta_group_significance
from qiime2.plugins.feature_table.methods import filter_samples, rarefy
from qiime2.plugins.feature_table.visualizers import summarize

def parse_adiv_group_sig_jsonp_file(input_file):
    """Parse a jsonp file by crudely scraping out the H and p values for the overall analysis    
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
denoisers = ['dada2', 'deblur']
filters = ['filtered', 'unfiltered']
classifiers = ['vsearch', 'nb']
references = ['silva', 'silva_extended']#, 'gg', 'gg_extended']
columns_of_interest = {'GCMP':['tissue_compartment', 'family'], 'GSMP':['host_scientific_name', 'empo_3'], 'human_gut':['life_stage', 'env_biome'], 'milk':['season', 'silo_lot_id'], 'peru_ants':['genus', 'habitat'], 'song':['class', 'country']}
filter_criteria = ['D', 'Not applicable', 'Not collected', 'not provided', 'TS', 'W', '', 'incertae sedis', 'not applicable', 'sponges', 'NA', 'Missing', 'unknown']
alpha_diversity_metrics = ['faiths_pd', 'obs_features', 'shannon_div', 'evenness']
beta_diversity_metrics = ['unweighted_unifrac', 'weighted_unifrac', 'jaccard', 'bray_curtis']
div_results = []

for study in studies:
    md_path = join(working_dir, 'input', study, 'sample_metadata.txt')
    md = Metadata.load(md_path)
    for denoiser in denoisers:
        phylogeny_path = join(working_dir, 'output', f'{study}_{denoiser}_unfiltered_tree.qza')
        phylogeny = Artifact.load(phylogeny_path)
        for filtered in filters:
            for classifier in classifiers:
                filtered_base_table = Artifact.load(join(working_dir, 'output', f'{study}_{denoiser}_{filtered}_silva_{classifier}_harmonized_filtered_table.qza'))
                filtered_extended_table = Artifact.load(join(working_dir, 'output', f'{study}_{denoiser}_{filtered}_silva_extended_{classifier}_harmonized_filtered_table.qza'))            
                for reference in references:
                    output_path = join(working_dir, 'output', f'{study}_{denoiser}_{filtered}_{reference}_{classifier}_')
                    unweighted_unifrac = Artifact.load(f'{output_path}unweighted_unifrac.qza')
                    weighted_unifrac = Artifact.load(f'{output_path}weighted_unifrac.qza')
                    jaccard = Artifact.load(f'{output_path}jaccard.qza')
                    bray_curtis = Artifact.load(f'{output_path}bray_curtis.qza')
                    with tempfile.TemporaryDirectory() as temp_dir:
                        for column in columns_of_interest[study]:
                            md_column = md.get_column(column)
                            for a_metric in alpha_diversity_metrics:
                                qzv = Visualization.load(join(working_dir, 'output', f'{output_path}{a_metric}.qzv'))
                                qzv.export_data(temp_dir)
                                filename = 'column-' + column + '.jsonp'
                                H_and_p = parse_adiv_group_sig_jsonp_file(join(temp_dir, filename))
                                div_results.append([study, denoiser, filtered, reference, classifier, 'alpha', a_metric, column, H_and_p['H'], H_and_p['p']])
                            for b_metric in beta_diversity_metrics:
                                qzv = Visualization.load(join(working_dir, 'output', f'{output_path}{column}_{b_metric}.qzv'))
                                qzv.export_data(temp_dir)
                                b_div_results = parse_bdiv_results_html_file(join(temp_dir, 'index.html'))
                                div_results.append([study, denoiser, filtered, reference, classifier, 'beta', (b_metric + '_' + b_div_results[0]), column, b_div_results[4], b_div_results[5]])
    pd.DataFrame(div_results, columns = ['study', 'denoiser', 'positive filter', 'reference', 'classifier', 'diversity_type', 'diversity_metric', 'comparison_column', 'test_statistic', 'p']).to_csv(join(working_dir, 'output', f'{study}_diversity_stats_tests.csv'))
pd.DataFrame(div_results, columns = ['study', 'denoiser', 'positive filter' 'reference', 'classifier', 'diversity_type', 'diversity_metric', 'comparison_column', 'test_statistic', 'p']).to_csv(join(working_dir, 'output', 'diversity_stats_tests.csv'))
