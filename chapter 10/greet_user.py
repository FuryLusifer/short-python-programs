from pathlib import Path
import json

# file = Path("chapter 10/usernames.json")
# content = file.read_text().title()

# username = json.loads(content)

# print(f"welcome back, {username}!")

# a little more than above.

file = Path("chapter 10/usernames.json")

if file.exists():
    content = file.read_text().title()
    username = json.loads(content)
    print(f"welcome back, {username}!")

else:
    username = input("What is your name? ")
    content = json.dumps(username)
    file.write_text(content)

    print(f"We will remember you when you come back, {username}!")