dna = "ATGCGATCGATCGATCGATCGA"
def length_sequence(dna):
    result = len(dna)
    return result
def first5(dna):
    result = dna[0:5]
    return result
def last3(dna):
    result = dna[-3:]
    return result
def lower(dna):
    result = dna.lower()
    return result
def atc(dna):
    count = 0
    for i in range(len(dna)-2):
        if dna[i] == "A" and dna[i+1] == "T" and dna[i+2] == "C":
            count += 1
    return count
def t_to_u(dna):
    new_string = dna.replace("T", "U")
    return new_string
print("The length of the sequence is:", length_sequence(dna))
print("The first five characters of the sequence are:", first5(dna))
print("The last three characters of the sequence are:", last3(dna))
print("The string converted to lowercase:", lower(dna))
print("The times the substring 'ATC' appears in the sequence are:", atc(dna))
print("The string with all occurrences of 'T' replaced by 'U'is:", t_to_u(dna))