prompt = "Enter the name of a city you have visited: "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}")