from qiime2 import Artifact
import os
import glob

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for barcode_path in glob.glob(working_dir + '/input/**/barcodes.fastq.gz', recursive = True):
    directory_path = os.path.dirname(barcode_path)
    directory = os.path.basename(directory_path)
    if not os.path.exists(directory_path + '/' + directory + '_seqs.qza'):
        qza = Artifact.import_data('EMPSingleEndSequences', directory_path)
        qza.save(directory_path + '/' + directory + '_seqs.qza')
