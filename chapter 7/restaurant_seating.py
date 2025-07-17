# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

guest_number = input("How many people are in your dinner group ?: ")

count = int(guest_number)

if count > 8:
    print("You'll have to wait.")

else:
    print("Your table is ready.")