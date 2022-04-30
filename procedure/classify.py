from os.path import join

from qiime2 import Artifact
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch
from qiime2.plugins.feature_classifier.methods import classify_sklearn

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
references = ['silva_', 'silva_extended_', 'gg_', 'gg_extended_']
denoisers = ['dada2_', 'deblur_']
filters = ['filtered_', 'unfiltered_']
classifiers = ['vsearch', 'nb']
studies = ['GCMP_', 'GSMP_', 'human_gut_', 'milk_', 'peru_ants_', 'song_', 'mocks_']

for study in studies:
    for denoiser in denoisers:
        for filter in filters:
            ft = Artifact.load(join(working_dir, 'input', study + denoiser + filter + 'merged_ft.qza'))
            seqs = Artifact.load(join(working_dir, 'input', study + denoiser + filter + 'merged_seqs.qza'))
            for reference in references:
                ref_seqs = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'sequences.qza'))
                ref_tax = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'taxonomy.qza'))
                classification_taxonomy, = classify_consensus_vsearch(seqs, ref_seqs, ref_tax, threads = 30)
                classification_taxonomy.save(join(working_dir, 'output', study + denoiser + filter + reference + 'vsearch_classification_taxonomy.qza'))
                classifier = Artifact.load(join(working_dir, 'taxonomy_references', reference + 'nb_classifier.qza'))
                nb_classification_taxonomy, = classify_sklearn(seqs, classifier, n_jobs = 30)
                nb_classification_taxonomy.save(join(working_dir, 'output', study + denoiser + filter + reference + 'nb_classification_taxonomy.qza')
