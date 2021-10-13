#!/bin/bash

#SBATCH --job-name=temp
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=zaneveld
#SBATCH --partition=compute-bigmem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=185G
#SBATCH --time=2-10

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=sbatch.log # where STDOUT goes
#SBATCH --error=sbatch.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
qiime cutadapt demux-single \
	--i-seqs input/human_gut/split_libraries/multiplexed_seqs.qza \
	--m-barcodes-file input/human_gut/split_libraries/hg_barcodes.txt \
	--m-barcodes-column barcode \
	--p-error-rate 0 \
	--o-per-sample-sequences input/human_gut/split_libraries/demuxed_seqs.qza \
	--o-untrimmed-sequences input/human_gut/split_libraries/untrimmed_seqs.qza \
	--verbose
