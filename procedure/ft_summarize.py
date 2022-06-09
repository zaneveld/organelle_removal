#find the frequencies of each feature, by study
#this takes a massive amount of memory, >300GB. 

from os.path import join

from qiime2 import Artifact
from qiime2.plugins.feature_table.visualizers import summarize

working_dir = join('gscratch', 'zaneveld', 'sonettd', 'organelle_removal')
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song']
denoisers = ['dada2', 'deblur']
filters = ['unfiltered', 'filtered']

for study in studies:
    for denoiser in denoiser:
        for filter_ in filters:
            prefix = f'{study}_{denoiser}_{filter_}_'
            ft = Artifact.load(join(working_dir, 'input',
                                    f'{prefix}merged_ft.qza'))
            summarized_ft, = summarize(ft)
            summarized_ft.save(join(working_dir, 'output',
                               f'{prefix}ft_summary.qzv'))