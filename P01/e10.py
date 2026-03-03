from pathlib import Path

class Seq:

    def __init__(self, strbases=None):
        bases = {'A', 'T', 'G', 'C'}
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            for i in strbases:
                if i not in bases:
                    self.strbases = "ERROR"
                    print("INVALID sequence!")
                    return

            self.strbases = strbases
            print("New sequence created!")


    def __str__(self):
        return self.strbases


    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        a = file_contents.split("\n")
        body = a[1::]
        b = "".join(body).strip()
        self.strbases = b

    def gene_processing(self,):
        if self.strbases in ("NULL", "ERROR"):
            return "NONE"
        else:
            base = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
            for i in self.strbases:
                if i in base:
                    base[i] += 1
            max_value = max(base.values())
            for name, value in base.items():
                if value == max_value:
                    return name


print("-----| Practice 1, Exercise 10 |------")

FILENAME1 = "../S04/sequences/U5.txt"
FILENAME2 = "../S04/sequences/ADA.txt"
FILENAME3 = "../S04/sequences/FRAT1.txt"
FILENAME4 = "../S04/sequences/FXN.txt"
FILENAME5 = "../S04/sequences/RNU6_269P.txt"

s1 =Seq()
s2 =Seq()
s3 =Seq()
s4 =Seq()
s5 =Seq()

s1.read_fasta(FILENAME1)
s2.read_fasta(FILENAME2)
s3.read_fasta(FILENAME3)
s4.read_fasta(FILENAME4)
s5.read_fasta(FILENAME5)



print(f"Gene U5 : Most frequent Base:{s1.gene_processing()}")
print(f"Gene ADA : Most frequent Base:{s2.gene_processing()}")
print(f"Gene FRAT1 : Most frequent Base:{s3.gene_processing()}")
print(f"Gene FXN : Most frequent Base:{s4.gene_processing()}")
print(f"Gene RNU6_269P : Most frequent Base:{s5.gene_processing()}")
