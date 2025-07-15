# Make several dictionaries, where each dictionary represents a different pet.
# In  each dictionary, include the kind of animal and the owner’s name. Store
# these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1 = {
    'animal': 'cat',
    'owner': 'gaurab',
}

pet_2 = {
    'animal': 'dog',
    'owner': 'aakriti',
}

pet_3 = {
    'animal': 'hamster',
    'owner': 'ram',
}

pet_4 = {
    'animal': 'rabbit',
    'owner': 'shyam',
}

pet_5 = {
    'animal': 'snake',
    'owner': 'ramesh',
}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for count,pet in enumerate(pets, start = 1):
    print(f"Pet {count}:")
    print(f"\tAnimal: {pet['animal'].title()}")
    print(f"\tOwner : {pet['owner'].title()}\n")