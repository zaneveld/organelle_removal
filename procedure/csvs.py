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


def load_tbp(fp, level):
    """load a qiime2 taxa barplot qzv, then load the specified CSV into a pandas dataframe. 
    Parameters
    ----------
    fp : path to qzv
    directory : path to directory to which the qzv will be exported
    level : int or str, taxonomic level to load into pandas
    
    Returns
    ----------
    qzv_df : pandas dataframe of specified taxonomic level"""

    qzv = Visualization.load(fp)
    with tempfile.TemporaryDirectory() as temp_dir:
        qzv.export_data(temp_dir)
        csv_name = 'level-' + str(level) + '.csv'
        fp = join(temp_dir, csv_name)
        if exists(fp):
            qzv_df = pd.read_csv(fp, index_col = 'index')
        else:
            #qiime does not create a csv for that level if nothing was annotated at that point.
            #get around that by grabbing the index from the level 1 csv and returning nothing else
            qzv_df = pd.read_csv(join(temp_dir, 'level-1.csv'), index_col = 'index')
            qzv_df = qzv_df[[]]
        
    return qzv_df

def main_function():
    """run script"""

    working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
    studies = ['song', 'GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'mocks', 'song', 'song_Amphibia', 'song_Arachnida', 'song_Aves', 'song_Hyperoartia', 'song_Insecta', 'song_Leptocardii', 'song_Mammalia', 'song_Reptilia', 'song_Sagittoidea']
    denoisers = ['dada2', 'deblur']
    filters = ['filtered', 'unfiltered']
    classifiers = ['nb', 'vsearch']
    references = ['silva', 'silva_extended', 'gg', 'gg_extended']

    
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
                        df = load_tbp(fp, 1)
                        unassigned_results = get_proportions_and_counts(df, 'Unassigned', 'unassigned')
                        #there are several differences between silva and greengenes - taxonomic level of chloroplasts (4 vs 3) and specific lineages of both chloroplasts and mitochondria
                        if 'silva' in reference:
                            df = load_tbp(fp, 4)
                            cp_name = 'd__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast'
                            mc_name = 'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria'
                        else:
                            df = load_tbp(fp, 3)
                            cp_name = 'k__Bacteria;p__Cyanobacteria;c__Chloroplast'
                            mc_name = 'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'
                        chloroplast_results = get_proportions_and_counts(df, cp_name, 'chloroplasts')
                        df = load_tbp(fp, 5)
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
