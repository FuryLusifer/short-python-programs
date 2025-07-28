# Wrap your code in a while loop so the user can continue entering numbers,
# even if they make a mistake and enter text instead of a number.

# ************ Approach 1 ************
while True:
    try:
        num1 = int(input("Enter the 1st number: "))
        num2 = int(input("Enter the 2nd number: "))
            
    except ValueError:
        print("Invalid Input.")
    
    else:
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        break

# ************ Approach 2 ************
# print("Enter 'q' at any time to quit.\n")

# while True:
#     try:
#         num1 = input("Enter the 1st number: ")
#         if num1.lower() == 'q':
#             break
#         num1 = int(num1)

#         num2 = input("Enter the 2nd number: ")
#         if num2.lower() == 'q':
#             break
#         num2 = int(num2)

#     except ValueError:
#         print("Invalid Input.")

#     else:
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")