#lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]

f = open("dna.txt.", "r")
lines = f.readlines()
f.close()

bases = {"A": 0, "C": 0, "T": 0, "G": 0}

total = 0

for sequence in lines:
    sequence = sequence.strip()
    total += len(sequence)
    for i in sequence:
        if i in bases:
            bases[i]+=1

print("Total number of bases:", total)
for base, count in bases.items():
    print(f'{base}: {count}')

