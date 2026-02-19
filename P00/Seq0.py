#Exercise 1:
def seq_ping():
    print("OK")
#Exercise 2:
def seq_read_fasta(filename):
    from pathlib import Path
    f = f"../S04/sequences/{filename}"
    file = Path(f).read_text()
    a = file.split("\n")
    body = a[1::]
    first_part = "".join(body)
    second_part = first_part[0:20]
    print(f"DNA file: {filename}")
    print("The first 20 bases are:")
    return print(second_part)

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
#Exercise 5:
def seq_count(seq, base):
    from pathlib import Path
    print("-----| Exercise 5 |------")
    for gene in seq:
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
        print(f"Gene {gene}: {base}")
#Exercise 6:
def seq_reverse(seq, n):
    from pathlib import Path
    filename = f"../S04/sequences/{seq}.txt"
    file = Path(filename).read_text()
    a = file.split("\n")
    body = a[1::]
    first_part = "".join(body)
    fragment = first_part[0:n]
    print("-----| Exercise 6 |------")
    print(f"Gene {seq}")
    print("Fragment:", fragment)
    reverse = fragment[::-1]
    print("Reverse:", reverse)
#Exercise 7:
def seq_complement(seq):
    from pathlib import Path
    filename = f"../S04/sequences/{seq}.txt"
    file = Path(filename).read_text()
    a = file.split("\n")
    body = a[1::]
    first_part = "".join(body)
    fragment = first_part[0:20]
    print("-----| Exercise 7 |------")
    print(f"Gene {seq}:")
    print("Frag:", fragment)
    bases = {"A": "T", "C": "G", "T": "A", "G": "C"}
    complement = ""
    for base in fragment:
        if base in bases:
            complement += bases[base]
    print("Comp:", complement)
#Exercise 8
def gene_processing(seq, base):
    from pathlib import Path
    print("-----| Exercise 8 |------")
    for gene in seq:
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
        base_dict = dict(base)
        max_value = max(base_dict.values())
        for name, value in base_dict.items():
            if value == max_value:
                most_frequent = name
        print(f"Gene {gene} : Most frequent Base:{most_frequent}")