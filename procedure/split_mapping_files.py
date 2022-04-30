#separate barcodes
import pandas as pd
from shutil import copyfile

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

#GCMP
df = pd.read_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/mapping_files/31543_mapping_file.txt', sep = '\t')
for run in df['run_prefix'].unique():
    run_barcodes = df.loc[df['run_prefix'] == run]
    run_dir = 'L' + run[-1]
    run_barcodes.to_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/' + run_dir + '/barcodes.tsv', sep = '\t', index = False)

#GSMP
df = pd.read_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/mapping_files/2979_mapping_file.txt', sep = '\t')
for run in df['run_prefix'].unique():
    run_barcodes = df.loc[df['run_prefix'] == run]
    run_dir = 'L' + run[-1]
    run_barcodes.to_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/' + run_dir + '/barcodes.tsv', sep = '\t', index = False)

#human_gut
df = pd.read_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/mapping_files/2457_mapping_file.txt', sep = '\t')
for run in df['run_prefix'].unique():
    run_barcodes = df.loc[df['run_prefix'] == run]
    run_dir = run[0:4].rstrip('_').lstrip('s_')
    run_barcodes.to_csv('/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/' + run_dir + '/barcodes.tsv', sep = '\t', index = False)

#milk and peru_ants have a single lane per mapping file so do not need to be split
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3532_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/1/barcodes.tsv')
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3533_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/2/barcodes.tsv')
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3534_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/3/barcodes.tsv')
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3536_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/4/barcodes.tsv')
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3537_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/5/barcodes.tsv')
copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/milk/mapping_files/3538_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/milk/6/barcodes.tsv')

copyfile('/gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/mapping_files/3198_mapping_file.txt', '/gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/1/barcodes.tsv')

