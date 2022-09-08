import glob
import gzip
import shutil
import tempfile
from os.path import join
from os import system
from Bio import SeqIO

from qiime2 import Artifact

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
lanes = {'milk':6}#'GCMP':2, 'GSMP':2, 'human_gut':14, 'milk':6, 'peru_ants':1, 'song':13, 'mocks':10}

for study, lane_count in lanes.items():
    for lane in range(1, 1 + lane_count):
        demuxed_qza = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_demuxed_seqs.qza'))
        with tempfile.TemporaryDirectory() as temp_dir:
            demuxed_qza.export_data(temp_dir)
            for fp in glob.glob(join(temp_dir, '*.fastq.gz')):
                with gzip.open(fp, 'rb') as gz:
                    with open(fp.rstrip('.gz'), 'wb') as fastq:
                        shutil.copyfileobj(gz, fastq)
            system('cat ' + join(temp_dir, '*fastq') + ' > ' + join(temp_dir, 'LANE_FASTQS.fastq'))
            SeqIO.convert(join(temp_dir, 'LANE_FASTQS.fastq'), 'fastq', join(temp_dir, 'LANE.fasta'), 'fasta')
            with open(join(temp_dir, 'LANE.fasta')) as infile:
                with open(join(temp_dir, 'LANE_FIXED.fasta'), 'w') as outfile:
                    for i, line in enumerate(infile):
                        if line.startswith('>'):
                            outfile.write('>' + str(i) + '\n')
                        else:
                            outfile.write(line)
            lane_seqs = Artifact.import_data('FeatureData[Sequence]', join(temp_dir, 'LANE_FIXED.fasta'))
        lane_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_fasta_seqs.qza'))
