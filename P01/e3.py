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
        return len(self.strbases)

print("-----| Practice 1, Exercise 3 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Sequence 3: {s3}")