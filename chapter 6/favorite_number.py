favorite_numbers = {'ram': 7,
                    'Shyam': 15,
                    'hari': 28,
                    'Rita': 45,
                    'Sita': 99,
                    }

print(favorite_numbers)

# printing the results:

rita_number = favorite_numbers['Rita']
sita_number = favorite_numbers.get("Sita", "NO DATA.")

print(f"""The favorite numbers of my friends are:
Ram: {favorite_numbers.get('ram', "No such friend")}
Shyam: {favorite_numbers.get("Shyam", "No such Friend.")}
Ramesh: {favorite_numbers.get("Ramesh", "No Such Friend.")}
Hari: {favorite_numbers.get("hari", "No data available.")}
Rita: {rita_number}
Sita: {sita_number} """)

# using loops

for key,value in favorite_numbers.items():
    print(f"Mr. {key.title()}'s Favorite Number is {value}.")