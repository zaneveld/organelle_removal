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

for study in ['human_gut']: #['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']:
    for seq_path in glob.glob(working_dir + '/input/' + study + '/*/demuxed_p33_*_seqs.qza'):
        seqs = Artifact.load(seq_path)
        lane = os.path.basename(os.path.dirname(seq_path))
        d2_table, d2_rep_seqs, d2_stats, = denoise_single(seqs, 100, n_threads = 40)
        d2_table.save(working_dir + '/output/' + study + '_' + lane + '_dada2_ft.qza')
        d2_rep_seqs.save(working_dir + '/output/' + study + '_' + lane + '_dada2_rep_seqs.qza')
        d2_stats.save(working_dir + '/output/' + study + '_' + lane + '_dada2_stats.qza')
        d2_stats_view = d2_stats.view(Metadata)
        d2_stats_qzv, = tabulate(d2_stats_view)
        d2_stats_qzv.save(working_dir + '/output/' + study + '_' + lane + '_dada2_stats.qzv')
        #qiita does not use qual filtering, to my knowledge
        qual_filtered_seqs, qual_filtered_stats, = q_score(seqs)
        qual_filtered_seqs.save(working_dir + '/output/' + study + '_' + lane + '_quality_filtered_seqs.qzv')
        qual_filtered_stats_view = qual_filtered_stats.view(Metadata)
        qual_filtered_stats_qzv, = tabulate(qual_filtered_stats_view)
        qual_filtered_stats_qzv.save(working_dir + '/output/' + study + '_' + lane + '_quality_filtered_stats.qzv')
        deblur_table, deblur_rep_seqs, deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = True, jobs_to_start = 40)
        deblur_table.save(working_dir + '/output/' + study + '_' + lane + '_deblur_ft.qza')
        deblur_rep_seqs.save(working_dir + '/output/' + study + '_' + lane + '_deblur_rep_seqs.qza')
        deblur_stats.save(working_dir + '/output/' + study + '_' + lane + '_deblur_stats.qza')
        deblur_stats_qzv, = visualize_stats(deblur_stats)
        deblur_stats_qzv.save(working_dir + '/output/' + study + '_' + lane + '_deblur_stats.qzv')
