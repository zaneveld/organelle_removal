import glob
from subprocess import check_output,CalledProcessError
import os
from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.quality_filter.methods import q_score
from qiime2.plugins.deblur.methods import denoise_16S
from qiime2.plugins.dada2.methods import denoise_single
from qiime2.plugins.metadata.visualizers import tabulate
from qiime2.plugins.deblur.visualizers import visualize_stats

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for study in ['human_gut']:#['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']:
    for i in range (11, 17):
        seq_path = '/gscratch/zaneveld/sonettd/organelle_removal/input/human_gut/demuxed_170_s_'+str(i)+'_1_seqs.qza'#glob.glob(working_dir + '/input/' + study + '/demuxed*seqs.qza'):
        seqs = Artifact.load(seq_path)
        qza_name = os.path.basename(seq_path)
        artifact_id = qza_name.rstrip('_seqs.qza').lstrip('demuxed_')
        if not os.path.exists(working_dir + '/output/' + study + '_dada2_' + artifact_id + '_rep_seqs.qza'):
            d2_table, d2_rep_seqs, d2_stats, = denoise_single(seqs, 100, n_threads = 16)
            d2_table.save(working_dir + '/output/' + study + '_dada2_' + artifact_id + '_ft.qza')
            d2_rep_seqs.save(working_dir + '/output/' + study + '_dada2_' + artifact_id + '_rep_seqs.qza')
            #d2_stats.save(working_dir + '/output/' + study + '_dada2_' + artifact_id + '_stats.qza')
            #d2_stats_qzv = tabulate(d2_stats)
            #d2_stats_qzv.save(working_dir + '/output/' + study + '_dada2_' + artifact_id + '_stats.qzv')
        if not os.path.exists(working_dir + '/output/' + study + '_deblur_' + artifact_id + '_rep_seqs.qza'):
            try:
                qual_filtered_seqs, qual_filtered_stats, = q_score(seqs)
            #qual_filtered_stats_qzv = tabulate(qual_filtered_stats)
            #qual_filtered_stats_qzv.save(working_dir + '/output/' + study + '_' + artifact_id + '_quality_filtered_stats.qzv')
                deblur_table, deblur_rep_seqs, deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = False, jobs_to_start = 16)
                deblur_table.save(working_dir + '/output/' + study + '_deblur_' + artifact_id + '_ft.qza')
                deblur_rep_seqs.save(working_dir + '/output/' + study + '_deblur_' + artifact_id + '_rep_seqs.qza')
            #deblur_stats.save(working_dir + '/output/' + study + '_deblur_' + artifact_id + '_stats.qza')
            #deblur_stats_qzv = visualize_stats(deblur_stats)
            #deblur_stats_qzv.save(working_dir + '/output/' + study + '_deblur_' + artifact_id + '_stats.qzv')
            except (ValueError, CalledProcessError) as e:
                print('number', i, 'failed\n')
                continue
