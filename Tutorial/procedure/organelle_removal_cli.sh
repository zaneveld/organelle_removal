#assume all files are present and named correctly

#generate taxonomic annotations with the base and extended silva references

#base silva 138 annotation
qiime feature-classifier classify-consensus-vsearch \
--i-query input/rep_seqs_merged.qza \
--i-reference-reads input/taxonomy_references/silva_sequences.qza \
--i-reference-taxonomy input/taxonomy_reference/silva_taxonomy.qza \
--p-threads 1 \
--o-classification output/silva_classification_taxonomy.qza

#extended silva 138 annotation
qiime feature-classifier classify-consensus-vsearch \
--i-query input/rep_seqs_merged.qza \
--i-reference-reads input/taxonomy_references/silva_extended_sequences.qza \
--i-reference-taxonomy input/taxonomy_reference/silva_extended_taxonomy.qza \
--p-threads 1 \
--o-classification output/silva_extended_classification_taxonomy.qza

#filter the feature table to only include samples in the metadata
qiime feature-table filter-samples \
--i-table input/feature_table_live_vs_dead.qza \
--m-metadata input/sample_metadata_live_vs_dead_combo.tsv \
--o-filtered-table output/feature_table_live_vs_dead_metadata_filtered.qza

#filter the feature table with each classification taxonomy to remove organelles

#base silva 138 filtering
qiime taxa filter-table \
--i-table output/feature_table_live_vs_dead_metadata_filtered.qza \
--i-taxonomy output/silva_classification_taxonomy.qza \
--p-exclude 'mitochondria,chloroplast' \
--o-filtered_table output/feature_table_live_vs_dead_metadata_silva_filtered.qza

#extended silva 138 filtering
qiime taxa filter-table \
--i-table output/feature_table_live_vs_dead_metadata_filtered.qza \
--i-taxonomy output/silva_extended_classification_taxonomy.qza \
--p-exclude 'mitochondria,chloroplast' \
--o-filtered_table output/feature_table_live_vs_dead_metadata_silva_extended_filtered.qza

#generate taxa barplots to visualize the changes (view @ https://view.qiime2.org)

#base silva 138 barplot
qiime taxa barplot \
--i-table output/feature_table_live_vs_dead_metadata_silva_filtered.qza \
--i-taxonomy output/silva_classification_taxonomy.qza \
--m-metacdata-file input/sample_metadata_live_vs_dead_combo.tsv \
--o-visualization output/feature_table_live_vs_dead_metadata_silva_filtered_barplot.qzv

#extended silva 138 barplot
qiime taxa barplot \
--i-table output/feature_table_live_vs_dead_metadata_silva_extended_filtered.qza \
--i-taxonomy output/silva_extended_classification_taxonomy.qza \
--m-metacdata-file input/sample_metadata_live_vs_dead_combo.tsv \
--o-visualization output/feature_table_live_vs_dead_metadata_silva_extended_filtered_barplot.qzv
