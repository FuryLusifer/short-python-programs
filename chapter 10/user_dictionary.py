# The remember_me.py example only stores one piece of information, the username.
# Expand this example by asking for two more pieces of information about the
# user, then store all the information you collect in a dictionary. Write this
# dictionary to a file using json.dumps(), and read it back in using json.loads().
# Print a summary showing exactly what your program remembers about the user.

from pathlib import Path
import json

user_details = {}
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your age? "))

user_details['firstname'] = first_name
user_details['last_name'] = last_name
user_details['age'] = age

file = Path("chapter 10/username_details.json")
contents = json.dumps(user_details)

try:
    file.write_text(contents)

except FileNotFoundError:
    print("Could not locate the file.")

else:
    print(f"Your details have been saved, {user_details['firstname'].title()}!")
    choice = input("Do you want to view it (y or n)? ")
    if choice.lower() == 'y':
        content = file.read_text()
        data = json.loads(content)
        print(f"{user_details['firstname'].title()} {user_details['last_name'].
                title()}, you are {user_details['age']} years old.")
    else:
        exit()