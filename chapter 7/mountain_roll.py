responses = {}

# setting to a flag to indicate poll is active

poll_status = True

while poll_status:
    name = input("What is your name: ")
    mountain = input(
        f"What mountain would you like to climb today, {name.title()}: "
        )
    # storing the responses in the dictionary
    responses[name] = mountain

    # checking for another person to take the poll.
    choice = input(
        f"Would someone else like to take the poll (Y or N): "
    )

    if choice.lower() == 'n':
        poll_status = False

# showing total responses
print("********** Poll Results **********")
for name,response in responses.items():
    print(f"{name.title()} would like to climb mountain {response}.")