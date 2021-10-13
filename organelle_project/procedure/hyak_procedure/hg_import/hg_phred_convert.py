import glob
from qiime2 import Artifact
import tempfile

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for fp in glob.glob(working_dir + '/input/human_gut/*/demuxed_*_seqs.qza'):
    p64_seqs = Artifact.load(fp)
    with tempfile.TemporaryDirectory() as temp_dir:
        p64_seqs.export_data(temp_dir)
        with open(temp_dir + '/MANIFEST') as infile:
            with open(temp_dir + 'manifest.txt', 'w') as outfile:
                outfile.write('sample-id\tabsolute-filepath\tdirection\n')
                for line in infile:
                    if not line.startswith('sample-id') and not line.startswith('#'):
                        cells = line.split(',')
                        newline = '\t'.join(cells)
                        outfile.write(newline)
        p64_qza = Artifact.import_data('SampleData[SequencesWithQuality]', temp_dir + '/manifest.txt', view_type = 'SingleEndFastqManifestPhred64')
    p64_qza.save(fp + '.fixed')
