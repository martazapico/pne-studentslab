class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    for i in seq_list:
        index = seq_list.index(i)
        length = i.len()
        sequence = i
        print(f"Sequence {index}: (Length: {length}) {sequence}")



def generate_seqs(pattern, number):
    list_a = []
    for i in range(1, number + 1):
        letter = pattern * i
        list_a.append(Seq(letter))
    return list_a


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
