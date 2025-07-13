current_users = ["Ram", "Shyam", "Hari", "Sita", "Rita"]

new_users = ["Gita", "Hari", "Aaku", "Ram", "Binita"]

current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)


for users in new_users:
    if users.lower() in current_users_lower:
        print(f"Username: {users} has already been used. Choose new !!!")
    else:
        print(f"Username: {users} is available.")