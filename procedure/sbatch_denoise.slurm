#!/bin/bash

#SBATCH --job-name=denoise_hg
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=zaneveld
#SBATCH --partition=compute-bigmem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --mem=364G
#SBATCH --time=1-23

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=sbatch.log # where STDOUT goes
#SBATCH --error=sbatch.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
python procedure/hg_denoise.py
