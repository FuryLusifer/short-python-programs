# A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
# (that is, the cube of each integer from 1 through 10), and use a for loop to 
# print out the value of each cube.

list_of_cube = []

for i in range(1,11):
    list_of_cube.append(i**3)

print(list_of_cube)

for i in range(len(list_of_cube)):
    print(list_of_cube[i], end=" ")