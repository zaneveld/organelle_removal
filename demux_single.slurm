#!/bin/bash

#SBATCH --job-name=m1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=uwb
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=30G
#SBATCH --time=8-0

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=sbatch.log # where STDOUT goes
#SBATCH --error=sbatch.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
qiime demux emp-single \
--i-seqs input/mocks/mock_6_sequences.qza \
--m-barcodes-file input/milk/6_barcodes.tsv \
--m-barcodes-column 'barcode' \
--o-per-sample-sequences input/milk/milk_6_demuxed_seqs.qza \
--o-error-correction-details NULL
