from os.path import join

from qiime2.plugins.taxa.visualizers import barplot
from qiime2 import Artifact
from qiime2.metadata import Metadata

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
denoisers = ['dada2', 'deblur']
filters = ['unfiltered', 'filtered']
studies = ['song_Amphibia', 'song_Arachnida', 'song_Aves', 'song_Hyperoartia', 'song_Insecta', 'song_Leptocardii', 'song_Mammalia', 'song_Reptilia', 'song_Sagittoidea']#['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song', 'song_Amphibia', 'song_Arachnida', 'song_Aves', 'song_Hyperoartia', 'song_Insecta', 'song_Leptocardii', 'song_Mammalia', 'song_Reptilia', 'song_Sagittoidea', 'mocks']
classifiers = ['nb', 'vsearch']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']


for study in studies:
    if 'song' in study:
        Metadata = metadata.load(join(working_dir, 'input', 'song', 'sample_metadata.txt'))
    else:
        metadata = Metadata.load(join(working_dir, 'input', study, 'sample_metadata.txt'))
    df = metadata.to_dataframe()
    df = df.drop(df.columns.difference(['#SampleID']), 1)
    ids = Metadata(df)
    for denoiser in denoisers:
        for filtered in filters:
            ft = Artifact.load(join(working_dir, 'input', f'{study}_{denoiser}_{filtered}_merged_ft.qza'))
            for classifier in classifiers:
                for reference in references:
                    if 'song' in study:
                        taxonomy = Artifact.load(join(working_dir, 'output', f'song_{denoiser}_{filtered}_{reference}_{classifier}_classification_taxonomy.qza'))
                    else:
                        taxonomy = Artifact.load(join(working_dir, 'output', f'{study}_{denoiser}_{filtered}_{reference}_{classifier}_classification_taxonomy.qza'))
                    tbp, = barplot(ft, taxonomy, ids)
                    tbp.save(join(working_dir, 'output', f'{study}_{denoiser}_{filtered}_{reference}_{classifier}_tbp.qzv'))

