class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
def print_seqs(seq_list):
    for i in seq_list:
        index = seq_list.index(i)
        length = i.len()
        sequence = i
        print(f"Sequence {index}: (Length: {length}) {i}")

print_seqs(seq_list)