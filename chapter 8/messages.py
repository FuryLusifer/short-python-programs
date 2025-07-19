# Make a list containing a series of short text messages. Pass the list 
# to a function called show_messages(), which prints each text message.

def show_message(messages):
    '''prints message from a list.'''
    for msg in messages:
        print(f"{msg}")

messages = ['message 1', 'message 2', 'message 3']
show_message(messages)