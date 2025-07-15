# Make a dictionary called cities. Use the names of three cities as keys in
# your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one 
# fact about that city. The keys for each city’s dictionary should be something 
# like country, population, and fact. Print the name of each city and all of
# the information you have stored about it.

cities = {
    'kathmandu': {
        'country': 'Nepal',
        'population': 1500000,
        'fact': 'Capital city of Nepal.'
    },
    'bangkok': {
        'country': 'Thailand',
        'population': 2500000,
        'fact': 'Tourism hub of Thailand.'
    },
    'Los Angeles': {
        'country': 'United States of America',
        'population': 5000000,
        'fact': 'Home of Hollywood.'
    }
}

# ********** Method 1 **********
# for index, (key,value) in enumerate(cities.items(), start = 1):
#     print(f"{index}. {key.title()}")

#     for fact,details in value.items():
#         print(f"\t{fact.title()}: {details}")
#     print()

# ********** Method 2 **********

for index, (key,value) in enumerate(cities.items(), start = 1):
    print(f"{index}. {key.title()}")
    print(f"\tCountry: {value['country']}")
    print(f"\tPopulation: {value['population']}")
    print(f"\tFact: {value['fact']}")
