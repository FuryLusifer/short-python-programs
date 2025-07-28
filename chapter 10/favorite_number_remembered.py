# Combine the two programs you wrote in Exercise 10-11 into one file. If the
# number is already stored, report the favorite number to the user. If not,
# prompt for the user’s favorite number and store it in a file.
# Run the program twice to see that it works.

from pathlib import Path
import json

file = Path("chapter 10/favorite numbers.json")

if file.exists():
    try:
        content = file.read_text()

    except FileNotFoundError:
        print(f"The file {file.name} could not be located.")

    else:
        fav_num = json.loads(content)
        print(f"Your favorite number: {fav_num}")

else:
    fav_num = input("What is your favorite number? ")
    content = json.dumps(fav_num)
    try:
        file.write_text(content)

    except FileNotFoundError:
        print(f"The file {file.name} could not be found.")

    else:
        print("We will remember your favorite number.")