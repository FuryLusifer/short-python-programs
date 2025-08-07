# Write a class called Employee. The __init__() method should take in a first
# name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.

class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    # def give_raise(self):
    #     amount = input("Enter raise amount (d for default $5000 raise): ")
    #     if amount.lower() == 'd':
    #         total_salary = self.annual_salary + 5000
    #         print(f"{self.first_name.title()} {self.last_name.title()}, " 
    #               f" your annual salary of {self.annual_salary} has been raised"
    #               f" by $5000 and it is now {total_salary}."
    #               )
            
    #     else:
    #         total_salary = self.annual_salary + float(amount)
    #         print(f"{self.first_name.title()} {self.last_name.title()}, " 
    #               f" your annual salary of {self.annual_salary} has been raised"
    #               f" by ${amount} and it is now {total_salary:.2f}."
    #               )

    def give_raise(self, raise_amount=5000):
        self.annual_salary += raise_amount
        return self.annual_salary