# The final listing for remember_me.py assumes either that the user has already
# entered their username or that the program is running for the first time.
# We should modify it in case the current user is not the person who last used
# the program. Before printing a welcome back message in greet_user(), ask the
# user if this is the correct username. If it’s not, call get_new_username()
# to get the correct username.

from pathlib import Path
import json

def get_stored_username(file):
    """ Get stored username if available. """
    if file.exists():
        contents = file.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(file):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    file.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    file = Path('chapter 10/username.json')
    stored_username = get_stored_username(file)
    if stored_username:
        confirm = input(f"Is this your username: {stored_username}? (y/n): ").lower()
        if confirm == 'y':
            print(f"Welcome back, {stored_username}!")
        else:
            username = get_new_username(file)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(file)
        print(f"We'll remember you when you come back, {username}!")

greet_user()