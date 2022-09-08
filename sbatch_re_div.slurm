#!/bin/bash

#SBATCH --job-name=diversity
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=bbiosci
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=175G
#SBATCH --time=4-0

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=log.log # where STDOUT goes
#SBATCH --error=err.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
python procedure/reanalyze_div.py
