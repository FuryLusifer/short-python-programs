# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

sandwich_orders = ['Grilled cheese','Club', 'Cuban','Italian Beef', 'Reuben'
                   ,'Ham and cheese', 'Breakfast','Chicken', 'Egg salad']

finished_sandwiches = []

# printing the current status of sandwiches.
print("Current status of Sandwiches:")
print(f"Sandwich Orders: {sandwich_orders}")
print(f"Finished Sandwiches: {finished_sandwiches}")

# Removing one sandwich and adding it to finished list.
while sandwich_orders:
    # aproach 1
    # current_order = sandwich_orders[0]  # taking the first sandwich.
    # sandwich_orders.remove(sandwich_orders[0]) # removing from unfinished list.

    # approach 2
    current_order = sandwich_orders.pop(0)
    finished_sandwiches.append(current_order) # adding it to finished list.

    print(f" I made your {current_order}.") #printing the current order.


print("\nThe finished sandwiches are: ")
for index, sandwich in enumerate(finished_sandwiches, start = 1):
    print(f"{index}. {sandwich}")