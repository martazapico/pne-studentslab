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
    for gene in seq:
        filename = f"../S04/sequences/{gene}.txt"
        file = Path(filename).read_text()
        a = file.split("\n")
        body = a[1::]
        first_part = "".join(body)
        count = 0
        for i in first_part:
            count += 1
        print(f"Gene {gene} -> Length: {count}")
#Exercise 4:
def seq_count_base(seq, base):
    from pathlib import Path
    print("-----| Exercise 4 |------\n")
    for gene in seq:
        print(f"Gene {gene}:")
        for b in base:
            base[b] = 0
        filename = f"../S04/sequences/{gene}.txt"
        file = Path(filename).read_text()
        a = file.split("\n")
        body = a[1::]
        b = "".join(body)
        for type in b:
            if type in base:
                base[type] += 1
        for bases, count in base.items():
            print(f'  {bases}: {count}')
        print("")
