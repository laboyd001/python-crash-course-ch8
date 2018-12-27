#write a function called make_album that builds a dictionary containing a music album.  The function should take the artists name and the album title and return a dictionary containing these two pieces of info.  Use the function to make 3 dictionaries.

# make an optional parameter that stores the number of tracks

def make_album(artist, album_name, tracks=''):
    """Return a dictionary of info about an album."""
    album = {'artist':artist, 'album_name':album_name}
    if tracks:
        album['tracks'] = tracks
    return album

album_info = make_album('radiohead', 'the bends', tracks='13')
print(album_info)
album_info = make_album('coldplay', 'rush of blood to the head')
print(album_info)