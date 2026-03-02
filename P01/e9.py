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

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            count = 0
            for i in self.strbases:
                if base == i:
                    count += 1
        return count

    def count(self):
        bases = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return bases
        else:
            for i in self.strbases:
                if i in bases:
                    bases[i] += 1
            return bases

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            return self.strbases[::-1]
    def complement(self):
        bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"

        else:
            result = ""
            for i in self.strbases:
                if i in bases:
                    result += bases[i]
            return result

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        a = file_contents.split("\n")
        body = a[1::]
        b = "".join(body).strip()
        self.strbases = b


print("-----| Practice 1, Exercise 9 |------")

FILENAME = "../S04/sequences/U5.txt"

s =Seq()
s.read_fasta(FILENAME)

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Comp: {s.complement()}")

