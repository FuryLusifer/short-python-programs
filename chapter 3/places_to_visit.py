print("original places")
places = ["Kathmandu", "New York", "Switzerland", "Bangkok", "Amsterdam"]
print(places)

print()
#temporarily sorts the list
print("Temporarily sorted lsit")
print(sorted(places))

#printing the original list
print("again original list")
print(places)

print()

#printing the list in reverse order using sorted(reverse = True)
print("temporarily sorted list in reverse order")
print(sorted(places, reverse=True))

#printing the original list
print("again original list")
print(places)

print()

#reversing the order of list
places.reverse()
print("reversed list")
print(places)
print("again original list by re-reversing")
places.reverse()
print(places)

print()

#sorting the list using sort() permanently
print("Using sort()")
places.sort()
print(places)
print()

#sorting the list in reverse alphabetical order using sort(reverse = True)
print("Using sort(reverse = True)")
places.sort(reverse = True)
print(places)
print()

#finding the length of list
print(f"i want to visit these {len(places)} places in my list")