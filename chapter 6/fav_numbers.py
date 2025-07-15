# Modify your program from Exercise 6-2 (page 98) so each person can
# have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {
    'ram': [1, 2, 3,],
    'shyam': [3,4,5,],
    'hari': [6, 7, 8,],
    'sita': [8, 9, 10, 11],
    'rita': [34, 24, 55, 87],
}

print("The favorite numbers of my friends are:")

# ************* Method 1 *************
# i = 1
# for key,value in favorite_numbers.items():
#     print(f"{i}. {key.title()}:")
#     for val in value:
#         print(f"\t{val}", end=' ')

#     i += 1
#     print()


# ************* Method 2 *************
# for index,(key,value) in enumerate(favorite_numbers.items(), start = 1):
#     print(f"{index}. {key.title()}:")
#     print("\t", end = "")

#     for val in value:
#         print(val, end = " ")
#     print()

# ************* Method 3 *************
for index, (key,value) in enumerate(favorite_numbers.items(), start = 1):
    fav_nums = " ".join(str(val) for val in value)
    print(f"{index}. {key.title()}: {fav_nums}")
    print()



