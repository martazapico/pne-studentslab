from mypyc.primitives.generic_ops import arg_count

sequence = input("Please, enter a DNA sequence here: ")
sequence = sequence.upper()
sequence_count = 0
a_count = 0
g_count = 0
t_count = 0
c_count = 0
for i in sequence:
    sequence_count += 1
    if i == "A":
        a_count += 1
    elif i == "G":
        g_count += 1
    elif i == "T":
        t_count += 1
    elif i == "C":
        c_count += 1
print("Total length:", sequence_count)
print("A:", a_count)
print("C:", c_count)
print("T:", t_count)
print("G:", g_count)