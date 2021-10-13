import itertools
from qiime2 import Artifact

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for i in itertools.chain(range(1,7), range(11,17)):
    fp = working_dir + '/input/human_gut/' + str(i) + '/demuxed_' + str(i) + '_seqs.qza'
    p64_seqs = Artifact.load(fp)
    p64_seqs.export_data(working_dir + '/input/' + str(i) + '/exported_seqs')

