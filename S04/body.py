from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

a = file_contents.split("\n")
body = a[1:]

print("\n".join(body))
