qiime tools import --type MultiplexedSingleEndBarcodeInSequence --input-path input/MWS/1/forward.fastq.gz --output-path input/MWS/1/multiplexed-seqs.qza

qiime cutadapt demux-single --i-seqs input/MWS/1/multiplexed-seqs.qza --m-barcodes-file input/MWS/1/metadata.tsv --m-barcodes-column BarcodeSequence --p-error-rate 0 --o-per-sample-sequences input/MWS/1/demultiplexed-seqs.qza --o-untrimmed-sequences input/MWS/1/untrimmed.qza

qiime cutadapt trim-single --i-demultiplexed-sequences input/MWS/1/demultiplexed-seqs.qza --p-cores 40 --p-adapter AGRGTTTGATCMTGGCTCAG --p-front GTNTTACNGCGGCKGCTG --p-error-rate 0 --o-trimmed-sequences input/MWS/1/trimmed-seqs.qza

qiime dada2 denoise-pyro --i-demultiplexed-seqs input/MWS/1/trimmed-seqs.qza --p-trunc-len 250 --p-n-threads 40 --o-table output/MWS_dada2_ft.qza --o-representative-sequences output/MWS_dada2_rep_seqs.qza --o-denoising-stats output/MWS_dada2_stats.qza


