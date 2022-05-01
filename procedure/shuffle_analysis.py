from os.path import join
from random import shuffle
import tempfile

import os
import tempfile

import pandas as pd

from qiime2 import Artifact, Visualization
from qiime2.metadata import Metadata
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch
from qiime2.plugins.feature_classifier.methods import classify_sklearn
from qiime2.plugins.taxa.visualizers import barplot

from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

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

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
studies = ['GCMP_', 'mocks_']
references = ['silva_', 'silva_extended_']
classifiers = ['nb', 'vsearch']

for study in studies:
    rep_seqs = Artifact.load(join(working_dir, 'input', study + 'dada2_unfiltered_merged_seqs.qza'))
    metadata = Metadata.load(join(working_dir, 'input', study.rstrip('_'), 'sample_metadata.txt'))
    df = metadata.to_dataframe()
    df = df.drop(df.columns.difference(['#SampleID']), 1)
    ids = Metadata(df)
    with tempfile.TemporaryDirectory() as temp_dir:
        rep_seqs.export_data(temp_dir)
        with open(join(temp_dir, 'dna-sequences.fasta')) as original_fasta:
            with open(join(temp_dir, 'shuffled.fasta'), 'w') as shuffled_fasta:
                for line in original_fasta:
                    if line.startswith('>'):
                        shuffled_fasta.write(line)
                    else:
                        bases = list(line.rstrip('\n'))
                        shuffle(bases)
                        shuffled_line = ''.join(bases)
                        shuffled_fasta.write(shuffled_line + '\n')
        shuffled_seqs = Artifact.import_data('FeatureData[Sequence]', join(temp_dir, 'shuffled.fasta'))
    #shuffled_seqs.save(join(working_dir, 'input', study + 'shuffled_dada2_unfiltered_merged_seqs.qza'))
    ft = Artifact.load(join(working_dir, 'input', study + 'dada2_unfiltered_merged_ft.qza'))
    for reference in references:
        ref_seqs = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'sequences.qza'))
        ref_tax = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'taxonomy.qza'))
        classification_taxonomy, = classify_consensus_vsearch(shuffled_seqs, ref_seqs, ref_tax, threads = 30)
        #classification_taxonomy.save(join(working_dir, 'output', study + 'shuffled_dada2_unfiltered_silva_vsearch_classification_taxonomy.qza'))
        classifier = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'nb_classifier.qza'))
        nb_classification_taxonomy, = classify_sklearn(shuffled_seqs, classifier, n_jobs = 30)
        #nb_classification_taxonomy.save(join(working_dir, 'output', study + 'shuffled_dada2_unfiltered_silva_nb_classification_taxonomy.qza'))
        tbp, = barplot(ft, classification_taxonomy, ids)
        tbp.save(join(working_dir, 'output', study + 'shuffled_dada2_unfiltered_silva_vsearch_tbp.qzv'))
        nb_tbp = barplot(ft, nb_classification_taxonomy, ids)
        nb_tbp.save(join(working_dir, 'output', study + 'shuffled_dada2_unfiltered_silva_nb_tbp.qzv'))

with tempfile.TemporaryDirectory() as temp_dir:
    results = pd.DataFrame().rename_axis('#SampleID')
    for study in ['GCMP', 'mocks']:
        study_results = pd.DataFrame().rename_axis('#SampleID')
        for classifier in classifiers:
            classifier_results = pd.DataFrame().rename_axis('#SampleID')
            for reference in references:
                fp = join(working_dir, study + '_shuffled_dada2_unfiltered_silva_' + classifier + '_tbp.qzv')
                df = load_tbp(fp, temp_dir, 1)
                unassigned_results = get_proportions_and_counts(df, 'Unassigned', 'unassigned')
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
            study_results = study_results.append(classifier_results)
        study_results['study'] = study
        results = results.append(study_results)
results.to_csv(join(working_dir, 'shuffled_proportions.csv'))
