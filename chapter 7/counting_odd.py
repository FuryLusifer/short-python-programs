current_number = 0

# printing even numbers and using break to limit loop.
# flag = True
# while True:
#     current_number += 1
#     if(current_number % 2 == 0):
#         print(current_number, end = " ")
    
#     else:
#         if current_number > 10:
#             break


# will use continue to print odd numbers till 20.

while current_number < 20:
    current_number += 1
    if (current_number % 2 == 0):
        continue

    print(current_number, end = " ")