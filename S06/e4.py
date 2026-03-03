import termcolor

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list, color):
    for i in seq_list:
        index = seq_list.index(i)
        length = i.len()
        sequence = i
        termcolor.cprint(f"Sequence {index}: (Length: {length}) {sequence}", color)



def generate_seqs(pattern, number):
    list_a = []
    for i in range(1, number + 1):
        letter = pattern * i
        list_a.append(Seq(letter))
    return list_a


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint('List 1:', 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint('List 2:', 'green')
print_seqs(seq_list2, 'green')