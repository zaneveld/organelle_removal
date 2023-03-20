#import mock communities

from os.path import join
import tempfile

from qiime2 import Artifact

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

for mock in range(1, 11):
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(join(temp_dir, 'MANIFEST'), 'w') as file:
            file.write('sample-id,absolute-filepath,direction\nsample-' + str(mock) + ',/gscratch/zaneveld/sonettd/organelle_removal/input/mocks/' + str(mock) + '/1_1_L001_R1_001.fastq.gz,forward')
        qza = Artifact.import_data('SampleData[SequencesWithQuality]', join(temp_dir, 'MANIFEST'), 'SingleEndFastqManifestPhred33')
    qza.save(join(working_dir, 'input', 'mocks', 'mocks_' + str(mock) + '_demuxed_seqs.qza'))