from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
a = file_contents.split("\n")
body = a[1::]
b = "".join(body)

exon1 = "GCTGGCCCCAGGGAAAGCCGAGCGGCCACCGAGCCGGCAGAGACCCACCGAGCGGCGGCGGAGGGAGCAGCGCCGGGGCGCACGAGGGCACCATGGCCCAGACGCCCGCCTTCGACAAGCCCAAA"
index1 = b.find(exon1)
print(index1)
length1 = len(exon1)
print(length1)
start = 44652852
end = 44584296

start1 = start - index1
print(start1)