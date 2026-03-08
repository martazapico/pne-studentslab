from P01.Seq1_new_version import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.97" # your IP address

PORT = 8081
c = Client(IP, PORT)

print(c)
s = Seq()
gene = "FRAT1"




FILENAME = f"../S04/sequences/{gene}.txt"
gene_bases = s.read_fasta(FILENAME)
print(f"Gene {gene}: {str(gene_bases)}")

importing = c.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases...")



number = 1
for i in range(0, len(gene_bases), 10):
    fragment = gene_bases[i:i + 10]
    print(f"Fragment {number}: {fragment}")
    c.talk(f"Fragment {number}: {fragment}")
    number += 1
    if number > 5:
        break


