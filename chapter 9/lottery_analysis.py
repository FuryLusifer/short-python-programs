# You can use a loop to see how hard it might be to win the kind of lottery
# you just modeled. Make a list or tuple called my_ticket. Write  a loop
# that keeps pulling numbers until your ticket wins. Print a message reporting
# how many times the loop had to run to give you a winning ticket.

from random import choice

class Lottery:
    """ Simulating a lottery roll """

    def __init__(self, no_of_roll=4):
        self.choice_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                             'a', 'e', 'i', 'o', 'u']
        self.no_of_roll = no_of_roll
        self.rolled_items = ""
        self.no_of_tries = 0

    def lottery_roll(self):
        self.no_of_tries +=1
        self.rolled_items = ""
        for _ in range(self.no_of_roll):
            self.rolled_items += str(choice(self.choice_pool))
        return self.rolled_items
    
    def winning_ticket(self):
        print(f"The winning Ticket is: {self.rolled_items}")


my_ticket = "12au"
user = Lottery()
while True:
    current_roll = user.lottery_roll()
    if current_roll == my_ticket:
        print(f"You won! Winning ticket: {current_roll}")
        print(f"Total attempts: {user.no_of_tries}")
        break