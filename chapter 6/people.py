# People: Start with the program you wrote for Exercise 6-1 (page 98). Make two 
# new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_1 = {
    "first_name": "piyush",
    "last_name": "karn",
    "age": 25,
    "city": "janakpur",
}

person_2 = {
    "first_name": "aakriti",
    "last_name": "acharya",
    "age": 25,
    "city": "hetauda"
}

person_3 = {
    "first_name": "gaurab",
    "last_name": "karn",
    "age": 24,
    "city": "mahendranagar"
}

people = [person_1, person_2, person_3]
i = 0
for human in people:
    i += 1
    print(f"""Person {i}:
    First Name: {human['first_name'].title()}
    Last Name: {human['last_name'].title()}
    Age : {human['age']}
    City: {human['city'].title()}
""")