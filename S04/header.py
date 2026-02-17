from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

a = file_contents.split("\n")
header = a[0]
print(header)
