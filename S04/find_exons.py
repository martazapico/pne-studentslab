#worwking with ADA.txt:
from pathlib import Path
FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
a = file_contents.split("\n")
body = a[1::]
b = "".join(body)

#worwking with ADA_EXONS.txt:

from process_exons import get_exons_from_file
filename = "sequences/ADA_EXONS.txt"
exon = get_exons_from_file(filename)

start = 44652852
end = 44584296
number = 0
print(" | Exon  | Long. | Start      | End        |")
print(" -------------------------------------------")
for i in exon:

    number += 1
    if number < 10:
        number1 = f"{number} "
    else:
        number1 = f"{number}"
    length = len(i)
    if length < 100:
        length1 = f"{length} "
    else:
        length1 = f"{length}"
    index = b.find(i)
    end1 = start - index
    start1 = start - (index + length -1)

    print(f" | {number1}    | {length1}   | {start1}   | {end1}   |")