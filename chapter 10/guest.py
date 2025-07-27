# Write a program that prompts the user for their name. When
# they respond, write their name to a file called guest.txt.

from pathlib import Path

guest_list = Path("chapter 10/guest.txt")

names = ''
# getting the names of guest.
while True:
    guest_name = input("What is your name? (press q for quit): ")
    if guest_name.lower() == 'q':
        break

    names += f"{guest_name}\n"

guest_list.write_text(names.title().strip())