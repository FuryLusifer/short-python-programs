favorite_numbers = {'ram': 7,
                    'shyam': 15,
                    'hari': 28,
                    'rita': 45,
                    'sita': 99,
                    }

candidates = ['ram', 'ramesh', 'rita', 'aakriti', 'piyush', 'sita', 'shyam',]

for person in candidates:
    if person.lower() in favorite_numbers:
        print(f"Thanks Mr. {person.title()} for taking the poll.")
    else:
        print(f"Mr. {person.title()}, please take the poll ASAP.")