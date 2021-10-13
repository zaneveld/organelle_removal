from qiime2 import Artifact
from qiime2.plugins.feature_classifier.methods import fit_classifier_naive_bayes
import os

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
refs_dir = working_dir + '/taxonomy_references'

for reference in ['silva_extended']:# ['gg', 'gg_extended', 'silva', 'silva_extended']:
    if not os.path.exists(working_dir + '/output/' + reference + '_nb_classifier.qza'):
        ref_reads = Artifact.load(refs_dir + '/' + reference + '_sequences.qza')
        ref_taxonomy = Artifact.load(refs_dir + '/' + reference + '_taxonomy.qza')
        classifier, = fit_classifier_naive_bayes(ref_reads, ref_taxonomy)
        classifier.save(working_dir + '/output/' + reference + '_nb_classifier.qza')
