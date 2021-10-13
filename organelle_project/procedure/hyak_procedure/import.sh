#mkdir input/GCMP/L007
#mkdir input/GCMP/L008
#mv input/GCMP/GCMP1_Lane7_S7_L007_I1_001.fastq.gz input/GCMP/L007/barcodes.fastq.gz
#mv input/GCMP/GCMP1_Lane7_S7_L007_R1_001.fastq.gz input/GCMP/L007/sequences.fastq.gz
#mv input/GCMP/GCMP2_Lane8_S8_L008_I1_001.fastq.gz input/GCMP/L008/barcodes.fastq.gz
#mv input/GCMP/GCMP2_Lane8_S8_L008_R1_001.fastq.gz input/GCMP/L008/sequences.fastq.gz
#qiime tools import --type EMPSingleEndSequences --input-path input/GCMP/L007 --output-path input/GCMP/L007_seqs.qza
qiime tools import --type EMPSingleEndSequences --input-path input/GCMP/L008 --output-path input/GCMP/L008_seqs.qza

mkdir input/GSMP/L007
mkdir input/GSMP/L008
mv input/GSMP/870_EMP_Thomas_sponges_16S_L007_barcodes.fastq.gz input/GSMP/L007/barcodes.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L007_sequences.fastq.gz input/GSMP/L007/sequences.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L008_barcodes.fastq.gz input/GSMP/L008/barcodes.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L008_sequences.fastq.gz input/GSMP/L008/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/GSMP/L007 --output-path input/GSMP/L007_seqs.qza
qiime tools import --type EMPSingleEndSequences --input-path input/GSMP/L008 --output-path input/GSMP/L008_seqs.qza

mkdir input/human_gut/170_s_11_1
mv input/human_gut/170_s_11_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_11_1/barcodes.fastq.gz
mv input/human_gut/170_s_11_1_withindex_sequence.fastq.gz input/human_gut/170_s_11_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_11_1 --output-path input/human_gut/170_s_11_1_seqs.qza

mkdir input/human_gut/170_s_12_1
mv input/human_gut/170_s_12_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_12_1/barcodes.fastq.gz
mv input/human_gut/170_s_12_1_withindex_sequence.fastq.gz input/human_gut/170_s_12_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_12_1 --output-path input/human_gut/170_s_12_1_seqs.qza

mkdir input/human_gut/170_s_13_1
mv input/human_gut/170_s_13_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_13_1/barcodes.fastq.gz
mv input/human_gut/170_s_13_1_withindex_sequence.fastq.gz input/human_gut/170_s_13_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_13_1 --output-path input/human_gut/170_s_13_1_seqs.qza

mkdir input/human_gut/170_s_14_1
mv input/human_gut/170_s_14_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_14_1/barcodes.fastq.gz
mv input/human_gut/170_s_14_1_withindex_sequence.fastq.gz input/human_gut/170_s_14_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_14_1 --output-path input/human_gut/170_s_14_1_seqs.qza

mkdir input/human_gut/170_s_15_1
mv input/human_gut/170_s_15_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_15_1/barcodes.fastq.gz
mv input/human_gut/170_s_15_1_withindex_sequence.fastq.gz input/human_gut/170_s_15_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_15_1 --output-path input/human_gut/170_s_15_1_seqs.qza

mkdir input/human_gut/170_s_16_1
mv input/human_gut/170_s_16_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_16_1/barcodes.fastq.gz
mv input/human_gut/170_s_16_1_withindex_sequence.fastq.gz input/human_gut/170_s_16_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_16_1 --output-path input/human_gut/170_s_16_1_seqs.qza

mkdir input/human_gut/170_s_17_1
mv input/human_gut/170_s_17_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_17_1/barcodes.fastq.gz
mv input/human_gut/170_s_17_1_withindex_sequence.fastq.gz input/human_gut/170_s_17_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_17_1 --output-path input/human_gut/170_s_17_1_seqs.qza

mkdir input/human_gut/170_s_1_1
mv input/human_gut/170_s_1_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_1_1/barcodes.fastq.gz
mv input/human_gut/170_s_1_1_withindex_sequence.fastq.gz input/human_gut/170_s_1_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_1_1 --output-path input/human_gut/170_s_1_1_seqs.qza

