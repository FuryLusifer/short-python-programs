# ********** Import Approach 1 **********
# import pizza_module_demo

# pizza_module_demo.make_pizza(12,"pepperoni")
# pizza_module_demo.make_pizza(12,"pepperoni", "chicken")
# pizza_module_demo.make_pizza(12,"pepperoni", "margherita", "cheese")



# ********** Import Approach 2 **********
# from pizza_module_demo import make_pizza

# make_pizza(12,"pepperoni", "margherita", "cheese")



# ********** Import Approach 3 **********
# from pizza_module_demo import make_pizza as mp

# mp(12, "pepperoni", "margherita", "cheese")




# ********** Import Approach 4 **********
# import pizza_module_demo as pm

# pm.make_pizza(15, "pepperoni", "margherita", "cheese")




# ********** Import Approach 5 **********
from pizza_module_demo import *
make_pizza(10, "pepperoni", "margherita", "cheese")

