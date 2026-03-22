import termcolor

from P02.Client0 import Client


PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)

print("-----| Practice 3, Exercise 7 |------")
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

#test 1
print("* Testing PING...")
message = "Hello"
response = c.talk(message)
print(response)

#