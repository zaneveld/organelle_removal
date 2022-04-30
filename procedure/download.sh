#GCMP
mkdir input/GCMP
wget -O input/GCMP/31543.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=31543

#GSMP
mkdir input/GSMP
wget -O input/GSMP/2979.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=2979

#human_gut
mkdir input/human_gut
wget -O input/human_gut/2457.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=2457

#milk
mkdir input/milk
wget -O input/milk/3532.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3532
wget -O input/milk/3533.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3533
wget -O input/milk/3534.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3534
wget -O input/milk/3536.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3536
wget -O input/milk/3537.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3537
wget -O input/milk/3538.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3538

#ants
mkdir input/peru_ants
wget -O input/peru_ants/3198.zip https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3198

#unzip
unzip input/GCMP/\*.zip -d input/GCMP
unzip input/GSMP/\*.zip -d input/GSMP
unzip input/human_gut/\*.zip -d input/human_gut
unzip input/milk/\*.zip -d input/milk
unzip input/peru_ants/\*.zip -d input/peru_ants

#mkdirs
mkdir input/GCMP/L7
mkdir input/GCMP/L8
mkdir input/GSMP/L7
mkdir input/GSMP/L8
mkdir input/human_gut/1
mkdir input/human_gut/2
mkdir input/human_gut/3
mkdir input/human_gut/4
mkdir input/human_gut/5
mkdir input/human_gut/6
mkdir input/human_gut/7
mkdir input/human_gut/11
mkdir input/human_gut/12
mkdir input/human_gut/13
mkdir input/human_gut/14
mkdir input/human_gut/15
mkdir input/human_gut/16
mkdir input/human_gut/17
mkdir input/milk/1
mkdir input/milk/2
mkdir input/milk/3
mkdir input/milk/4
mkdir input/milk/5
mkdir input/milk/6
mkdir input/peru_ants/1

#move and rename
mv input/GCMP/FASTQ/31543/GCMP1_Lane7_S7_L007_I1_001.fastq.gz input/GCMP/L7/barcodes.fastq.gz
mv input/GCMP/FASTQ/31543/GCMP1_Lane7_S7_L007_R1_001.fastq.gz input/GCMP/L7/sequences.fastq.gz
mv input/GCMP/FASTQ/31543/GCMP2_Lane8_S8_L008_I1_001.fastq.gz input/GCMP/L8/barcodes.fastq.gz
mv input/GCMP/FASTQ/31543/GCMP2_Lane8_S8_L008_R1_001.fastq.gz input/GCMP/L8/sequences.fastq.gz

mv input/GSMP/raw_data/870_EMP_Thomas_sponges_16S_L007_barcodes.fastq.gz input/GSMP/L7/barcodes.fastq.gz
mv input/GSMP/raw_data/870_EMP_Thomas_sponges_16S_L007_sequences.fastq.gz input/GSMP/L7/sequences.fastq.gz
mv input/GSMP/raw_data/870_EMP_Thomas_sponges_16S_L008_barcodes.fastq.gz input/GSMP/L8/barcodes.fastq.gz
mv input/GSMP/raw_data/870_EMP_Thomas_sponges_16S_L008_sequences.fastq.gz input/GSMP/L8/sequences.fastq.gz

