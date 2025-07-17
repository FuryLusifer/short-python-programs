unconfirmed_users = ['ram', 'shyam', 'hari', 'sita', 'gita', 'rita']
confirmed_users = []

print("Unconfirmed users: ")
print(unconfirmed_users)
print("Confirmed users:")
print(confirmed_users)
# ********** Approach 1 (Recommended) **********
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying User: {current_user.title()}")
    confirmed_users.append(current_user)

print("List of Confirmed Users:")

for index, users in enumerate(confirmed_users, start = 1):
    print(f"{index}. {users.title()}")

# ********** Approach 2 **********

# while unconfirmed_users:
#     if unconfirmed_users:
#         current_user = unconfirmed_users[0]

#         print(f"Verifying User: {current_user.title()}")
#         confirmed_users.append(current_user)
#         unconfirmed_users.remove(unconfirmed_users[0])
    
#     else:
#         print("List empty !!!")

# print("List of Confirmed Users:")

# for index, users in enumerate(confirmed_users, start = 1):
#     print(f"{index}. {users.title()}")