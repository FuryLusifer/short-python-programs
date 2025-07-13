user_list = ["Ram", "Shyam", "admin", "Hari"]
# user_list = []

if user_list:
    for user in user_list:
        if "admin" in user:
            print(f"Hello {user}, Would you like to see the status report?")
        else:
            print(f"Welcome, {user}")

else:
    print("We need to add some user")