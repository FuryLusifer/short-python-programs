my_pizzas = ["pepperoni", "margharita", "italian"]

friend_pizza = my_pizzas[:]

# printing the initial pizzas
print("My pizza\n", my_pizzas)
print("\nFriend's Pizza\n", friend_pizza)

# adding item to both lists

my_pizzas.append("chicken")
friend_pizza.append("chicago")

# printing both lists again
print("My pizza\n", my_pizzas)
print("\nFriend's Pizza\n", friend_pizza)
print()

# printing using loops

for i in my_pizzas:
    print(i, end = "  ")

print()
for i in range(len(friend_pizza)):
    print (friend_pizza[i], end = "  ")