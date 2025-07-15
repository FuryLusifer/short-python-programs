# Make a dictionary called favorite_places. Think of three names to use
#  as keys in the dictionary, and store one to three favorite places for
# each person. To make this exercise a bit more interesting, ask some friends to
# name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places.

favorite_places = {
    'gaurab': ['bangkok', 'california', 'las vegas'],
    'aaku': ['janakpur', 'paris', 'london'],
    'piyush': ['malaysia', 'maldives', 'malta']
}

for key,value in favorite_places.items():
    print(f"Favourite Places of {key.title()} are:")
    for places in value:
        print(f"{places}", end=" ")
    print("\n")