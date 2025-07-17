# Write different versions of either Exercise 7-4 or 7-5 that do each of the
# following at least once:
#  • Use a conditional test in the while statement to stop the loop.
#  • Use an active variable to control how long the loop runs.
#  • Use a break statement to exit the loop when the user enters a 'quit' value.

# Use a conditional test in the while statement to stop the loop.
# while True:
#     topping = input("Enter a topping for your pizza: ")

#     if topping.lower() != "quit":
#         print(f"I will add {topping} to your pizza.")
#     else: 
#         break

# Use an active variable to control how long the loop runs.

# active = True

# while active:
#     topping = input("Enter a topping for your pizza: ")

#     if topping.lower() == "quit":
#         active = False
#     else: 
#         print(f"I will add {topping} to your pizza.")

# Use a break statement to exit the loop when the user enters a 'quit' value.

while True:
    user_age = input("Enter your age: ")

    if user_age.lower() == "quit":
        break

    else:
        user_age = int(user_age)
        if user_age > 0 and user_age < 3:
            print(f"Your Ticket Price: $Free")
        
        elif user_age >= 3 and user_age <= 12:
            print("Your Ticket Price: $10")
        
        elif user_age > 12:
            print("Your Ticket Price: $15")
        
        else:
            print("Invalid Age")
            break