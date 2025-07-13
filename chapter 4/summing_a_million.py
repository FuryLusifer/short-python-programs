# Make a list of the numbers from one to one million, and then use min() and max
# () to make sure your list actually starts at one and end sat one million.Also,
# use the sum() function to see how quickly Python can add a million numbers.

list_upto_million = [value for value in range(1,1000001)]

print(min(list_upto_million))
print(max(list_upto_million))
print(sum(list_upto_million))