def make_album(name, genre):
    album = {}
    album['name'] = name
    album['genre'] = genre
    return album
    
album = make_album('rihanna', 'pop')
print(album)

album = make_album('mercury', 'rock')
print(album)