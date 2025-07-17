# Write a function called make_album() that builds a dictionary describing
# a music album. The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store
# the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(name, title, no_of_songs = None):
    '''prints title, artist name and no. of songs in an album'''
    album = {'artist_name': name.title(), 'title': title.title()}

    if no_of_songs:
        album['no_of_song'] = no_of_songs

    return album

# calling function

print(make_album("piyush", "random"))
print(make_album("aaku", "random2"))
print(make_album("gaurab", "random3"))

print(make_album("piyush", "random",5))
print(make_album("aaku", "random2", 10))