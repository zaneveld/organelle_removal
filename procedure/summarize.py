#find the frequencies of each feature, by study

from os.path import join

from qiime2 import Artifact
from qiime2.plugins.feature_table.visualizers import summarize

working_dir = '/mnt/c/Users/Dylan/Documents/zaneveld/2022_may_procedure'
studies = ['human_gut', 'milk', 'peru_ants', 'song']
denoisers = ['dada2', 'deblur']
filters = ['unfiltered', 'filtered']

for study in studies:
    for denoiser in denoisers:
        for filter_ in filters:
            prefix = f'{study}_{denoiser}_{filter_}_'
            hash_frequencies = {}
            ft = Artifact.load(join(working_dir, 'input',
                                    f'{prefix}merged_ft.qza'))
            summarized_ft, = summarize(ft)
            summarized_ft.save(join(working_dir, 'output',
                               f'{prefix}ft_summary.qzv'))
            summarized_ft = None