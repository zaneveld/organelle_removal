from os.path import join

from qiime2 import Artifact
from qiime2.plugins.feature_classifier.methods import classify_consensus_vsearch
from qiime2.plugins.feature_classifier.methods import classify_sklearn

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
references = ['silva', 'silva_extended', 'gg', 'gg_extended']
denoisers = ['dada2', 'deblur']
filters = ['filtered', 'unfiltered']
classifiers = ['vsearch', 'nb']
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song', 'mocks']

for study in studies:
    for denoiser in denoisers:
        for filter in filters:
            seqs = Artifact.load(join(working_dir, 'input', f'{study}_{denoiser}_{filter}_merged_seqs.qza'))
            for reference in references:
                ref_seqs = Artifact.load(join(working_dir, 'taxonomy_references', f'{reference}_sequences.qza'))
                ref_tax = Artifact.load(join(working_dir, 'taxonomy_references', f'{reference}_taxonomy.qza'))
                classification_taxonomy, = classify_consensus_vsearch(seqs, ref_seqs, ref_tax, threads = 30)
                classification_taxonomy.save(join(working_dir, 'output', f'{study}_{denoiser}_{filter}_{reference}_vsearch_classification_taxonomy.qza'))
                classifier = Artifact.load(join(working_dir, 'taxonomy_references', f'{reference}_nb_classifier.qza'))
                nb_classification_taxonomy, = classify_sklearn(seqs, classifier, n_jobs = 30)
                nb_classification_taxonomy.save(join(working_dir, 'output', f'{study}_{denoiser}_{filter}_{reference}_nb_classification_taxonomy.qza'))
