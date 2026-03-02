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


print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f"A: {s1.count_base('A')}, C: {s1.count_base('C')}, T: {s1.count_base('T')}, G: {s1.count_base('G')}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"A: {s2.count_base('A')}, C: {s2.count_base('C')}, T: {s2.count_base('T')}, G: {s2.count_base('G')}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f"A: {s3.count_base('A')}, C: {s3.count_base('C')}, T: {s3.count_base('T')}, G: {s3.count_base('G')}")