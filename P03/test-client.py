import termcolor
from P02.Client0 import Client

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

print("-----| Practice 3, Exercise 7 |------")
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

#test 1
print("* Testing PING...")
message = "PING"
response = c.talk(message)
print(response)

#test 2
print("* Testing GET...")
for i in range(5):
    message2 = f"GET {i}"
    response = c.talk(message2)
    print(f"{message2}: {response}")
print("")

#test 3
print("* Testing INFO...")


message3 = "INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
response = c.talk(message3)
print(response)


#test 4
print("* Testing COMP...")

message4 = "COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(message4)
response = c.talk(message4)
print(f"{response}")
print("")


#test 5
print("* Testing REV...")

message5 = "REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
print(message5)
response = c.talk(message5)
print(f"{response}")
print("")


#test 6
print("* Testing GENE...")
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gene in gene_list:
    message6 = f"GENE {gene} "
    print(message6)
    response = c.talk(message6)
    print(f"{response}")
    print("")

