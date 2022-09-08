from os.path import join

from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import filter_samples
from qiime2.metadata import Metadata

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
md = Metadata.load(join(working_dir, 'input', 'song', 'song_sample_metadata.txt'))

for denoiser in ['dada2_', 'deblur_']:
    for filtered in ['filtered', 'unfiltered']:
        ft = Artifact.load(join(working_dir, 'input', 'song_' + denoiser + filtered + '_merged_ft.qza'))
        for name in ['Amphibia', 'Arachnida', 'Aves', 'Hyperoartia', 'Insecta', 'Leptocardii', 'Mammalia', 'Reptilia', 'Sagittoidea']:#, 'unknown']:
            where = "class='" + name + "'"
            class_ft, = filter_samples(ft, metadata = md, where = where)
            class_ft.save(join(working_dir, 'input', 'song_' + name + '_' + denoiser + filtered + '_merged_ft.qza'))

