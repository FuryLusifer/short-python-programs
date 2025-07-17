pets = ['cat', 'ant', 'rabbit', 'cat','mouse', 'cat']
print(pets)

# removing all instances of a pet in a list.
choice = input("Enter the pets name to be removed: ")

while choice.lower() in pets:
    pets.remove(choice.lower())

print(pets)