import json

def list_species_json(limit, n_species, species, options):
    data = {
        "limit": limit,
        "n_species": n_species,
        "species": []}

    for i in options:
        number = species[i]
        name = number["display_name"]
        data["species"].append(name)
    return json.dumps(data)

def karyotype_json(karyotype):
    data = {"chromosomes": karyotype}
    return json.dumps(data)

def chromosome_length_json(length):
    data = {"chromosome_length": length}
    return json.dumps(data)

def gene_seq_json(gene, sequence):
    data = {"gene": gene, "sequence": sequence}
    return json.dumps(data)

def gene_lookup_json(gene, id):
    data = {"gene": gene, "id": id}
    return json.dumps(data)

def gene_info_json(gene, start, end, length, id, chrom_name):
    data = {"gene": gene, "start": start, "end": end, "length": length}
    return json.dumps(data)

def gene_calc_json(gene, bases, length):
    data = {"gene": gene, "length": length, "base calculations": bases}
    return json.dumps(data)

def gene_list_json(chromo, start, end, name_list):
    data = {"chromosome": chromo, "start": start, "end": end, "names": name_list}
    return json.dumps(data)