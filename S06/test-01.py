from P00.Seq0 import *

seq1 = "ATTCCCGGGG"

print(f"Seq:    {seq1}")
print(f"  Rev : {seq_reverse2(seq1)}")
print(f"  Comp: {seq_complement2(seq1)}")
print(f"  Length: {seq_len2(seq1)}")
print(f"    A: {seq_count_base2(seq1, 'A')}")
print(f"    T: {seq_count_base2(seq1, 'T')}")
print(f"    C: {seq_count_base2(seq1, 'C')}")
print(f"    G: {seq_count_base2(seq1, 'G')}")
