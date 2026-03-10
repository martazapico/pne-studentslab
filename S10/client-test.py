import termcolor

from P02.Client0 import Client

PORT = 8083
IP = "212.128.255.105"


c = Client(IP, PORT)

for i in range(5):

    message = f"Message {i}"
    termcolor.cprint(f"To server: {message} ", 'blue')
    response = c.talk(message)

    print(f"From Server: {response}")