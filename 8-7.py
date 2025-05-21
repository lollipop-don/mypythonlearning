def make_album(name, genre, number = None):
    album = {}
    album['name'] = name
    album['genre'] = genre
    if number:
        album['number'] = number
    return album
    
album = make_album('rihanna', 'pop', 13)
print(album)

album = make_album('mercury', 'rock')
print(album)