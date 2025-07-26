# Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and 
# use your method to show its privileges.

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

class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
           privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges
    
    def show_privileges(self):
        print("\nAdmin has folllowing privileges:")
        for index, privilege in enumerate(self.privileges, start=1):
            print(f"{index}. {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, sex, education):
        super().__init__(first_name, last_name, age, sex, education)
        self.privileges = Privileges()

admin = Admin("random1", "random2", 25, "male", "bachelors")
admin.describe_user()
admin.privileges.show_privileges()
