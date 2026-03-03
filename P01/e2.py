class Seq:

    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
        else:
            self.strbases = strbases
            print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

print("-----| Practice 1, Exercise 2 |------")
s1 = Seq()
s2 = Seq("TATAC")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")