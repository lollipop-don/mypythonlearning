def make_album(name, genre, number = None):
    album = {}
    album['name'] = name
    album['genre'] = genre
    if number:
        album['number'] = number
    return album


while True:
    name = input('artist name')
    genre = input('genre?')
    if name == 'quit' or genre == 'quit':
        break
    album = make_album(name, genre)
    print(album)



