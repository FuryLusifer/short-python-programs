# Write a program that polls users about their dream vacation. Write a prompt
# similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

destinations = {}

polling_active = True
while polling_active:
    name = input("What is your name?: ")
    place = input(f"Where would you like to visit, {name.title()}?: ")
    destinations[name] = place

    choice = input("would someone else like to take the poll? (Y or N): ")
    if choice.lower() == "n":
        polling_active = False

print("\nPolling Results:\n")
for name, place in destinations.items():
    print(f"{name.title()} would like to visit {place.title()}.")