#find the frequencies of each feature, by study

from os.path import join

from qiime2 import Artifact
import pandas as pd

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
studies = ['GCMP', 'GSMP', 'human_gut', 'milk', 'peru_ants', 'song']
denoisers = ['dada2', 'deblur']
filters = ['filtered', 'unfiltered']
classifiers = ['vsearch', 'nb']
references = ['silva', 'gg']

df = pd.DataFrame()
for study in studies:
    for denoiser in denoisers:
        #filter, reference, and classifier aren't important, but it makes the merging step easier because everything is 1:1
        for filter_ in filters:
            for classifier in classifiers:
                for reference in references:
                    ft_df = Artifact.load(join(working_dir, 'input', f'{study}_{denoiser}_unfiltered_merged_ft.qza')).view(pd.DataFrame).transpose()
                    frequencies = ft_df.sum(axis = 1)
                    frequencies = frequencies.rename('frequency')
                    frequencies = frequencies.to_frame()
                    frequencies = frequencies.rename_axis('Feature ID')
                    frequencies['study'] = study
                    frequencies['denoise method'] = denoiser
                    frequencies['positive filter'] = filter_
                    frequencies['classification method'] = classifier
                    frequencies['base reference'] = reference
                    df = pd.concat([df, frequencies])

differential_annotations = pd.read_csv(join(working_dir, 'output', 'differential_annotations.tsv'), sep = '\t')
shared_columns = ['study', 'denoise method', 'positive filter', 'classification method', 'base reference', 'Feature ID']
differential_annotations = differential_annotations.merge(df, on = shared_columns, how = 'left', validate = 'one_to_one')
differential_annotations.to_csv(join(working_dir, 'output', 'differential_annotations.tsv'), sep = '\t')

total_frequencies = differential_annotations.groupby('sequence').sum().reset_index()
total_frequencies.columns = ['sequence', 'sequence frequency']
total_frequencies = total_frequencies.merge(differential_annotations, how = 'right', validate = 'one_to_many')
total_frequencies = total_frequencies.sort_values('sequence frequency', ascending = False)
total_frequencies = total_frequencies.drop_duplicates('sequence')
total_frequencies.to_csv(join(working_dir, 'output', 'dereplicated_differential_sequences.csv'))

with open(join(working_dir, 'output', 'differential_annotations.fasta'), 'w') as outfile:
    for index, sequence, sequence_frequency, base_annotation, extended_annotation,  Feature_ID, base_reference, classification_method, positive_filter, denoise_method, study, frequency in total_frequencies.itertuples():
        outfile.write(f'>{base_annotation}_|_{extended_annotation}_|_{sequence}_|_{sequence_frequency}_|_{study}\n{sequence}\n')
