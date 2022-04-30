from qiime2 import Artifact
import tempfile
from os.path import join
from random import shuffle

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

rep_seqs = Artifact.load(join(working_dir, 'input', 'GCMP_dada2_merged_seqs.qza'))
with tempfile.TemporaryDirectory() as temp_dir:
    rep_seqs.export_data(temp_dir)
    with open(join(temp_dir, 'dna-sequences.fasta')) as original_fasta:
        with open(join(temp_dir, 'shuffled.fasta'), 'w') as shuffled_fasta:
            for line in original_fasta:
                if line.startswith('>'):
                    shuffled_fasta.write(line)
                else:
                    bases = list(line.rstrip('\n'))
                    shuffle(bases)
                    shuffled_line = ''.join(bases)
                    shuffled_fasta.write(shuffled_line + '\n')
    shuffled_seqs = Artifact.import_data('FeatureData[Sequence]', join(temp_dir, 'shuffled.fasta'))
shuffled_seqs.save(join(working_dir, 'input', 'GCMP_shuffled_dada2_merged_seqs.qza'))
