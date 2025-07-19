def greet_user(list_of_people):
    for name in list_of_people:
        print(f"Hello, {name.title()}")

list_of_people = ['ram', 'shyam', 'hari', 'gita', 'sita']

greet_user(list_of_people)
