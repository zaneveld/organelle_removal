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
denoisers = ['shuffled_dada2']
classifiers = ['vsearch', 'nb']
studies = ['GCMP']#'song', 'GCMP', 'GSMP', 'peru_ants', 'human_gut', 'mocks']

for study in studies:
    for denoiser in denoisers:
#        ft = Artifact.load(working_dir + '/input/' + study + '_' + denoiser + '_merged_ft.qza')
        seqs = Artifact.load(working_dir + '/input/' + study + '_' + denoiser + '_merged_seqs.qza')
        for reference in references:
            ref_seqs = Artifact.load(refs_dir + '/' + reference + '_sequences.qza')
            ref_tax = Artifact.load(refs_dir + '/' + reference + '_taxonomy.qza')
            classification_taxonomy, = classify_consensus_vsearch(seqs, ref_seqs, ref_tax, threads = 10)
            classification_taxonomy.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_vsearch_classification_taxonomy.qza')
            classifier = Artifact.load(refs_dir + '/' + reference + '_nb_classifier.qza')
            nb_classification_taxonomy, = classify_sklearn(seqs, classifier, n_jobs = 15)
            nb_classification_taxonomy.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_nb_classification_taxonomy.qza')
