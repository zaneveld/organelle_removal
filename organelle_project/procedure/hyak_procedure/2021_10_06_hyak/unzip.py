import zipfile
import tempfile
import os
import shutil

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'

for file in os.listdir(working_dir + '/input'):
    if file.endswith('.zip'):
        dir_name = os.path.dirname(os.path.join(working_dir, 'input', file.rstrip('.zip')))
        os.makedirs(dir_name, exist_ok = True)
        zip_path = os.path.join(working_dir, 'input', file)
        with zipfile.ZipFile(zip_path, 'r') as zip:
            zip.extractall(dir_name)
