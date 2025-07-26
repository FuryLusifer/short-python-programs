# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message
# saying that any ticket matching these 4 numbers or letters wins a prize.

from random import choice

class Lottery:
    """ Simulating a lottery roll """

    def __init__(self, no_of_roll=4):
        self.choice_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                             'a', 'e', 'i', 'o', 'u']
        self.no_of_roll = no_of_roll
        self.rolled_items = ""

    def lottery_roll(self):
        for i in range(self.no_of_roll):
            self.rolled_items += str(choice(self.choice_pool))
    
    def winning_ticket(self):
        print(f"The winning Ticket is: {self.rolled_items}")


user1 = Lottery(5)
user1.lottery_roll()
user1.winning_ticket()