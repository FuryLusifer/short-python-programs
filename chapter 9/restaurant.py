# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant:
    """ Modeling a simple restaurant. """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type}"
              " dishes")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now OPEN !!!")


# *************** Exercise 9.1 ***************
# printing both attributes indvidually.
# my_restaurant = Restaurant("ABC Restaurant", "Traditional Nepali")

# print(f"My restaurant's name is {my_restaurant.restaurant_name}")
# print(f"Availabe Cuisine Type: {my_restaurant.cuisine_type}")

# # calling both methods.
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# ********************************************


# *************** Exercise 9.2 ***************

restaurant1 = Restaurant("ABC Restaurant", "Traditional Nepali")
restaurant2 = Restaurant("DEF Restaurant", "Indian")
restaurant3 = Restaurant("GHI Restaurant", "Continental")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
