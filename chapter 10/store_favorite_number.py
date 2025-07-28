# Write a program that prompts for the user’s favorite number. Use json.dumps()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message “I know your favorite number! It’s _____.”

from pathlib import Path
import json

fav_num = input("What is your favorite number? ")
file = Path("chapter 10/favorite numbers.json")
content = json.dumps(fav_num)
try:
    file.write_text(content)

except FileNotFoundError:
    print(f"The file {file.name} could not be found.")

else:
    print("We will remember your favorite number.")