import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
people1 = person['people']
print(f"Total people in the database: {len(people1)}")
for i, people2 in enumerate(people1):
    # Print the information on the console, in colors
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(people2['Firstname'], people2['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(people2['age'])

    # Get the phoneNumber list
    phoneNumbers = people2['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    count1 = 0
    # Print all the numbers
    for num in phoneNumbers:
        count1 += 1
        termcolor.cprint(f"\tPhone {count1 -1}: ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t\t- Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("\t\t- Number: ", 'red', end='')
        print(num['number'])

    count1 = 0
