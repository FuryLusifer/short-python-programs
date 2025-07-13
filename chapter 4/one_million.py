# Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, 
# stop it by pressing CTRL-C or by closing the output window.)


# using list comprehension to insert values upto 1 million inside a list.
list_upto_milllion = [value for value in range(1,1000001)]

for i in list_upto_milllion:
    print(i)