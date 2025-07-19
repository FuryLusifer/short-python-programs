# Start with a copy of your program from Exercise 8-9. Write a function called
# send_messages() that prints each text message and moves each message to a new
# list called sent_messages as it’s printed. After calling the function,
# print both of your lists to make sure the messages were moved correctly.

def send_messages(unsent_messages, sent_messages):
    '''prints message from a list and moves it to sent_list.'''
    while unsent_messages:
        current_message = unsent_messages.pop(0)
        print(f"Sending... {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['message 1', 'message 2', 'message 3']
sent_messages = []
print("Before calling the function:")
print(f"Unsent Messages: {unsent_messages}")
print(f"Sent Message: {sent_messages}")

send_messages(unsent_messages, sent_messages)

print("After calling the function:")
print(f"Unsent Messages: {unsent_messages}")
print(f"Sent Messages: {sent_messages}")