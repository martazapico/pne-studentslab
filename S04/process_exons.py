def get_exons_from_file(filename):
    from pathlib import Path
    file_cont = Path(filename).read_text()
    file_contents = file_cont.split("\n")
    sequences = []
    headers = []
    lines = []
    for i in file_contents:
        if i.startswith(">"):
            headers.append(i)
    for i in file_contents:
        if i.startswith(">"):
            if len(lines) > 0:
                sequences.append("".join(lines))
                lines = []
        else:
            lines.append(i.strip())
    if len(lines) > 0:
        sequences.append("".join(lines))

    return sequences

filename = "sequences/ADA_EXONS.txt"
exon = get_exons_from_file(filename)
print(exon)
