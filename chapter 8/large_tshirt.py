# Modify the make_shirt() function so that shirts are large by default with
# a message that reads I love Python. Make a large shirt and a medium shirt with
# the default message, and a shirt of any size with a different message.


def make_tshirt(size= "Large", message = "I Love Python."):
    '''prints the size and text to be printed in the tshirt.'''

    print(f"The size of the t-shirt is '{size}' and the message to be printed "
          f"is:\n'{message}'")
    
make_tshirt()
make_tshirt("Medium")
make_tshirt(size = "Medium")
make_tshirt(message = "I Love Rasbari.")
make_tshirt("Small", "Manners Mmaketh Man.")