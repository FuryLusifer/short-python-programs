pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'chicken', 'pineapple']
}

print(f"You have ordered a pizza with {pizza['crust'].title()} crust "
      "And the toppings to put are:")

for topping in pizza['toppings']:
    print(f"{topping}")