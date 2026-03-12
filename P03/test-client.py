import termcolor
from P02.Client0 import Client

PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

#test 1
print("Test 1:")
message = "PING"
termcolor.cprint(f"To server: {message} ", 'blue')
response = c.talk(message)
print(response)

#test 2
print("Test 2:")
for i in range(5):
    message2 = f"GET {i}"
    print(f"To server: {message2} ")
    response = c.talk(message2)
    print(response)

#test 3
print("Test 3:")

message3 = "INFO AACCGTA"
termcolor.cprint(f"To server: {message3} ", 'blue')
response = c.talk(message3)
print(response)


#test 4
print("Test 4:")

message4 = "COMP AACCGTA"
termcolor.cprint(f"To server: {message4} ", 'blue')
response = c.talk(message4)
print(f"{response}")

