#all scripts in order (this will take an absurd amount of time (weeks), mostly due to importing, demuxing, and denoising)

#WIP: need to add download/creation of reference taxonomies
#WIP: write script to grab counts at each filtering step

#import
sh /gscratch/zaneveld/sonettd/organelle_removal/procedure/import.sh

#demultiplex and denoise
python /gscratch/zaneveld/sonettd/organelle_removal/procedure/demux_denoise.py

#classify with all reference taxonomies
#WIP - update for all studies, match input and output files with other scripts

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/classify.py

#calculate organelle proportions
#WIP - update for all studies, match input and output files with other scripts

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/csvs.py

#calculate differences in organelle proportions
#WIP - update for all studies, match input and output files with other scripts
#WIP - splice in code from ipynbs to create plot image files

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/calculate_stats.py

#generate rooted trees for each study
#WIP - update for all studies, match input and output files with other scripts

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/sepp.py

#filter out organelles, rarefy to 1k depth
#WIP - update for all studies, match input and output files with other scripts

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/filter_rarefy.py

#calculate diversity metrics
#WIP - update for all studies, match input and output files with other scripts

python /gscratch/zaneveld/sonettd/organelle_removal/procedure/diversity.py