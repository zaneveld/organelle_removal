from qiime2.plugins.taxa.visualizers import barplot
from qiime2 import Artifact
from qiime2.metadata import Metadata
import glob
import os
import pandas as pd
import tempfile
from qiime2 import Visualization

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
denoisers = ['dada2', 'deblur']
studies = ['GCMP', 'GSMP', 'milk', 'peru_ants']
classifiers = ['vsearch', 'nb']
references = ['silva', 'silva_extended', 'gg', 'gg_extended']

#for study in studies:
#    metadata = Metadata.load(glob.glob(working_dir + '/input/' + study + '/mapping_files/*mapping_file.txt')[0])
#    df = metadata.to_dataframe()
#    df = df.drop(df.columns.difference(['#SampleID']), 1)
#    ids = Metadata(df)
#    for denoiser in denoisers:
#        ft = Artifact.load(working_dir + '/output/' + study + '_' + denoiser + '_merged_ft.qza')
#        for classifier in classifiers:
#            for reference in references:
#                taxonomy = Artifact.load(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_' + classifier + '_classification_taxonomy.qza')
#                tbp, = barplot(ft, taxonomy, ids)
#                tbp.save(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_' + classifier + '_tbp.qzv')

results = pd.DataFrame(columns = ['absolute unassigned', 'proportion unassigned',
                                  'absolute chloroplasts', 'proportion chloroplasts',
                                  'absolute mitochondria', 'proportion mitochondria',
                                  'denoise method', 'reference taxonomy']).rename_axis('#SampleID')
with tempfile.TemporaryDirectory() as temp_dir:
    for study in studies:
        study_results = pd.DataFrame().rename_axis('#SampleID')
        for denoiser in denoisers:
            denoiser_results = pd.DataFrame().rename_axis('#SampleID')
            for classifier in classifiers:
                classifier_results = pd.DataFrame().rename_axis('#SampleID')
                for reference in references:
                    reference_results = pd.DataFrame().rename_axis('#SampleID')
                    qzv = Visualization.load(working_dir + '/output/' + study + '_' + denoiser + '_' + reference + '_' + classifier + '_tbp.qzv')
                    qzv.export_data(temp_dir)
                    df = pd.read_csv(temp_dir + '/level-1.csv', index_col = 0)
                    df['total'] = df.sum(1)
                    if 'Unassigned' in df.columns:
                        df['proportion unassigned'] = df['Unassigned'] / df['total']
                        reference_results['absolute unassigned'] = df['Unassigned']
                        reference_results['proportion unassigned'] = df['proportion unassigned']
                    else:
                        reference_results['absolute unassigned'] = 0
                        reference_results['proportion unassigned'] = 0
                    if 'silva' in reference:
                        df = pd.read_csv(temp_dir + '/level-4.csv', index_col = 0)
                        df['total'] = df.sum(1)
                        df['proportion chloroplasts'] = df['d__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast'] / df['total']
                        reference_results['absolute chloroplasts'] = df['d__Bacteria;p__Cyanobacteria;c__Cyanobacteriia;o__Chloroplast']
                    else:
                        df = pd.read_csv(temp_dir + '/level-3.csv', index_col = 0)
                        df['total'] = df.sum(1)
                        df['proportion chloroplasts'] = df['k__Bacteria;p__Cyanobacteria;c__Chloroplast'] / df['total']
                        reference_results['absolute chloroplasts'] = df['k__Bacteria;p__Cyanobacteria;c__Chloroplast']
                    reference_results['proportion chloroplasts'] = df['proportion chloroplasts']
                    df = pd.read_csv(temp_dir + '/level-5.csv', index_col = 0)
                    df['total'] = df.sum(1)
                    if 'silva' in reference:
                        if 'd__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria' in df.columns:
                            df['proportion mitochondria'] = df['d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria'] / df['total']
                            reference_results['absolute mitochondria'] = df['d__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__Mitochondria']
                        else:
                            df['proportion mitochondria'] = 0
                            reference_results['absolute mitochondria'] = 0
                    else:
                        if 'k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria' in df.columns:
                            df['proportion mitochondria'] = df['k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria'] / df['total']
                            reference_results['absolute mitochondria'] = df['k__Bacteria;p__Proteobacteria;c__Alphaproteobacteria;o__Rickettsiales;f__mitochondria']
                        else:
                            df['proportion mitochondria'] = 0
                            reference_results['absolute mitochondria'] = 0
                    reference_results['proportion mitochondria'] = df['proportion mitochondria']
                    reference_results['reference taxonomy'] = reference
                    classifier_results = classifier_results.append(reference_results)
                classifier_results['classification method'] = classifier
                denoiser_results = denoiser_results.append(classifier_results)
            denoiser_results['denoise method'] = denoiser
            study_results = study_results.append(denoiser_results)
        study_results['study'] = study
        results = results.append(study_results)
        md_path = glob.glob(working_dir + '/input/' + study + '/mapping_files/*mapping_file.txt')[0]
        metadata = Metadata.load(md_path)
        md = metadata.to_dataframe()
        results_with_metadata = results.merge(md, 'left', left_index = True, right_index = True).rename_axis('sample-id')
        results_with_metadata.to_csv(working_dir + '/output/' + study + '_proportions.csv')
