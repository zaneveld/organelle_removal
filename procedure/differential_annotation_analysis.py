from os.path import join
import tempfile

from Bio import SeqIO
import pandas as pd
from qiime2 import Artifact

working_dir = '/mnt/c/Users/Dylan/Documents/zaneveld/22_may_procedure/'
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song']
denoisers = ['dada2', 'deblur']
filters = ['unfiltered', 'filtered']
classifiers = ['vsearch', 'nb']
base_refs = ['silva', 'gg']

differential_annotations = pd.DataFrame()
for study in studies:
    study_df = pd.DataFrame()
    with open(join(working_dir, 'output', f'{study}_differential_annotations.fasta'), 'w') as fasta_file:
        for denoiser in denoisers:
            denoiser_df = pd.DataFrame()
            rep_seqs = Artifact.load(join(working_dir, 'input', f'{study}_{denoiser}_unfiltered_merged_seqs.qza'))
            #in addition to the sequences themselves, we're also interested
            #in the frequency of the sequences - which are most common?


            #the classifiers currently list the FeatureIDs by their hashes.
            #We need to recover the actual 100 bp sequence.
            #this is a rather brute-force approach which loads everything into memory
            with tempfile.TemporaryDirectory() as temp_dir:
                rep_seqs.export_data(temp_dir)
                fasta_seqs = SeqIO.to_dict(SeqIO.parse(join(temp_dir, 'dna-sequences.fasta'), 'fasta'))
            for hashed_id, record in fasta_seqs.items():
                fasta_seqs[hashed_id] = str(record.seq)
            for filter_ in filters:
                filter_df = pd.DataFrame()
                for classifier in classifiers:
                    classifier_df = pd.DataFrame()
                    for base in base_refs:
                        base_path = join(working_dir, 'output', f'{study}_{denoiser}_{filter_}_{base}_{classifier}_classification_taxonomy.qza')
                        base_classification = Artifact.load(base_path)
                        with tempfile.TemporaryDirectory() as temp_dir:
                            base_classification.export_data(temp_dir)
                            base_taxonomy = pd.read_csv(join(temp_dir, 'taxonomy.tsv'), sep = '\t')
                            base_taxonomy['sequence'] = base_taxonomy['Feature ID'].map(fasta_seqs)
                        extended_path = join(working_dir, 'output', f'{study}_{denoiser}_{filter_}_{base}_extended_{classifier}_classification_taxonomy.qza')
                        extended_classification = Artifact.load(extended_path)
                        with tempfile.TemporaryDirectory() as temp_dir:
                            extended_classification.export_data(temp_dir)
                            extended_taxonomy = pd.read_csv(join(temp_dir, 'taxonomy.tsv'), sep = '\t')
                            extended_taxonomy['sequence'] = extended_taxonomy['Feature ID'].map(fasta_seqs)
                        base_taxonomy = base_taxonomy.sort_values('sequence').reset_index()
                        extended_taxonomy = extended_taxonomy.sort_values('sequence').reset_index()
                        #vsearch taxonomy has a different column name than nb
                        if classifier == 'vsearch':
                            base_taxonomy = base_taxonomy.drop(['Consensus', 'index'], axis = 1)
                            extended_taxonomy = extended_taxonomy.drop(['Consensus', 'index'], axis = 1)
                        else:
                            base_taxonomy = base_taxonomy.drop(['Confidence', 'index'], axis = 1)
                            extended_taxonomy = extended_taxonomy.drop(['Confidence', 'index'], axis = 1)
                        results = base_taxonomy.compare(extended_taxonomy).reset_index(drop = True)
                        results.columns = ['base annotation', 'extended annotation']
                        results['sequence'] = base_taxonomy['sequence']
                        results['Feature ID'] = base_taxonomy['Feature ID']
                        results['base reference'] = base
                        classifier_df = pd.concat([classifier_df, results])
                    classifier_df['classification method'] = classifier
                    filter_df = pd.concat([filter_df, classifier_df])
                filter_df['positive filter'] = filter_
                denoiser_df = pd.concat([denoiser_df, filter_df])
            denoiser_df['denoise method'] = denoiser
            study_df = pd.concat([study_df, denoiser_df])
    study_df['study'] = study
    differential_annotations = pd.concat([differential_annotations, study_df])
differential_annotations.to_csv(join(working_dir, 'output', 'differential_annotations.tsv'), sep = '\t', index = False)

