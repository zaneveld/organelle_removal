#dirty paralellization of human gut demux/denoising
#multiple weeks on hyak, due to conversion of human gut files to phred33
from os.path import join
import tempfile

from qiime2 import Artifact
from qiime2 import Metadata
from qiime2.plugins.demux.methods import emp_single
from qiime2.plugins.dada2.methods import denoise_single
from qiime2.plugins.deblur.methods import denoise_16S
from qiime2.plugins.feature_table.methods import merge, merge_seqs
from qiime2.plugins.quality_filter.methods import q_score

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

study = 'human_gut'
lane = 1 

seq_path = join(working_dir, 'input', study, study + '_' + str(lane) + '_sequences.qza')
seqs = Artifact.load(seq_path)
md_path = join(working_dir, 'input', study, str(lane) + '_barcodes.tsv')
metadata = Metadata.load(md_path)
barcodes = metadata.get_column('barcode')
demuxed_seqs, stats = emp_single(seqs, barcodes)
with tempfile.TemporaryDirectory() as temp_dir:
    demuxed_seqs.export_data(temp_dir)
    with open(join(temp_dir, 'MANIFEST')) as infile:
        with open(join(temp_dir, 'manifest.txt'), 'w') as outfile:
            outfile.write('sample-id,absolute-filepath,direction\n')
            for line in infile:
                if not line.startswith('sample-id') and not line.startswith('#'):
                    cells = line.split(',')
                    cells[1] = temp_dir + '/' + cells[1]
                    newline = ','.join(cells)
                    outfile.write(newline)
    demuxed_seqs = Artifact.import_data('SampleData[SequencesWithQuality]', temp_dir + '/manifest.txt', view_type = 'SingleEndFastqManifestPhred64')
demuxed_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demuxed_seqs.qza'))
stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demux_ecd.qza'))
d2_table, d2_rep_seqs, d2_stats, = denoise_single(demuxed_seqs, 100)
d2_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_stats.qza'))
d2_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_table.qza'))
d2_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_seqs.qza'))
qual_filtered_seqs, qual_filtered_stats, = q_score(demuxed_seqs)
qual_filtered_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_qual_filtered_stats.qza'))
deblur_table, deblur_rep_seqs, deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = True)
deblur_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_table.qza'))
deblur_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_seqs.qza'))
deblur_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_stats.qza'))
