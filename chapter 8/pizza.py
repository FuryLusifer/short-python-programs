def make_pizza(*toppings):
    '''printing the pizza as it is made.'''
    print("The pizza is being prepared with toppings: ")
    for index, topping in enumerate(toppings, start = 1):
        print(f"{index}. {topping.title()}")


make_pizza("pepperoni")
make_pizza("pepperoni", "tomato", "pineapple", "mushrooms")