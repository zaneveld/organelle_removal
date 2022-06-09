#!/bin/bash

#SBATCH --job-name=import
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=zaneveld
#SBATCH --partition=compute-bigmem
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=30
#SBATCH --mem=364G
#SBATCH --time=10-0

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=import.log # where STDOUT goes
#SBATCH --error=import.err # where STDERR goes

# Modules to use (optional).
eval "$(conda shell.bash hook)"
conda activate qiime2-2021.4

# Your programs to run.
#GCMP
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/1
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/2

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_7_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Gilbert_7_25_17_HB1_NoIndex_L001_I1_001.fastq  \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/11/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Gilbert_7_25_17_HB1_NoIndex_L001_R1_001.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/11/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Gilbert_7_25_17_HB2_NoIndex_L002_I1_001.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/12/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Gilbert_7_25_17_HB2_NoIndex_L002_R1_001.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/12/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_8_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=82947'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_8_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Undetermined_S0_L001_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/13/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Undetermined_S0_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/13/sequences.fastq.gz

rm /gscratch/zaneveld/sonettd/organelle_removal/input/song/*qiita*

rm /gscratch/zaneveld/sonettd/organelle_removal/input/song/*fastq*

#mocks
#we'll download them here but I find the import process a little easier in python so we'll do it there

#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/1
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/2
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/3
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/4
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/5
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/6
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/7
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/8
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/9
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/10

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/1/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-12/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/2/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-13/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/3/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-14/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/4/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-15/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/5/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-16/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/6/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-18/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/7/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-19/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/8/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-20/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/9/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-21/mock-forward-read.fastq.gz'

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/mocks/10/1_1_L001_R1_001.fastq.gz \
'https://s3-us-west-2.amazonaws.com/mockrobiota/latest/mock-22/mock-forward-read.fastq.gz'

