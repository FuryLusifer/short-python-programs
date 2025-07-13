# a tuple is a list whose value cannot be changed, immutable
# declaring a tuple. 
menu_items = ("momo", "chowmein", "sekuwa", "ice-cream")

for i in menu_items:
    print(i, end =" ")

# trying to modify an item in the tuple, it raised an error because tuple is 
# immutable so commenting it.
# menu_items[2] = "Rasbari"
# print(menu_items)

# changing the items in the tuple by redefining the tuple
menu_items = ("rasbari", "chowmein", "lalmohan", "ice-cream")
print("\nprinting the modified tuple")

for i in menu_items:
    print(i, end =" ")