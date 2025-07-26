# An administrator is a special kind of user. Write a class called Admin
#  that inherits from the User class you wrote in Exercise 9-3 (page 162) or
# Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
# strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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


# class Admin that inherits from the User class

class Admin(User):

    def __init__(self, first_name, last_name, age, sex, education):
        super().__init__(first_name, last_name, age, sex, education)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print("\nAdmin has folllowing privileges:")
        for index, privilege in enumerate(self.privileges, start=1):
            print(f"{index}. {privilege}")


admin = Admin("random1", "random2", 25, "male", "bachelors")

admin.describe_user()
admin.show_privileges()