# Add an attribute called login_attempts to your User class from Exercise 9-3 
# (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). Print 
# login_attempts again to make sure it was reset to 0.

class User:
    """ Simualting a user info class"""
    def __init__(self, first_name, last_name, age, sex, education):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.sex = sex.title()
        self.education = education.title()
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User {self.first_name} {self.last_name} is {self.age} years old"
              f", {self.sex}. they have studied till {self.education}.")
        
    def greet_user(self):
        print(f"Hello user, {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("piyush", "Kayastha", 25, "male", "graduate")

print(f"Login Attempts: {user1.login_attempts}")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"\nLogin Attempts: {user1.login_attempts}")

print("\nReseting login attempts...")
user1.reset_login_attempts()
print(f"Login Attempts: {user1.login_attempts}")
