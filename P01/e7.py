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


print("-----| Practice 1, Exercise 7 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f"Bases: {s1.count()}")
print(f"Rev: {s1.reverse()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"Bases: {s2.count()}")
print(f"Rev: {s2.reverse()}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f"Bases: {s3.count()}")
print(f"Rev: {s3.reverse()}")