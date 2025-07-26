# Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_die() that prints a
# random number between 1 and the number of sides the die has. Make a 
# 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """Modeling a basic die """
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)
    
# Make a 6-sided die and roll it 10 times.
six_sided_die = Die(6)  # can also be Die() because default side = 6.
print()
for i in range(10):
    print(f"{i+1}. you have rolled a {six_sided_die.roll_die()}")

# Make a 10-sided die and roll it 10 times.
ten_sided_die = Die(10)
print()
for index, _ in enumerate(range(10), start=1):
    print(f"{index}. You have rolled a {ten_sided_die.roll_die()}")

# Make a 20-sided die and roll it 10 times.
twenty_sided_die = Die(20)
print()
for index, _ in enumerate(range(10), start=1):
    print(f"{index}. You have rolled a {twenty_sided_die.roll_die()}")