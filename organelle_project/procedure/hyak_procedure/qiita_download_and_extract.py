#!/usr/bin/env python
# coding: utf-8

import glob
import gzip
import os
import urllib.request
import shutil
import tempfile
from qiime2 import Artifact
from qiime2 import Metadata
from qiime2.plugins.cutadapt.methods import demux_single
from qiime2.plugins.dada2.methods import denoise_single
from qiime2.plugins.deblur.methods import denoise_16S
from zipfile import ZipFile


qiita_prep_id = 1257 # "sample info (only this prep)"
qiita_artifact_id = 701 #artifact of interest is the 'demultiplexed' artifact directly downstream
#of split libraries FASTQ (not one of the trimmed artifacts)
working_dir = '/mnt/c/Users/Dylan/Documents/zaneveld/klone/smp'
refs_dir = working_dir + '/taxonomy_references'

def download_file(url, local_filepath):
    with urllib.request.urlopen(url) as response, open(local_filepath, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

def download_qiita_files(qiita_prep_id, qiita_artifact_id):
    """Download and extract the metadata from the study as well as the biom
    file and fasta file for each artifact listed.

    Parameters
    ----------
    qiita_prep_id : int or str
        the prep id of the run of interest. This ID is unique to each
        run within a study.
    qiita_artifact_id : int, str, or list of ints or strs
        the artifact id of the deblur reference hit table artifact. One
        artifact per 16S prep in the study, which will be merged"""

    download_file('https://qiita.ucsd.edu/public_download/?data=prep_information&prep_id=' +
                  str(qiita_prep_id), working_dir + '/input/metadata.zip')
    #download artifacts
    download_file('https://qiita.ucsd.edu/public_artifact_download/?artifact_id=' +
                  str(qiita_artifact_id),
                  working_dir + '/input/qiita_artifact.zip')

download_qiita_files(qiita_prep_id, qiita_artifact_id)

#unzip files
with ZipFile(working_dir + '/input/qiita_artifact.zip') as artifact_zip:
    with artifact_zip.open('Demultiplexed/' + str(qiita_artifact_id) + '/seqs.fastq.gz') as zipped, open(working_dir + '/input/seqs.fastq.gz', 'wb') as file:
        shutil.copyfileobj(zipped, file)
with ZipFile(working_dir + '/input/metadata.zip') as metadata_zip:
    path = metadata_zip.namelist()[0]
    with metadata_zip.open(path) as zipped, open(working_dir + '/input/barcodes.txt', 'wb') as file:
        shutil.copyfileobj(zipped, file)

#set up barcode file
with open(working_dir + '/input/barcodes.txt') as file:
    lines = file.readlines()
    lines[0] = '#SampleID\tbarcode\tcenter_name\texperiment_design_description\tinstrument_model\tlibrary_construction_protocol\tpcr_primers\tplatform\tprimer\tqiita_prep_id\tsequencing_meth\ttarget_gene\ttarget_subfragment\n'
    with open(working_dir + '/input/qiime2/barcode_file.tsv', 'w') as metadata:
        for line in lines:
            metadata.write(line)