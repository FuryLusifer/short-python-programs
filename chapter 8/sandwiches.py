# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwich that’s
# being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwiches(* ingredients):
    '''summarizes the preparation of a sandwich.'''
    print(f"Your sanwich is being prepared with: ")

    for value in ingredients:
        print(f"- {value.title()}")


make_sandwiches("chicken")
make_sandwiches("parmesan", "extra chicken")
make_sandwiches("mayonaise", "cabbage", "omellette")