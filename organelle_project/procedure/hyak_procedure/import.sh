wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=31543'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP1_Lane7_S7_L007_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/1/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP1_Lane7_S7_L007_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/1/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP2_Lane8_S8_L008_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/2/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP2_Lane8_S8_L008_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/2/barcodes.fastq.gz

rm /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/*qiita*

rm /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/*fastq*

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/1/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP_1_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/2/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP/GCMP_2_sequences

#GSMP
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/1
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/2

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/GSMP_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=2979'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/GSMP_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/870_EMP_Thomas_sponges_16S_L007_sequences.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/1/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/870_EMP_Thomas_sponges_16S_L007_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/1/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/870_EMP_Thomas_sponges_16S_L008_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/2/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/870_EMP_Thomas_sponges_16S_L008_sequences.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/2/sequences.fastq.gz

rm /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/*qiita*

rm /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/*fastq*

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/1 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/GSMP_1_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/2 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP/GSMP_2_sequences

#human gut
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/1
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/2
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/3
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/4
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/5
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/6
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/7
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/8
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/9
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/10
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/11
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/12
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/13
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/14

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=2457'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_1_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/1/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_1_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/1/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_2_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/2/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_2_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/2/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_3_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/3/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_3_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/3/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_4_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/4/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_4_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/4/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_5_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/5/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_5_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/5/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_6_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/6/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_6_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/6/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_7_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/7/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_7_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/7/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_11_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/8/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_11_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/8/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_12_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/9/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_12_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/9/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_13_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/10/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_13_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/10/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_14_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/11/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_14_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/11/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_15_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/12/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_15_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/12/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_16_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/13/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_16_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/13/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_17_1_withindex_sequence.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/14/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/170_s_17_1_withindex_sequence_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/14/barcodes.fastq.gz

rm /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/*qiita*

rm /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/*fastq*

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/1/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_1_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/2/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_2_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/3/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_3_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/4/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_4_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/5/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_5_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/6/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_6_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/7/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_7_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/8/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_8_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/9/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_9_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/10/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_10_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/11/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_11_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/12/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_12_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/13/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_13_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/14/ \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/human_gut_14_sequences

#milk
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_1_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3532'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_1_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/1/barcodes.fastq
mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/1/sequences.fastq
gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1/barcodes.fastq
gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1/sequences.fastq

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_2_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3533'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_2_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/2/barcodes.fastq

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/2/sequences.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2/barcodes.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2/sequences.fastq

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_3_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3534'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_3_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/3/barcodes.fastq

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/3/sequences.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3/barcodes.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3/sequences.fastq

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_4_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3536'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_4_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/4/barcodes.fastq

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/4/sequences.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4/barcodes.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4/sequences.fastq

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_5_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3537'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_5_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/5/barcodes.fastq

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/5/sequences.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5/barcodes.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5/sequences.fastq

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_6_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3538'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_6_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/milk'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6_barcodes.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/6/barcodes.fastq

mv /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6_reads.fastq \
/gscratch/zaneveld/sonettd/organelle_removal/input/milk/6/sequences.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6/barcodes.fastq

gzip /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6/sequences.fastq

rm /gscratch/zaneveld/sonettd/organelle_removal/input/milk/*qiita*
rm /gscratch/zaneveld/sonettd/organelle_removal/input/milk/*fastq*

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/1 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_1_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/2 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_2_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/3 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_3_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/4 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_4_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/5 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_5_sequences

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/6 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/milk/milk_6_sequences

#peru_ants
#mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/1
wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/peru_ants_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=3198'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/peru_ants_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/Ants_Amnon_Lane1_S1_L001_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/1/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/Ants_Amnon_Lane1_S1_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/1/sequences.fastq.gz

rm /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/*qiita*

rm /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/*fastq*

qiime tools import \
--type EMPSingleEndSequences \
--input-path /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/1 \
--output-path /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants/peru_ants_1_sequences

#song
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/1
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/2
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/3
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/4
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/5
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/6
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/7
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/8
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/9
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/10
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/11
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/12
# mkdir /gscratch/zaneveld/sonettd/organelle_removal/input/song/13

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_1_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=54385'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_1_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Undetermined_S0_L001_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/1/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Undetermined_S0_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/1/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_2_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=54434'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_2_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Metcalf_16sV4_DecompMaterialV4_71712_NoIndex_L007_R2_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/2/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Metcalf_16sV4_DecompMaterialV4_71712_NoIndex_L007_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/2/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_3_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=54503'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_3_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2082_NoIndex_L002_R2_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/3/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2082_NoIndex_L002_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/3/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_4_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=54504'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_4_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2082_NoIndex_L001_R2_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/4/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2082_NoIndex_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/4/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2083_NoIndex_L001_R2_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/5/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2083_NoIndex_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/5/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2081_NoIndex_L002_R2_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/6/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/2013-2081_NoIndex_L002_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/6/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_5_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=54587'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_5_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Delsuc16SV4_EMP_Noindex_L001_R1_001_sequences_barcodes.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/7/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/Delsuc16SV4_EMP_Noindex_L001_R1_001_sequences.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/7/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_6_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=55205'

7z e /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_6_qiita.zip \
'-o/gscratch/zaneveld/sonettd/organelle_removal/input/song'

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/NZdata_Templeton_S0_L001_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/8/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/NZdata_Templeton_S0_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/8/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/SeJin_Templeton_Lane1_S1_L001_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/9/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/SeJin_Templeton_Lane1_S1_L001_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/9/sequences.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/SeJin_Templeton_Lane2_S2_L002_I1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/10/barcodes.fastq.gz

mv /gscratch/zaneveld/sonettd/organelle_removal/input/song/SeJin_Templeton_Lane2_S2_L002_R1_001.fastq.gz \
/gscratch/zaneveld/sonettd/organelle_removal/input/song/10/sequences.fastq.gz

wget -O /gscratch/zaneveld/sonettd/organelle_removal/input/song/song_7_qiita.zip \
'https://qiita.ucsd.edu/public_artifact_download/?artifact_id=56221'

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
