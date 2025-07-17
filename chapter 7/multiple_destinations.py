# same program as dream_vacation.py but one person can choose multiple places.

destinations = {}

polling_active = True

while polling_active:
    name = input("What is your name?: ")
    destinations[name] = []

    print("Enter places you would like to visit.")
    print("Type done when you are finished.")

    while True:
        place = input().strip().title()
        if place.lower() == "done":
            break
        destinations[name].append(place)

    choice = input("would someone else like to take the poll? (Y or N): ")
    if choice.lower() == "n":
        polling_active = False

print("\nPolling Results:\n")
for name, place in destinations.items():
    print(f"{name.title()} would like to visit: ", end = "")
    print(", ".join(place))