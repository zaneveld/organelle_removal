#demultiplex qiita studies
#this script includes a time-intensive step (days) in order to reimport human_gut sequences from p64 to p33

from os.path import join
import tempfile

from qiime2 import Artifact, Metadata
from qiime2.plugins.demux.methods import emp_single

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
lanes = {'GCMP':2, 'GSMP':2, 'human_gut':14, 'milk':6, 'peru_ants':1, 'song':13}

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