mv input/human_gut/raw_data/170_s_1_1_withindex_sequence_barcodes.fastq.gz input/human_gut/1/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_1_1_withindex_sequence.fastq.gz input/human_gut/1/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_2_1_withindex_sequence_barcodes.fastq.gz input/human_gut/2/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_2_1_withindex_sequence.fastq.gz input/human_gut/2/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_3_1_withindex_sequence_barcodes.fastq.gz input/human_gut/3/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_3_1_withindex_sequence.fastq.gz input/human_gut/3/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_4_1_withindex_sequence_barcodes.fastq.gz input/human_gut/4/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_4_1_withindex_sequence.fastq.gz input/human_gut/4/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_5_1_withindex_sequence_barcodes.fastq.gz input/human_gut/5/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_5_1_withindex_sequence.fastq.gz input/human_gut/5/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_6_1_withindex_sequence_barcodes.fastq.gz input/human_gut/6/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_6_1_withindex_sequence.fastq.gz input/human_gut/6/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_7_1_withindex_sequence_barcodes.fastq.gz input/human_gut/7/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_7_1_withindex_sequence.fastq.gz input/human_gut/7/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_11_1_withindex_sequence_barcodes.fastq.gz input/human_gut/11/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_11_1_withindex_sequence.fastq.gz input/human_gut/11/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_12_1_withindex_sequence_barcodes.fastq.gz input/human_gut/12/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_12_1_withindex_sequence.fastq.gz input/human_gut/12/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_13_1_withindex_sequence_barcodes.fastq.gz input/human_gut/13/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_13_1_withindex_sequence.fastq.gz input/human_gut/13/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_14_1_withindex_sequence_barcodes.fastq.gz input/human_gut/14/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_14_1_withindex_sequence.fastq.gz input/human_gut/14/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_15_1_withindex_sequence_barcodes.fastq.gz input/human_gut/15/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_15_1_withindex_sequence.fastq.gz input/human_gut/15/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_16_1_withindex_sequence_barcodes.fastq.gz input/human_gut/16/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_16_1_withindex_sequence.fastq.gz input/human_gut/16/sequences.fastq.gz
mv input/human_gut/raw_data/170_s_17_1_withindex_sequence_barcodes.fastq.gz input/human_gut/17/barcodes.fastq.gz
mv input/human_gut/raw_data/170_s_17_1_withindex_sequence.fastq.gz input/human_gut/17/sequences.fastq.gz

gzip input/milk/FASTQ/3532/1_barcodes.fastq
mv input/milk/FASTQ/3532/1_barcodes.fastq.gz input/milk/1/barcodes.fastq.gz
gzip input/milk/FASTQ/3532/1_reads.fastq
mv input/milk/FASTQ/3532/1_reads.fastq.gz input/milk/1/sequences.fastq.gz
gzip input/milk/FASTQ/3533/2_barcodes.fastq
mv input/milk/FASTQ/3533/2_barcodes.fastq.gz input/milk/2/barcodes.fastq.gz
gzip input/milk/FASTQ/3533/2_reads.fastq
mv input/milk/FASTQ/3533/2_reads.fastq.gz input/milk/2/sequences.fastq.gz
gzip input/milk/FASTQ/3534/3_barcodes.fastq
mv input/milk/FASTQ/3534/3_barcodes.fastq.gz input/milk/3/barcodes.fastq.gz
gzip input/milk/FASTQ/3534/3_reads.fastq
mv input/milk/FASTQ/3534/3_reads.fastq.gz input/milk/3/sequences.fastq.gz
gzip input/milk/FASTQ/3536/4_barcodes.fastq
mv input/milk/FASTQ/3536/4_barcodes.fastq.gz input/milk/4/barcodes.fastq.gz
gzip input/milk/FASTQ/3536/4_reads.fastq
mv input/milk/FASTQ/3536/4_reads.fastq.gz input/milk/4/sequences.fastq.gz
gzip input/milk/FASTQ/3537/5_barcodes.fastq
mv input/milk/FASTQ/3537/5_barcodes.fastq.gz input/milk/5/barcodes.fastq.gz
gzip input/milk/FASTQ/3537/5_reads.fastq
mv input/milk/FASTQ/3537/5_reads.fastq.gz input/milk/5/sequences.fastq.gz
gzip input/milk/FASTQ/3538/6_barcodes.fastq
mv input/milk/FASTQ/3538/6_barcodes.fastq.gz input/milk/6/barcodes.fastq.gz
gzip input/milk/FASTQ/3538/6_reads.fastq
mv input/milk/FASTQ/3538/6_reads.fastq.gz input/milk/6/sequences.fastq.gz

mv input/peru_ants/FASTQ/3198/Ants_Amnon_Lane1_S1_L001_I1_001.fastq.gz
mv input/peru_ants/FASTQ/3198/Ants_Amnon_Lane1_S1_L001_R1_001.fastq.gz


qiime tools import --type EMPSingleEndSequences --input-path input/GCMP/L7 --output-path input/GCMP/L7_seqs.qza
qiime tools import --type EMPSingleEndSequences --input-path input/GCMP/L8 --output-path input/GCMP/L8_seqs.qza

mv input/GSMP/870_EMP_Thomas_sponges_16S_L007_barcodes.fastq.gz input/GSMP/L7/barcodes.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L007_sequences.fastq.gz input/GSMP/L7/sequences.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L008_barcodes.fastq.gz input/GSMP/L8/barcodes.fastq.gz
mv input/GSMP/870_EMP_Thomas_sponges_16S_L008_sequences.fastq.gz input/GSMP/L8/sequences.fastq.gz
