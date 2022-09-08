import os
import pandas as pd
import tempfile

from qiime2 import Visualization


def get_proportions_and_counts(dataframe, taxon, results_label = None):
    """calculate the per-sample proportion of a given taxon from a qiime2 taxa barplot (in dataframe form)
    
    Parameters
    -----------
    dataframe : pandas DataFrame built from a qiime2 taxa barplot visualization
    taxon : str, name of column of interest
    results_label : str, suffix (with 'proportion' or 'absolute') of results columns, e.g. 'unassigned', 'mitochondria'

    Returns
    -----------
    results : pandas DataFrame with the original index, a column of proportions, and a column of counts"""
    
    #copy the df, otherwise the changes will be passed to the original
    dataframe = dataframe.copy()
    #if results_label not passed, default to taxon name
    if results_label == None:
        results_label = taxon
    proportion_label = 'proportion ' + results_label
    count_label = 'absolute ' + results_label

    #sum the counts of each sample
    dataframe['total'] = dataframe.sum(1)
    #divide the column of interest by the total to find the proportion
    if taxon in dataframe.columns:
        dataframe[proportion_label] = dataframe[taxon] / dataframe['total']
        dataframe[count_label] = dataframe[taxon]
    else:
        dataframe[proportion_label] = 0
        dataframe[count_label] = 0
    #empty the df of everything but the index, proportions, and counts
    results = dataframe[[proportion_label, count_label]]


    return results

# def find_proportion(dataframe, taxon_label, proportion_label = 'proportion_' + taxon_label):
#     """calculate the per-sample proportion of a given taxon from a qiime2 taxa barplot (converted to pandas dataframe)
    
#     Parameters
#     -----------
#     dataframe : pandas DataFrame built from a qiime2 taxa barplot visualization
#     taxon_label : str, name of column of interest
#     proportion_label : str, name of results column (defaults to ('proportion_' + taxon_label))

#     Returns
#     -----------
#     proportions : pandas DataFrame with the original index and a single column of calculated proportions"""
    
#     #sum the counts of each sample
#     dataframe['total'] = dataframe.sum(1)
#     #divide the column of interest by the total to find the proportion
#     if taxon_label in dataframe.columns:
#         dataframe[proportion_label] = dataframe[taxon_label] / dataframe['total']
#     else:
#         dataframe[proportion_label] = 0
#     proportions = dataframe.drop(dataframe.columns.difference([proportion_label]), 1, inplace=True)


#     return proportions

# def find_absolute(dataframe, taxon_label, count_label = 'total_' + taxon_label):
#     """calculate the per-sample count of a given taxon from a qiime2 taxa barplot (converted to pandas dataframe)
    
#     Parameters
#     -----------
#     dataframe : pandas DataFrame built from a qiime2 taxa barplot visualization
#     taxon_label : str, name of column of interest
#     count_label : str, name of results column (defaults to ('total_' + taxon_label))

#     Returns
#     -----------
#     counts : pandas DataFrame with the original index and a single column of counts of the taxon"""
    
#     if taxon_label in dataframe.columns:
#         dataframe[count_label] = dataframe[taxon_label]
#     else:
#         datafreme[count_label] = 0
#     counts = dataframe.drop(dataframe.columns.difference([proportion_label]), 1, inplace=True)


#     return counts



def load_tbp(fp, directory, level):
    """load a qiime2 taxa barplot qzv, export qzv into a directory, and load the specified CSV into a pandas dataframe. 
    Parameters
    ----------
    fp : path to qzv
    directory : path to directory to which the qzv will be exported
    level : int or str, taxonomic level to load into pandas
    
    Returns
    ----------
    qzv_df : pandas dataframe of specified taxonomic level"""

    qzv = Visualization.load(fp)
    qzv.export_data(directory)
    csv_name = 'level-' + str(level) + '.csv'
    qzv_df = pd.read_csv(os.path.join(directory, csv_name), index_col = 'index')


    return qzv_df

def main_function():
    """run script"""

    working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
    studies = ['song', 'GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'mocks', 'song', 'song_Amphibia', 'song_Arachnida', 'song_Aves', 'song_Hyperoartia', 'song_Insecta', 'song_Leptocardii', 'song_Mammalia', 'song_Reptilia', 'song_Sagittoidea']
    denoisers = ['dada2', 'deblur']
    filters = ['filtered', 'unfiltered']
    classifiers = ['nb', 'vsearch']
    references = ['silva', 'silva_extended', 'gg', 'gg_extended']

    with tempfile.TemporaryDirectory() as temp_dir:
        results = pd.DataFrame().rename_axis('#SampleID')
        for study in studies:
            study_results = pd.DataFrame().rename_axis('#SampleID')
            for denoiser in denoisers:
                denoiser_results = pd.DataFrame().rename_axis('#SampleID')
                for filtered in filters:
                    filter_results = pd.DataFrame().rename_axis('#SampleID')
                    for classifier in classifiers:
                        classifier_results = pd.DataFrame().rename_axis('#SampleID')
                        for reference in references:
                            fp = working_dir + '/output/' + study + '_' + denoiser + '_' + filtered + '_' + reference + '_' + classifier + '_tbp.qzv'
                            df = load_tbp(fp, temp_dir, 1)
                            unassigned_results = get_proportions_and_counts(df, 'Unassigned', 'unassigned')
                            #there are several differences between silva and greengenes - taxonomic level of chloroplasts (4 vs 3) and specific lineages of both chloroplasts and mitochondria
                            if 'silva' in reference:
                                df = load_tbp(fp, temp_dir, 4)
                                cp_name = 'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast'
                                mc_name = 'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria'
                            else:
                                df = load_tbp(fp, temp_dir, 3)
                                cp_name = 'k__Bacteria;p__Cyanobacteria;c__Chloroplast'
                                mc_name = 'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'
                            chloroplast_results = get_proportions_and_counts(df, cp_name, 'chloroplasts')
                            df = load_tbp(fp, temp_dir, 5)
                            mitochondria_results = get_proportions_and_counts(df, mc_name, 'mitochondria')
                            reference_results = unassigned_results.merge(chloroplast_results, left_index = True, right_index = True, validate = '1:1')
                            reference_results = reference_results.merge(mitochondria_results, left_index = True, right_index = True, validate = '1:1')
                            reference_results['reference taxonomy'] = reference
                            classifier_results = classifier_results.append(reference_results)
                        classifier_results['classification method'] = classifier
                        filter_results = filter_results.append(classifier_results)
                    filter_results['positive filter'] = filtered
                    denoiser_results = denoiser_results.append(filter_results)
                denoiser_results['denoise method'] = denoiser
                study_results = study_results.append(denoiser_results)
            study_results['study'] = study
            results = results.append(study_results)
        results.to_csv(working_dir + '/output/proportions.csv')



if __name__ == '__main__':
    main_function()
