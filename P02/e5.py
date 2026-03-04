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
importing = c.talk(f"Sending {gene} Gene to the server, in fragments of 10 bases...")
print(f"{importing}\n From client: Sending {gene} Gene to the server, n fragments of 10 bases...")
send_bases = c.talk(str(gene_bases))
print(f"\n{importing}\n To server:{str(gene_bases)}")

