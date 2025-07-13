simple_list = [value for value in range(1,100) if value<=50]

print("Initial list")
print(simple_list)

# slicing a list in various ways
# [1:10] = 1 is starting index and 10 is the number of values from that position
print("printing the slice, 2nd item to tenth item")
print(simple_list[1:10])
print()
print("printing the 1st ten items")
print(simple_list[:10])
print()
print("printing the items from index 5 to last ")
print(simple_list[5:])
print()
print("printing the whole list as a slice using [:]")
print(simple_list[:])

print()
# looping through a slice
print("printing the slice for 1st ten item using a loop")
for i in simple_list[0:10]:
    print(i, end=" ")

print()
# slicing and performing tasks
print("printing the first three items")
# printing the first three items
print(simple_list[0:3]) # this is simple slicing print
print("\n this is same as above just using a loop to get items")
for i in simple_list[0:3]:
    print(i, end = "\t")
print()

# printing the middle three items using loop
print("This is the middle three items from the list")
for i in simple_list[int((len(simple_list)/2)-1):int((len(simple_list)/2)+1)]: # dividing the list in half then starting
    print(i, end = "\t")  # from 1 position before it and ending one position after it
print()

# printing the last three items in the list
print("printing the last three items")
for i in simple_list[(len(simple_list)-3):]:
    print(i, end = "\t")