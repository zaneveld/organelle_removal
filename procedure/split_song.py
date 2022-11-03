from os.path import join

import pandas as pd
from Bio import Entrez
from qiime2 import Artifact
from qiime2.plugins.feature_table.methods import filter_samples
from qiime2.metadata import Metadata


def get_ncbi_lineages(scientific_names):
    """query a list of scientific names against the NCBI Taxonomy database and
    return a dict of scientific name: class, order, family, genus"""

    sci_names = list(set(scientific_names))

    taxa = {}

    for name in sci_names:
        #NaN will break the query but it's the only float in this list
        if type(name) == float:
            continue
        #find a record in NCBI Taxonomy that matches the scientific name, copy the TaxID, and query the TaxID
        elif '_' in name:
            name = ' '.join(name.split('_'))
        handle = Entrez.esearch(db = 'Taxonomy', retmax = 1, term = name)
        record = Entrez.read(handle)
        handle.close()
        #if the search can't find anything, skip the rest and record that
        if record['Count'] == '0':
            _class = order = family = genus = 'not found'
        else:
            tax_id = record['IdList'][0]
            handle = Entrez.efetch(db = 'Taxonomy', id = tax_id)
            record = Entrez.read(handle)
            handle.close()
            #lineageEx contains all of the clades to which the organism belongs. I'm only interested in the class,
            #but might as well grab a few others while we're here
            lineage = record[0]['LineageEx']

            for taxon in lineage:
                if taxon['Rank'] == 'class':
                    _class = taxon['ScientificName']
                elif taxon['Rank'] == 'order':
                    order = taxon['ScientificName']
                elif taxon['Rank'] == 'family':
                    family = taxon['ScientificName']
                elif taxon['Rank'] == 'genus':
                    genus = taxon['ScientificName']
        taxa[name] = [_class, order, family, genus]
    
    return taxa

working_dir = '/gscratch/zaneveld/sonettd/organelle_removal'
Entrez.email = "sonettd@uw.edu"

md = Metadata.load(join(working_dir, 'input', 'song', 'sample_metadata.txt'))
md_df = md.to_dataframe()
if 'class' not in md_df.columns:
    md_df.index.names = ['index']
    species_names = md_df['corrected_species_name'].to_list()
    ncbi_lineages = get_ncbi_lineages(species_names)

    lineages = pd.DataFrame.from_dict(ncbi_lineages, orient = 'index', columns = ['class', 'order', 'family', 'genus'])
    merged = metadata.merge(lineages, 'left', left_on = 'species_name', right_index = True)
    merged.index.names = ['sample_name']
    merged.to_csv(join(working_dir, 'input', 'song', 'sample_metadata.txt', sep = '\t'))
    md = merged

for denoiser in ['dada2', 'deblur']:
    for filtered in ['filtered', 'unfiltered']:
        ft = Artifact.load(join(working_dir, 'input', f'song_{denoiser}_{filtered}_merged_ft.qza'))
        for name in ['Amphibia', 'Arachnida', 'Aves', 'Hyperoartia', 'Insecta', 'Leptocardii', 'Mammalia', 'Reptilia', 'Sagittoidea']:#, 'unknown']:
            where = f"class='{name}'"
            class_ft, = filter_samples(ft, metadata = md, where = where)
            class_ft.save(join(working_dir, 'input', f'song_{name}_{denoiser}_{filtered}_merged_ft.qza'))

