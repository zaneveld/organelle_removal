qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GCMP_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GCMP_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/GCMP_deblur_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/GSMP_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/GSMP_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/GSMP_deblur_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/human_gut_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/human_gut_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/human_gut_deblur_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/milk_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/milk_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/milk_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/milk_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/milk_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/milk_deblur_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/peru_ants_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/peru_ants_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/peru_ants_deblur_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/song_dada2_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree  /gscratch/zaneveld/sonettd/organelle_removal/output/song_dada2_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/output/song_dada2_placements.qza

qiime fragment-insertion sepp \
--i-representative-sequences /gscratch/zaneveld/sonettd/organelle_removal/input/song_deblur_merged_seqs.qza \
--i-reference-database /gscratch/zaneveld/sonettd/organelle_removal/taxonomy_references/sepp-refs-silva-128.qza \
--p-threads 40 \
--o-tree /gscratch/zaneveld/sonettd/organelle_removal/output/song_deblur_rooted_tree.qza \
--o-placements /gscratch/zaneveld/sonettd/organelle_removal/song_deblur_placements.qza
