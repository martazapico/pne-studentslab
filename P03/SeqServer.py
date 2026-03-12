import termcolor
import socket
from P01.Seq1_new_version import Seq




PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured!")
count = 0

while True:
    count += 1
    # -- Waits for a client to connect
    print("Waiting for clients....")
    (cs, client_ip_port) = ls.accept()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()


    #Exercise 1: PING
    if msg.strip() == "PING":
    # -- Print the received message
        termcolor.cprint("PING command!", 'green')

        # -- Send a response message to the client
        response = "OK!\n"
        print("OK!\n")

    # -- The message has to be encoded into bytes
        cs.send(response.encode())

    # Exercise 2: GET
    elif "GET" in msg.strip():
        number = [0, 1, 2, 3, 4]
        sequence = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "GGGTGTGTGTTAGTGTGCGTGCTTGCTTGTGTGTGGAAGAAACCAACAGGGTTCACGCTG", "CGGCTCCCGCGGCTGCAGGCGCGCGGCTAGAGTGCCTGGCGGGCTCCGGCTTCCGCGTCC", "ATCCCGCAGCCGCTGTCGGGTCCGTGCCGGCGAGGATGGCTCCGGGGCGCCGCCGCCTCC"]
        # -- Print the received message
        termcolor.cprint("GET", 'green')
        for i in number:
            i = str(i)
            if i in msg:
                i = int(i)
                response = f"{sequence[i]}\n"

        # -- Send a response message to the client

        print(response)

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # Exercise 3: INFO
    elif "INFO" in msg.strip():
        termcolor.cprint("INFO", 'green')
        first = msg.split()
        sequence = str(first[-1])
        s = Seq(sequence)
        length = s.len()
        response = ""
        a = f"Sequence: {sequence}\n"
        response += a

        b = f"Total length: {length}\n"
        response += b


        list_bases = s.count()
        for base, numb in list_bases.items():
            percentage = (numb/length)* 100
            percentage = round(percentage, 1)
            c =f"{base}: {numb} ({percentage}%)\n"
            response += c
        cs.send(response.encode())

        print(response)

     # Exercise 4: COMP
    elif "COMP" in msg.strip():
        termcolor.cprint("COMP", 'green')
        first = msg.split()
        sequence = str(first[-1])
        s = Seq(sequence)

        response2 = s.complement()

        cs.send(response2.encode())
        # -- Print the received message

        # -- Send a response message to the client

        print(f"{response2}\n")


     # Exercise 4: COMP
    elif "REV" in msg.strip():
        termcolor.cprint("REV", 'green')
        first = msg.split()
        sequence = str(first[-1])
        s = Seq(sequence)

        response2 = s.reverse()

        cs.send(response2.encode())
        # -- Print the received message

        # -- Send a response message to the client

        print(f"{response2}\n")




    # -- Close the data socket
    cs.close()


