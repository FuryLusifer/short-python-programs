# An ice cream stand is a specific kind of restaurant. Write a class called
# IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the 
# class will work; just pick the one you like better. Add an attribute called 
# flavors that stores a list of ice cream flavors. Write a method that displays 
# these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """ Modeling a simple restaurant. """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} restaurant serves delicious "
              f"{self.cuisine_type} dishes.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open to serve!!!")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

# creating IceCreamStand Class and inheriting Restaurant Class.

class IceCreamStand(Restaurant):
    """ An ice cream stand is a specific kind of restaurant called
        IceCreamStand that inherits from the Restaurant class """
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def list_flavors(self):
        print("\nThe flavors we have available are:")
        for index, flavor in enumerate(self.flavors, start=1):
            print(f"{index}. {flavor.title()}")


# creating instance of IceCreamStand
icecreams = IceCreamStand("ABC", "Ice-creams")
icecreams.flavors = ['Chocolate', 'Cookies and cream', 'Mint chocolate chip',
                     'Vanilla', 'Butter pecan', 'Coconut milk', 'Pistachio',
                     'Strawberry']

icecreams.list_flavors()