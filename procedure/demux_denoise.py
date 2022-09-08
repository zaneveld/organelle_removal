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
lanes = {'song':13}#{'GCMP':2, 'GSMP':2, 'human_gut':14, 'milk':6, 'peru_ants':1, 'song':13, 'mocks':10}

#first we'll import the mock files. they are not multiplexed
#for mock in range(1, 11):
#    with tempfile.TemporaryDirectory() as temp_dir:
#        with open(join(temp_dir, 'MANIFEST'), 'w') as file:
#            file.write('sample-id,absolute-filepath,direction\nsample-' + str(mock) + ',/gscratch/zaneveld/sonettd/organelle_removal/input/mocks/' + str(mock) + '/1_1_L001_R1_001.fastq.gz,forward')
#        qza = Artifact.import_data('SampleData[SequencesWithQuality]', join(temp_dir, 'MANIFEST'), 'SingleEndFastqManifestPhred33')
#    qza.save(join(working_dir, 'input', 'mocks', 'mocks_' + str(mock) + '_demuxed_seqs.qza'))

for study, lane_count in lanes.items():
    d2_tables = []
    d2_seqs = []
    deblur_tables = []
    deblur_seqs = []
    for lane in range(1, 1 + lane_count):
        if study == 'mocks':
            demuxed_seqs = Artifact.load(join(working_dir, 'input', 'mocks', 'mocks_' + str(lane) + '_demuxed_seqs.qza'))
        else:
            seq_path = join(working_dir, 'input', study, study + '_' + str(lane) + '_sequences.qza')
            seqs = Artifact.load(seq_path)
            md_path = join(working_dir, 'input', study, str(lane) + '_barcodes.tsv')
            metadata = Metadata.load(md_path)
            barcodes = metadata.get_column('barcode')
            if study == 'GCMP' or study == 'GSMP' or study == 'peru_ants' or study == 'song':
                demuxed_seqs, stats = emp_single(seqs, barcodes, rev_comp_mapping_barcodes = True)
            elif study == 'milk':
                demuxed_seqs, stats = emp_single(seqs, barcodes, golay_error_correction = False)
            elif study == 'human_gut':
                #human gut files are phred64 encoded and must be reimported (probably should have just imported them to begin with)
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
            else:
                demuxed_seqs, stats = emp_single(seqs, barcodes)
            demuxed_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demuxed_seqs.qza'))
            stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demux_ecd.qza'))
        d2_table, d2_rep_seqs, d2_stats, = denoise_single(demuxed_seqs, 100, n_threads = 30)
        d2_tables.append(d2_table)
        d2_seqs.append(d2_rep_seqs)
        d2_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_stats.qza'))
        qual_filtered_seqs, qual_filtered_stats, = q_score(demuxed_seqs)
        qual_filtered_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_qual_filtered_stats.qza'))
        deblur_table, deblur_rep_seqs, deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = True, jobs_to_start = 30)
        deblur_tables.append(deblur_table)
        deblur_seqs.append(deblur_rep_seqs)
        deblur_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_table.qza'))
        deblur_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_seqs.qza'))
        deblur_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_stats.qza'))
    d2_merged_table, = merge(d2_tables, 'sum')
    d2_merged_table.save(join(working_dir, 'input', study + '_dada2_merged_ft.qza'))
    d2_merged_seqs, = merge_seqs(d2_seqs)
    d2_merged_seqs.save(join(working_dir, 'input', study + '_dada2_merged_seqs.qza'))
    deblur_merged_table, = merge(deblur_tables, 'sum')
    deblur_merged_table.save(join(working_dir, 'input', study + '_deblur_merged_ft.qza'))
    deblur_merged_seqs, = merge_seqs(deblur_seqs)
    deblur_merged_seqs.save(join(working_dir, 'input', study + '_deblur_merged_seqs.qza'))


