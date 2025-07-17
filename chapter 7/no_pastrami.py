# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['Grilled cheese', 'pastrami', 'Club', 'Cuban' 
                   ,'Italian Beef', 'pastrami', 'Reuben', 'pastrami'
                   , 'Ham and cheese', 'pastrami', 'Egg salad'
                   , 'Breakfast','Chicken', 'pastrami']

finished_sandwiches = []

print("Sorry! We have run out of Pastrami sanwiches.\n")

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    if current_order.lower() == "pastrami":
        continue
    print(f"Preparing: {current_order} Sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe finished sandwiches are: ")
for index, sandwich in enumerate(finished_sandwiches, start = 1):
    print(f"{index}. {sandwich}")