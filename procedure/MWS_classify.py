import os
import pandas as pd
import seaborn as sns
import tempfile
from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch
from qiime2.plugins.feature_classifier.methods import classify_sklearn
from qiime2.plugins.taxa.visualizers import barplot
from qiime2 import Visualization
from scipy import stats

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
refs_dir = working_dir + '/taxonomy_references'
references = ['silva', 'silva_extended', 'gg', 'gg_extended']
denoisers = ['dada2']
studies = ['MWS']
classifiers = ['vsearch', 'nb']

for study in studies:
#    metadata = Metadata.load(working_dir + '/input/' + study + '/mapping_file.txt')
    for denoiser in denoisers:
#        ft = Artifact.load(working_dir + '/output/' + study + '_' + denoiser + '_merged_ft.qza')
        seqs = Artifact.load(working_dir + '/output/' + study + '_' + denoiser + '_rep_seqs.qza')
        for reference in references:
            if not os.path.exists(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_nb_classification_taxonomy.qza'):
                ref_seqs = Artifact.load(refs_dir + '/' + reference + '_sequences.qza')
                ref_tax = Artifact.load(refs_dir + '/' + reference + '_taxonomy.qza')
                classification_taxonomy, = classify_consensus_vsearch(seqs, ref_seqs, ref_tax, threads = 40)
                classification_taxonomy.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_vsearch_classification_taxonomy.qza')
                classifier = Artifact.load(working_dir + '/output/' + reference + '_nb_classifier.qza')
                nb_classification_taxonomy, = classify_sklearn(seqs, classifier, n_jobs = 40)
                nb_classification_taxonomy.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_nb_classification_taxonomy.qza')
