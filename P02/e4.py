from P01.Seq1_new_version import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.97" # your IP address
PORT = 8081

c = Client(IP, PORT)
print(c)

s = Seq()

genes = ["U5", "FRAT1", "ADA"]



for gene in genes:
    FILENAME = f"../S04/sequences/{gene}.txt"
    gene_bases = s.read_fasta(FILENAME)
    importing = c.talk(f"Sending {gene} Gene to the server...")
    print(f"{importing}\n To server: Sending {gene} Gene to the server...")
    send_bases = c.talk(str(gene_bases))
    print(f"\n{importing}\n To server:{str(gene_bases)}")


