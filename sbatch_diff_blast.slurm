#!/bin/bash

#SBATCH --job-name=BLAST2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sonettd@uw.edu

#SBATCH --account=bbiosci
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=175G
#SBATCH --time=2-08

#SBATCH --chdir=/gscratch/zaneveld/sonettd/organelle_removal
#SBATCH --export=NONE
#SBATCH --output=log.log# where STDOUT goes
#SBATCH --error=err.err # where STDERR goes

# Modules to use (optional).
#eval "$(conda shell.bash hook)"
#conda activate qiime2-2021.4

# Your programs to run.
/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn \
-db nt \
-query output/GCMP_differential_annotations.fasta \
#-num_threads 10 \
-max_target_seqs 5 \
#-max_hsps 1 \
-outfmt '6 qseqid sseqid staxids stitle evalue bitscore' \
-out output/GCMP_differential_seqs_blasted2.tsv

#/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn -db nt -query output/GSMP_differential_annotations.fasta -num_threads 10 -max_target_seqs 5 -max_hsps 1 -outfmt '6 qseqid sseqid staxids stitle evalue bitscore' -out output/GSMP_differential_seqs_blasted.tsv

#/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn -db nt -query output/human_gut_differential_annotations.fasta -num_threads 10 -max_target_seqs 5 -max_hsps 1 -outfmt '6 qseqid sseqid staxids stitle evalue bitscore' -out output/human_gut_differential_seqs_blasted.tsv

#/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn -db nt -query output/milk_differential_annotations.fasta -num_threads 10 -max_target_seqs 5 -max_hsps 1 -outfmt '6 qseqid sseqid staxids stitle evalue bitscore' -out output/milk_differential_seqs_blasted.tsv

#/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn -db nt -query output/peru_ants_differential_annotations.fasta -num_threads 10 -max_target_seqs 5 -max_hsps 1 -outfmt '6 qseqid sseqid staxids stitle evalue bitscore' -out output/peru_ants_differential_seqs_blasted.tsv

#/gscratch/zaneveld/BLAST/ncbi-blast-2.13.0+/bin/blastn -db nt -query output/song_differential_annotations.fasta -num_threads 10 -max_target_seqs 5 -max_hsps 1 -outfmt '6 qseqid sseqid staxids stitle evalue bitscore' -out output/song_differential_seqs_blasted.tsv

