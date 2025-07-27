from pathlib import Path

file = Path("chapter 10/pi_million_digits.txt")
contents = file.read_text()

bday = input("Input your birthday in format ddmmyy: ")
if bday in contents:
    print("Your bithdate has been found.")
    print("Found at index:", contents.find(bday))

else:
    print("Your bday could not be found.")