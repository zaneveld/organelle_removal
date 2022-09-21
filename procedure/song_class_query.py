from os.path import join
import pandas as pd
from Bio import Entrez

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

working_dir = '/mnt/c/Users/dsone/Documents/zaneveld/22_sept_procedure'#'/gscratch/zaneveld/sonettd/organelle_removal/'
Entrez.email = "sonettd@uw.edu"

#read the sample metadata file from qiita as a csv
metadata = pd.read_csv(join(working_dir, 'input', 'song_sample_metadata.txt'), sep = '\t', index_col = 0)
metadata.index.names = ['index']
species_names = metadata['corrected_species_name'].to_list()

ncbi_lineages = get_ncbi_lineages(species_names)

#many rows are still not populated with class information. Additionally, subclass
#Lepidosauria is incorrectly listed as the class of many reptiles (I assume due
#to the way I queried for the string "class" which is technically in "subclass")
#see 'song_sample_metadata_classes_cannonical.tsv' for the manually curated version

lineages = pd.DataFrame.from_dict(ncbi_lineages, orient = 'index', columns = ['class', 'order', 'family', 'genus'])
merged = metadata.merge(lineages, 'left', left_on = 'species_name', right_index = True)
merged.index.names = ['sample_name']
merged.to_csv(join(working_dir, 'input', 'song_sample_metadata_taxa.tsv'), sep = '\t')