# Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_tshirt(size, message):
    '''prints the size and text to be printed in the tshirt.'''

    print(f"The size of the tshirt is '{size}' and the message to be printed is: \
          \n'{message}'")
    
make_tshirt("Large", "Manners Maketh Man")