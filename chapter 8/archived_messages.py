# Start with your work from Exercise 8-10. Call the function send_messages()
# with a copy of the list of messages. After calling the function, print both
# of your lists to show that the original list has retained its messages.

def send_messages(unsent_messages, sent_messages):
    '''prints message from a copy of a list and moves it to sent_list.'''
    while unsent_messages:
        current_message = unsent_messages.pop(0)
        print(f"Sending... {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['message 1', 'message 2', 'message 3']
sent_messages = []
print("Before calling the function:")
print(f"Unsent Messages: {unsent_messages}")
print(f"Sent Message: {sent_messages}")

send_messages(unsent_messages[:], sent_messages)

print("After calling the function:")
print(f"Unsent Messages: {unsent_messages}")
print(f"Sent Messages: {sent_messages}")