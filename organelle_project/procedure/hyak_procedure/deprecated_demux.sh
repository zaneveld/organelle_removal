qiime qiime demux emp-single
for artifact in 170_s_1_1
       
	import Metadata
from qiime2.plugins.demux.methods import emp_single

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
for study in ['human_gut']:#['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants']:
    for seq_path in glob.glob(working_dir + '/input/' + study + '/*seqs.qza'):
        seqs = Artifact.load(seq_path)
        qza_name = os.path.basename(seq_path)
        artifact_id = qza_name.rstrip('seqs.qza')
        if artifact_id.endswith('_'):
            artifact_id = artifact_id.rstrip('_')
        md_path = working_dir + '/input/' + study + '/' + artifact_id + '_barcodes.txt'
        print(md_path)
        metadata = Metadata.load(md_path)
        barcodes = metadata.get_column('barcode')
        demuxed_seqs, stats = emp_single(seqs, barcodes, rev_comp_mapping_barcodes = False)
        demuxed_seqs.save(working_dir + '/input/' + study + '/demuxed_' + qza_name)
        stats.save(working_dir + '/input/' + study + '/' + artifact_id + 'demux_stats.qza')
