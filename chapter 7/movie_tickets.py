# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free; if they are between
#  3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the 
# cost of their movie ticket.

while True:
    user_age = int(input("Enter your age: "))

    if user_age > 0 and user_age < 3:
        print(f"Your Ticket Price: $Free")
    
    elif user_age >= 3 and user_age <= 12:
        print("Your Ticket Price: $10")
    
    elif user_age > 12:
        print("Your Ticket Price: $15")
    
    else:
        print("Invalid Age")
        break