#running the python script through slurm hangs the server, so we're back to command line prompts

# qiime fragment-insertion sepp \
# --i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP_dada2_unfiltered_merged_seqs.qza \
# --i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
# --p-threads 10 \
# --o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_dada2_unfiltered_tree.qza \
# --o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_deblur_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP_dada2_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_dada2_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_deblur_unfiltered_placements.qza

# qiime fragment-insertion sepp \
# --i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut_dada2_unfiltered_merged_seqs.qza \
# --i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
# --p-threads 10 \
# --o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_dada2_unfiltered_tree.qza \
# --o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_deblur_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/milk_dada2_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/milk_dada2_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/milk_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/milk_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/milk_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/milk_deblur_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants_dada2_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_dada2_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_deblur_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/song_dada2_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/song_dada2_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/song_dada2_unfiltered_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/song_deblur_unfiltered_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-gg-13-8.qza \
--p-threads 10 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/song_deblur_unfiltered_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/song_deblur_unfiltered_placements.qza
