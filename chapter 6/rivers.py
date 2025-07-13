rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'bagmati': 'nepal',
}

# printing a statement using key value pair.
for key,value in rivers.items():
    print(f"The {key.title()} river runs through {value.title()}.")

# printing only the keys.
print(f"\nThe rivers are:")
for key in rivers.keys():
    print(f"\t{key.upper()}.")

# printing only the values.
print(f"The countries are:")
for value in rivers.values():
    print(f"\t{value.capitalize()}.")