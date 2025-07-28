# Make two files, cats.txt and dogs.txt. Store at least three names of cats
# in the first file and three names of dogs in the second file. Write a program 
# that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a
# different location on your system, and make sure the code in the except block
# executes properly.

# Modify your except block in Exercise 10-7 to fail
# silently if either file is missing.

from pathlib import Path

def file_reader(animal, filename):
    file = Path(f"chapter 10/{filename}")
    try:
        content = file.read_text().splitlines()
    except FileNotFoundError:
        # print(f"The file {file.name} could not be found.") #approach 1
        pass   # Approach 2
    else:
        print(f"The name of {animal} are:")
        for index, name in enumerate(content, start=1):
            print(f"{index}. {name.title()}")
        print()


# calling the function
file_reader('cats', 'cats.txt')
file_reader("dogs", "dogs.txt")
