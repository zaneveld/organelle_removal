#>50 hours on hyak
from os.path import join

from qiime2 import Artifact
from qiime2.metadata import Metadata
from qiime2.plugins.demux.methods import emp_single

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
lanes = {'GCMP':2}#, 'GSMP':2, 'human_gut':14, 'milk':6, 'peru_ants':1, 'song':13, 'mocks':1}

for study, lane_count in lanes.items():
    for lane in range(1, 1 + lane_count):
        seq_path = join(working_dir, 'input', study, study + '_' + str(lane) + '_sequences.qza')
        seqs = Artifact.load(seq_path)
        md_path = join(working_dir, 'input', study, str(lane) + '_barcodes.tsv')
        metadata = Metadata.load(md_path)
        barcodes = metadata.get_column('barcode')
        if study == 'GCMP' or study == 'GSMP' or study == 'peru_ants':
            demuxed_seqs, stats = emp_single(seqs, barcodes, rev_comp_mapping_barcodes = True)
        elif study == 'milk':
            demuxed_seqs, stats = emp_single(seqs, barcodes, golay_error_correction = False)
        else:
            demuxed_seqs, stats = emp_single(seqs, barcodes)
        #demuxed_seqs.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demuxed_seqs.qza'))
        #stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_demux_ecd.qza'))
        d2_table, d2_rep_seqs, d2_stats, = denoise_single(demuxed_seqs, 100, n_threads = 30)
        d2_tables.append(d2_table)
        d2_seqs.append(d2_rep_seqs)
        d2_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_dada2_stats.qza'))
        qual_filtered_seqs, qual_filtered_stats, = q_score(demuxed_seqs)
        qual_filtered_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_qual_filtered_stats.qza'))
        deblur_table, deblur_rep_seqs, deblur_stats, = denoise_16S(qual_filtered_seqs, 100, sample_stats = True, jobs_to_start = 30)
        deblur_tables.append(deblur_table)
        deblur_seqs.append(deblur_rep_seqs)
        deblur_stats.save(join(working_dir, 'input', study, study + '_' + str(lane) + '_deblur_stats.qza'))
    d2_merged_table, = merge(d2_tables, 'sum')
    d2_merged_table.save(join(working_dir, 'input', study + '_' + '_dada2_merged_ft.qza'))
    d2_merged_seqs, = merge_seqs(d2_seqs)
    d2_merged_seqs.save(join(working_dir, 'input', study + '_' + '_dada2_merged_seqs.qza'))
    deblur_merged_table, = merge(deblur_tables, 'sum')
    deblur_merged_table.save(join(working_dir, 'input', study + '_' + '_deblur_merged_ft.qza'))
    deblur_merged_seqs, = merge_seqs(deblur_seqs)
    deblur_merged_seqs.save(join(working_dir, 'input', study + '_' + '_deblur_merged_seqs.qza'))
