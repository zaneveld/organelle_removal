#!/bin/bash

#SBATCH --job-name=ant_demux
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=zaneveld
#SBATCH --partition=compute-bigmem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=48G
#SBATCH --time=1-0

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=sbatch.log # where STDOUT goes
#SBATCH --error=sbatch.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
 qiime demux emp-single --i-seqs input/peru_ants/peru_ants_1_sequences.qza --m-barcodes-file input/peru_ants/1_barcodes.tsv --m-barcodes-column barcode --p-rev-comp-mapping-barcodes --o-per-sample-sequences input/peru_ants/peru_ants_demuxed_seqs --o-error-correction-details input/peru_ants/demux_stats
