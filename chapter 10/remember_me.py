from pathlib import Path
import json

username = input("What is your name?: ")

file = Path("chapter 10/usernames.json")
contents = json.dumps(username)
file.write_text(contents)

print(f"we will remember you when you come back, {username.title()}!")

