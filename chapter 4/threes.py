# Make a list of the multiples of 3, from 3 to 30. 
# Use a for loop to print the numbers in your list.

sample_list = [value for value in range(3,31) if value%3==0]

for i in sample_list:
    print(i, end=" ")



# simple table print

# for i in range(1,11):
#     print("5 * ",i," = ", 5*i, end="\n")