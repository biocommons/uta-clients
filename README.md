# uta-clients

A package containing clients of [UTA](https://github.com/biocommons/uta).

Each acts as a data provider for [hgvs](https://github.com/biocommons/hgvs), a library of sequence manipulation tools. Ensuring a data provider for hgvs allows users to normalize, validate, and map sequence variants, among other functionalities such as parsing and formatting that are included in the hgvs library.

## Clients

Supported clients include:
- [uta](https://github.com/biocommons/hgvs/blob/main/src/hgvs/dataproviders/uta.py)
- uta ([rest](https://github.com/ccaitlingo/uta-rest/tree/main/src/uta_restapi))
- cdot ([rest](https://github.com/SACGF/cdot/blob/main/cdot/hgvs/dataproviders/json_data_provider.py))

## Cdot vs Uta
Read the official cdot documentation [here](https://github.com/SACGF/cdot).

\* = places where different transcripts have been returned due to cdot and uta being two different data sources/collectors

| Data Provider Function    | uta       | cdot      |
| ------------------------- |-----------| ----------|
| get_seq                   |           |
| get_acs_for_protein_seq   |           | Not implemented (note in hgvs to drop this method)
| get_gene_info             | Includes datetime of when transcript was added  |
| get_tx_exons              | Includes the following additional fields: hgnc, tx_aseq, alt_aseq, tx_exon_set_id, alt_exon_set_id, tx_exon_id, alt_exon_id, exon_aln_id
| get_tx_for_gene           | *         | *
| get_tx_for_region         |
| get_alignments_for_region |           |
| get_tx_identity_info      |
| get_tx_info               |           |
| get_tx_mapping_options    |
| get_similar_transcripts   |           | Not implemented (hgvs does not use this function)
| get_pro_ac_for_tx_ac      |
| get_assembly_map          |


## Using with hgvs

    $ pip install hgvs
    $ pip install utaclients

In python:

    >>> import hgvs
    >>> import utaclients
    >>> hdp = ...

Assign any of the following supported clients to your hgvs data provider.

    >>> hdp = utaclients.uta.connect()
    >>> hdp = utaclients.utarest.connect()
    >>> hdp = utaclients.cdot.connect()

Then you can get started using all the functionalities of hgvs.

    >>> hdp = utaclients.uta.connect()

    >>> am = hgvs.assemblymapper.AssemblyMapper(hdp,
    ...     assembly_name='GRCh37', alt_aln_method='splign',
    ...     replace_reference=True)


## Developer Installation

    $ make devready
    $ source venv/bin/activate
