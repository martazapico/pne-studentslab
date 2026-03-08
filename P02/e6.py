from P01.Seq1_new_version import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.97" # your IP address


PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
print(c1)

c2 = Client(IP, PORT2)
print(c2)

s = Seq()
gene = "FRAT1"




FILENAME = f"../S04/sequences/{gene}.txt"
gene_bases = s.read_fasta(FILENAME)
c1.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases...")
c2.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases...")


print(f"Gene {gene}: {str(gene_bases)}")


number = 1
for i in range(0, len(gene_bases), 10):
    if number % 2 == 0:
        c = c2
    else:
        c = c1
    fragment = gene_bases[i:i + 10]
    print(f"Fragment {number}: {fragment}")
    c.talk(f"Fragment {number}: {fragment}")
    number += 1
    if number > 10:
        break


