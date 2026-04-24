import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'
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

