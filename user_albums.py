#write a while loop that allows users to enter an album's artist and title. Print the dictionary and be sure to include a quit.

def make_album(artist, album_name):
    """Return an artist and album name, neatly formatted."""
    album = {'artist':artist, 'album_name':album_name}
    return album

while True:
    print("\nPlease tell me an artist and their album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break
    formatted_name = make_album(artist, album_name)
    print(formatted_name)