mkdir input/human_gut/170_s_2_1
mv input/human_gut/170_s_2_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_2_1/barcodes.fastq.gz
mv input/human_gut/170_s_2_1_withindex_sequence.fastq.gz input/human_gut/170_s_2_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_2_1 --output-path input/human_gut/170_s_2_1_seqs.qza

mkdir input/human_gut/170_s_3_1
mv input/human_gut/170_s_3_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_3_1/barcodes.fastq.gz
mv input/human_gut/170_s_3_1_withindex_sequence.fastq.gz input/human_gut/170_s_3_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_3_1 --output-path input/human_gut/170_s_3_1_seqs.qza

mkdir input/human_gut/170_s_4_1
mv input/human_gut/170_s_4_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_4_1/barcodes.fastq.gz
mv input/human_gut/170_s_4_1_withindex_sequence.fastq.gz input/human_gut/170_s_4_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_4_1 --output-path input/human_gut/170_s_4_1_seqs.qza

mkdir input/human_gut/170_s_5_1
mv input/human_gut/170_s_5_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_5_1/barcodes.fastq.gz
mv input/human_gut/170_s_5_1_withindex_sequence.fastq.gz input/human_gut/170_s_5_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_5_1 --output-path input/human_gut/170_s_5_1_seqs.qza

mkdir input/human_gut/170_s_6_1
mv input/human_gut/170_s_6_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_6_1/barcodes.fastq.gz
mv input/human_gut/170_s_6_1_withindex_sequence.fastq.gz input/human_gut/170_s_6_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_6_1 --output-path input/human_gut/170_s_6_1_seqs.qza

mkdir input/human_gut/170_s_7_1
mv input/human_gut/170_s_7_1_withindex_sequence_barcodes.fastq.gz input/human_gut/170_s_7_1/barcodes.fastq.gz
mv input/human_gut/170_s_7_1_withindex_sequence.fastq.gz input/human_gut/170_s_7_1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/human_gut/170_s_7_1 --output-path input/human_gut/170_s_7_1_seqs.qza

mkdir input/milk/1
gzip input/milk/1_barcodes.fastq
mv input/milk/1_barcodes.fastq.gz input/milk/1/barcodes.fastq.gz
gzip input/milk/1_reads.fastq
mv input/milk/1_reads.fastq.gz input/milk/1/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/1 --output-path input/milk/1_seqs.qza

mkdir input/milk/2
gzip input/milk/2_barcodes.fastq
mv input/milk/2_barcodes.fastq.gz input/milk/2/barcodes.fastq.gz
gzip input/milk/2_reads.fastq
mv input/milk/2_reads.fastq.gz input/milk/2/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/2 --output-path input/milk/2_seqs.qza

mkdir input/milk/3
gzip input/milk/3_barcodes.fastq
mv input/milk/3_barcodes.fastq.gz input/milk/3/barcodes.fastq.gz
gzip input/milk/3_reads.fastq
mv input/milk/3_reads.fastq.gz input/milk/3/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/3 --output-path input/milk/3_seqs.qza

mkdir input/milk/4
gzip input/milk/4_barcodes.fastq
mv input/milk/4_barcodes.fastq.gz input/milk/4/barcodes.fastq.gz
gzip input/milk/4_reads.fastq
mv input/milk/4_reads.fastq.gz input/milk/4/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/4 --output-path input/milk/4_seqs.qza

mkdir input/milk/5
gzip input/milk/5_barcodes.fastq
mv input/milk/5_barcodes.fastq.gz input/milk/5/barcodes.fastq.gz
gzip input/milk/5_reads.fastq
mv input/milk/5_reads.fastq.gz input/milk/5/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/5 --output-path input/milk/5_seqs.qza

mkdir input/milk/6
gzip input/milk/6_barcodes.fastq
mv input/milk/6_barcodes.fastq.gz input/milk/6/barcodes.fastq.gz
gzip input/milk/6_reads.fastq
mv input/milk/6_reads.fastq.gz input/milk/6/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/milk/6 --output-path input/milk/6_seqs.qza

mkdir input/peru_ants/fastqs
mv input/peru_ants/Ants_Amnon_Lane1_S1_L001_I1_001.fastq.gz input/peru_ants/fastqs/barcodes.fastq.gz
mv input/peru_ants/Ants_Amnon_Lane1_S1_L001_R1_001.fastq.gz input/peru_ants/fastqs/sequences.fastq.gz
qiime tools import --type EMPSingleEndSequences --input-path input/peru_ants/fastqs --output-path input/peru_ants/seqs.qza
