from os.path import join, sep

from qiime2 import Artifact, Metadata
from qiime2.plugins.composition.methods import ancombc

working_dir = join(sep, 'gscratch', 'zaneveld', 'sonettd', 'organelle_removal')
studies = ['GCMP']
denoisers = ['dada2', 'deblur']
filters = ['filtered', 'unfiltered']
classifiers = ['vsearch', 'nb']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']
columns_of_interest = {'GCMP':['tissue_compartment', 'family']}

for study in studies:
    md_path = join(working_dir, 'input', f'{study}_ancombc_metadata.tsv')
    md = Metadata.load(md_path)
    for denoiser in denoisers:
        for filter_ in filters:
            for classifier in classifiers:
                for reference in references:
                    filtered_table = Artifact.load(join(working_dir, 'output', f'{study}_{denoiser}_{filter_}_{reference}_{classifier}_cleaned_filtered_table.qza'))
                    ancom_formula = ' + '.join(columns_of_interest[study])
                    differentials, = ancombc(filtered_table, md, ancom_formula)
                    differentials.save(join(working_dir, 'output', f'{study}_{denoiser}_{filter_}_{reference}_{classifier}_ancombc_differentials.qza'))
