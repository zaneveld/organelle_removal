#!/bin/bash

#SBATCH --job-name=freqs
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=zaneveld
#SBATCH --partition=compute-bigmem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=364G
#SBATCH --time=2-08

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=log.log # where STDOUT goes
#SBATCH --error=err.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
python procedure/find_frequencies.py
