# Make a class called User. Create two attributes called first_name and 
# last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User:
    """ Simualting a user info class"""
    def __init__(self, first_name, last_name, age, sex, education):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.education = education.title()
    
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} is {self.age} years old"
              f", {self.sex}. they have studied till {self.education}.")
        
    def greet_user(self):
        print(f"Hello user, {self.first_name} {self.last_name}.")

user1 = User("piyush", "karn", 25, "male", "graduate")
user2 = User("aaku", "kallu", 24, "female", "Under-graduate")
user3 = User("gaurab", "karn", 23, "male", "intermediate")

# *************** User 1 ***************
user1.greet_user()
user1.describe_user()

# *************** User 2 ***************
user2.greet_user()
user2.describe_user()

# *************** User 3 ***************
user3.greet_user()
user3.describe_user()