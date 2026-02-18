#Exercise 1:
def seq_ping():
    print("OK")
#Exercise 2:
def seq_read_fasta(filename):
    from pathlib import Path
    file = Path(filename).read_text()
    a = file.split("\n")
    body = a[1::]
    first_part = "".join(body)
    second_part = first_part[0:20]
    print(f"DNA file: {filename}")
    print("The first 20 bases are:")
    return second_part

#Exercise 3:
def seq_len(seq):
    from pathlib import Path
    gene_names = ["U5", "ADA", "FRAT1", "FXN"]
    filename = f"../S04/sequences/{gene_names[seq]}.txt"
    file = Path(filename).read_text()
    a = file.split("\n")
    body = a[1::]
    first_part = "".join(body)
    count = 0
    for i in first_part:
        count += 1
    return print(f"Gene {gene_names[seq]} -> Length: {count}")
#Exercise 4:
def seq_count_base(seq):
    from pathlib import Path
    gene_names = ["U5", "ADA", "FRAT1", "FXN"]
    print(f"Gene {gene_names[seq]}")
    filename = f"../S04/sequences/{gene_names[seq]}.txt"
    file = Path(filename).read_text()
    a = file.split("\n")
    body = a[1::]
    seq = "".join(body)
    base = {"A": 0, "C": 0, "T": 0, "G": 0}
    for i in seq:
        if i in base:
            base[i] += 1
    for base, count in base.items():
        print(f'  {base}: {count}')