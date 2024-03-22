# Organelle Removal

This repository holds code and tutorials for improved removal of cryptic organelle reads from 16S rRNA datasets analyzed in QIIME2.

## The problem of cryptical organelle sequences

Because mitochondria and chloroplasts derive from free-living bacterial ancestors, reads from host mitochondria or chloroplasts rRNAs often appear in 16S rRNA amplicon libraries. Typically these are identified during taxonomic annotation and removed. However, some mitochondrial sequences can be misannotated (especially in less studied groups of hosts), resulting in Unassigned annotations that are derived from host organelles. If not removed, these 'cryptic' mitochondrial sequences can distort alpha or beta-diversity measures.

Briefly, the approach described here is to supplement an existing taxonomic reference library (e.g. SILVA) with additional diverse mitochondrial reads to form an extended taxonomic reference,
then conduct downstream taxonomic analysis as usual.  In example datasets where high levels of cryptic mitochondrial reads were found, such as in the raw Global Coral Microbiome Project data, this greatly improves annotation of mitochondrial reads. Conversely in mock communities composed of known proportions of free-living bacteria, diversifying mitochondrial references does not result in false positive mitochondrial annotation

This repository includes pre-built extended taxonomies for SILVA138 and Greengenes 13_8. Tutorials show these can be incorporated into QIIME2 workflows that use either the command line interface or the python API. An additional tutorial shows how to build your own custom extended taxonomic reference, allowing updates to future releases of SILVA.

## Tutorials

### QIIME2 Command Line Interface Tutorial
[QIIME 2 Command Line Interface (CLI)](./Tutorial/qiime2_CLI_tutorial/organelle_removal_CLI.ipynb)

### QIIME2 API Tutorial
[QIIME 2 Command Line Interface (CLI)](./Tutorial/qiime2_API_tutorial/procedure/mitochondria_removal_protocol.ipynb)

### QIIME2 Custom Extended Taxonomy Tutorial
[QIIME 2 Extended Taxonomy Tutorial](./Tutorial/qiime2_API_tutorial/procedure/extended_taxonomy_construction_tutorial.ipynb)


## Manuscript Benchmarking Workflow

This repository also includes [code for the benchmarking of this method](./procedure/_index.txt) for the manuscript, in the `procedure` folder. Because many input 16S rRNA datasets analyzed in the manuscript are large, they are not included here, but the import step includes links to download them from QIITA. Similarly, because most output files are too large for GitHub, these must be regenerated. An output folder that will house them as scripts are run is included for convenience.


Reference:
```
The Organelle in the Ointment: cryptic mitochondria account for many unknown sequences in cross-species microbiome comparisons
Dylan Sonett, Tanya Brown, Johan Bengtsson-Palme, Jacqueline L. Padilla-Gamiño, Jesse R. Zaneveld
bioRxiv 2021.02.23.431501; doi: https://doi.org/10.1101/2021.02.23.431501
This article is a preprint and has not been certified by peer review
```
