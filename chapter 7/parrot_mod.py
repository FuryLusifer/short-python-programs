prompt = "Keep entering things and i will repeat it back:\n" \
"if you want to stop enter 'quit': "

# ********** Method 1 **********
# message = ''
# while message != "quit":
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

flag = True

while flag:
    message = input(prompt)

    if message == 'quit':
        flag = False
    else:
        print(message)
