from os.path import join

from qiime2.plugins.taxa.visualizers import barplot
from qiime2 import Artifact
from qiime2.metadata import Metadata

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
denoisers = ['dada2', 'deblur']
studies = ['mocks']#'GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song', 'song_Amphibia', 'song_Arachnida', 'song_Aves', 'song_Hyperoartia', 'song_Insecta', 'song_Lepidosauria', 'song_Leptocardii', 'song_Mamallia', 'song_Mammalia', 'song_Reptilia', 'song_Sagittoidea', 'mocks']
classifiers = ['nb', 'vsearch']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']


for study in studies:
    if 'song' in study:
        metadata = metadata.load(join(working_dir, 'input', 'song', 'sample_metadata.txt'))
    else:
        metadata = Metadata.load(join(working_dir, 'input', study, 'sample_metadata.txt'))
    df = metadata.to_dataframe()
    df = df.drop(df.columns.difference(['#SampleID']), 1)
    ids = Metadata(df)
    for denoiser in denoisers:
        ft = Artifact.load(working_dir + '/input/' + study + '_' + denoiser + '_merged_ft.qza')
        for classifier in classifiers:
            for reference in references:
                if 'song' in study:
                    taxonomy = Artifact.load(join(working_dir, 'output', 'song_' + denoiser + '_' + reference + '_' + classifier + '_classification_taxonomy.qza'))
                else:
                    taxonomy = Artifact.load(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_' + classifier + '_classification_taxonomy.qza')
                tbp, = barplot(ft, taxonomy, ids)
                tbp.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_' + classifier + '_tbp.qzv')

