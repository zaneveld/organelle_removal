import os
import pandas as pd
import seaborn as sns
import tempfile
from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch
from qiime2.plugins.taxa.visualizers import barplot
from qiime2 import Visualization
from scipy import stats


working_dir = os.path.abspath('/gscratch/zaneveld/sonettd/organelle_removal')
refs_dir = working_dir + '/taxonomy_references'
#metadata = Metadata.load(working_dir + '/input/qiime2/barcode_file.tsv')
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']
methods = ['dada2', 'deblur']
denoisers = ['dada2', 'deblur']
classifiers = ['vsearch', 'nb']

statistics = []
stats_df = pd.DataFrame(columns = ['denoiser', 'classifier', 'level', 'base reference', 'extended/base counts', 'H', 'p', 'study'])
for study in studies:
    df = pd.read_csv((working_dir + '/output/' + study + '_proportions.csv'), index_col = 0)
    for denoiser in denoisers:
        for level in ['unassigned', 'chloroplasts', 'mitochondria']:
            for classifier in classifiers:
                for base_reference in ['silva', 'gg']:
                    base_absolute = sum(df['absolute ' + level][(df['reference taxonomy'] == base_reference) & (df['denoise method'] == denoiser)])
                    extended_absolute = sum(df['absolute ' + level][(df['reference taxonomy'] == (base_reference + '_extended')) & (df['denoise method'] == denoiser)])
                    if not base_absolute == 0:
                        fold_delta = extended_absolute / base_absolute
                    else:
                        folde_delta = 'NaN'
                    base_proportion = df['proportion ' + level][(df['reference taxonomy'] == base_reference) & (df['denoise method'] == denoiser)]
                    extended_proportion = df['proportion ' + level][(df['denoise method'] == denoiser) & (df['reference taxonomy'] == (base_reference + '_extended'))]
                    try:
                        H, p = stats.kruskal(base_proportion, extended_proportion)
                    except ValueError:
                        H, p = 'NaN', 'NaN'
                    statistics.append((denoiser, classifier, level, base_reference, fold_delta, H, p))
    study_df = pd.DataFrame(statistics, columns = ['denoiser', 'classifier', 'level', 'base reference', 'extended/base counts', 'H', 'p'])
    study_df['study'] = study
    stats_df = stats_df.append(study_df)
stats_df.to_csv(working_dir + '/output/stats.csv', index = False)
