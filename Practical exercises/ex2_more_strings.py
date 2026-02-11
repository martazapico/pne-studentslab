text = "  Hello, World! Welcome to Python Programming.  "
#The string with leading and trailing spaces removed (use strip())
def strip(text):
    result = text.strip()
    result = text.replace(" ", "")
    return result
#The number of words in the string (use split())
def words(text):
    words = text.split()
    number = len(words)
    return number
#The string with the first letter of each word capitalized (use title())
def cap(text):
    result = text.title()
    return result
#Whether the stripped string starts with "Hello" (use startswith())
def starts(text):
    text = text.strip()
    result = text.startswith("Hello")
    return result
#Whether the stripped string ends with "ing." (use endswith())
def ends(text):
    text = text.strip()
    text = text.replace(".", "")
    result = text.endswith("ing")
    return result
#The position (index) of the word "Python" in the stripped string(use find())
def find(text):
    text = text.strip()
    result = text.find("Python")
    return result
#The words joined back together separated by " - " (use split() and " - ".join())
def joined(text):
    text = text.strip()
    text = text.split()
    result = " - ".join(text)
    return result

print("The string with leading and trailing spaces removed is:", strip(text))
print("The number of words in the string is:", words(text))
print("The string with the first letter of each word capitalized is:", cap(text))
print("Whether the stripped string starts with 'Hello' is:", starts(text))
print("Whether the stripped string ends with 'ing' is:", ends(text))
print("The position (index) of the word 'Python' in the stripped string is:", find(text))
print("The words joined back together separated by '-' is:", joined(text))