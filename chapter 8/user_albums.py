# Start with your program from Exercise 8-7. Write a while loop that
# allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(name, title, no_of_songs = None):
    '''prints title, artist name and no. of songs in an album'''
    album = {'artist_name': name.title(), 'title': title.title()}

    if no_of_songs:
        album['no_of_song'] = no_of_songs

    return album

# calling function
while True:
    print("Start entering details (q to quit)")
    name = input("Enter the name of artist: ")
    if name.lower() == 'q':
        break 
    title = input("Enter the title of album: ")
    if title.lower() == 'q':
        break
    print(make_album(name, title))