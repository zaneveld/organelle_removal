#this script denoises sequences created by demux.py
#this generates dada2 and deblur feature tables/rep seq artifacts with and without
#the sortmerna 16S filter

from os.path import join
import subprocess
import tempfile

from qiime2 import Artifact
from qiime2 import Metadata
from qiime2.plugins.demux.methods import emp_single
from qiime2.plugins.dada2.methods import denoise_single
from qiime2.plugins.deblur.methods import denoise_16S, denoise_other
from qiime2.plugins.feature_table.methods import filter_features, filter_seqs, merge, merge_seqs
from qiime2.plugins.quality_filter.methods import q_score

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
lanes = {'milk':6}#'GCMP':2, 'GSMP':2, 'human_gut':14, 'milk':6, 'peru_ants':1, 'mocks':10, 'song':13}
smrna_ref_fasta = join(working_dir, 'taxonomy_references', 'gg_88_otus.fasta')
smrna_ref = join(working_dir, 'taxonomy_references', 'sortmerna', 'gg_88_otus')
smrna_ref_param = smrna_ref_fasta + ',' + smrna_ref

for study, lane_count in lanes.items():
    d2_tables = []
    d2_seqs = []
    deblur_tables = []
    deblur_seqs = []
    deblur_unfiltered_tables = []
    deblur_unfiltered_seqs = []
    for lane in range(1, 1 + lane_count):
#        demuxed_seqs = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_demuxed_seqs.qza'))
        d2_table = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_unfiltered_table.qza'))
        d2_rep_seqs = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_unfiltered_seqs.qza'))
#        , d2_stats, = denoise_single(demuxed_seqs, 100, n_threads = 30)
        d2_tables.append(d2_table)
        d2_seqs.append(d2_rep_seqs)
#        d2_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_unfiltered_table.qza'))
#        d2_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_unfiltered_seqs.qza'))
#        d2_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_unfiltered_stats.qza'))

#        qual_filtered_seqs, qual_filtered_stats, = q_score(demuxed_seqs)
#        qual_filtered_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_qual_filtered_stats.qza'))

        deblur_table = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_filtered_table.qza'))
        deblur_rep_seqs = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_filtered_seqs.qza'))
#        , deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = True, jobs_to_start = 30)
        deblur_tables.append(deblur_table)
        deblur_seqs.append(deblur_rep_seqs)
#        deblur_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_filtered_table.qza'))
#        deblur_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_filtered_seqs.qza'))
#        deblur_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_filtered_stats.qza'))

        #deblur with a positive filter of the original sequences, effectively eliminating the filter
#        fasta = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_fasta_seqs.qza'))
        deblur_unfiltered_table = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_unfiltered_table.qza'))
        deblur_unfiltered_rep_seqs = Artifact.load(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_unfiltered_seqs.qza'))
#        , deblur_unfiltered_stats, = denoise_other(qual_filtered_seqs, fasta, 100, jobs_to_start = 30)
        deblur_unfiltered_tables.append(deblur_unfiltered_table)
        deblur_unfiltered_seqs.append(deblur_unfiltered_rep_seqs)
#        deblur_unfiltered_table.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_unfiltered_table.qza'))
#        deblur_unfiltered_rep_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_unfiltered_seqs.qza'))
#        deblur_unfiltered_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_unfiltered_stats.qza'))

    d2_merged_table, = merge(d2_tables, 'sum')
    d2_merged_table.save(join(working_dir, 'input', study + '_dada2_unfiltered_merged_ft.qza'))
    d2_merged_seqs, = merge_seqs(d2_seqs)
    d2_merged_seqs.save(join(working_dir, 'input', study + '_dada2_unfiltered_merged_seqs.qza'))

    deblur_merged_table, = merge(deblur_tables, 'sum')
    deblur_merged_table.save(join(working_dir, 'input', study + '_deblur_filtered_merged_ft.qza'))
    deblur_merged_seqs, = merge_seqs(deblur_seqs)
    deblur_merged_seqs.save(join(working_dir, 'input', study + '_deblur_filtered_merged_seqs.qza'))

    deblur_unfiltered_merged_table, = merge(deblur_unfiltered_tables, 'sum')
    deblur_unfiltered_merged_table.save(join(working_dir, 'input', study + '_deblur_unfiltered_merged_ft.qza'))
    deblur_unfiltered_merged_seqs, = merge_seqs(deblur_unfiltered_seqs)
    deblur_unfiltered_merged_seqs.save(join(working_dir, 'input', study + '_deblur_unfiltered_merged_seqs.qza'))


    with tempfile.TemporaryDirectory() as temp_dir:
        filtered_ids = []
        d2_merged_seqs.export_data(temp_dir)
        subprocess.run(['sortmerna', '--reads', join(temp_dir, 'dna-sequences.fasta'), '--ref', smrna_ref_param, '--aligned', join(temp_dir, 'filtered_seqs'), '--blast', '3', '--best', '1', '--print_all_reads', '-v', '-e', '100'])
        with open(join(temp_dir, 'filtered_seqs.blast')) as file:
            for line in file:
                line = line.strip().split('\t')
                if line[1] == '*':
                    continue
                if (float(line[2]) >= 65) and (float(line[13]) >= 50) and (float(line[11]) >= 65):
                    filtered_ids.append(line[0])
        with open(join(temp_dir, 'seq_ids.tsv'), 'w') as file:
            file.write('FeatureID\n')
            for id in filtered_ids:
                file.write(id + '\n')
        ids = Metadata.load(join(temp_dir, 'seq_ids.tsv'))
    d2_filtered_merged_table, = filter_features(d2_merged_table, metadata = ids)
    d2_filtered_merged_seqs, = filter_seqs(d2_merged_seqs, d2_filtered_merged_table)
    d2_filtered_merged_table.save(join(working_dir, 'input', study + '_dada2_filtered_merged_ft.qza'))
    d2_filtered_merged_seqs.save(join(working_dir, 'input', study + '_dada2_filtered_merged_seqs.qza'))
