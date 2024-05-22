GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

ACTORS = {
    'Robert De Niro': ['Meet the Parents'],
    'Ben Stiller': ['Meet the Parents'],
    'Adam Sandler': ['Anger Management'],
    'Jack Nicholson': ['Anger Management'],
    'Brendan Fraser': ['Mummy'],
    'Rachel Weisz': ['Mummy'],
    'Tom Cruise': ['Vanilla Sky', 'Mission Impossible'],
    'Penelope Cruz': ['Vanilla Sky'],
    'Cameron Diaz': ['Vanilla Sky'],
    'Brad Pitt': ['Meet Joe Black'],
    'Anthony Hopkins': ['Meet Joe Black'],
    'Jeremy Renner': ['Mission Impossible']
}

search_input = input('Search by Genre: ')

if search_input == 'y':
    print(f'Available Movies: {GENRES.keys()}\n')
    genre = input('Enter Genre: ')
    if GENRES.get(genre):
        print(f'Available Movies: {GENRES[genre]}\n')
        movie_by_genre = input('Enter Movie: ')
        if movie_by_genre in GENRES[genre]:
            print(f'Movie to watch: {movie_by_genre}. Genre: {genre}.\n')
        else:
            print('Movie was not found, try again.')
    else:
        print('Genre was not found, try again.')
elif search_input == 'n':
    search_input = input('Search by Actor: ')
    if search_input == 'y':
        print(f'Available Actors: {ACTORS.keys()}\n')
        actor = input('Enter Actor: ')
        if ACTORS.get(actor):
            print(f'Available Movies: {ACTORS[actor]} with {actor}\n')
            movie_by_actor = input('Enter Movie: ')
            if movie_by_actor in ACTORS[actor]:
                print(f'Movie to watch: {movie_by_actor}. Starring: {actor}.\n')
            else:
                print('Movie was not found, try again.')
        else:
            print('Actor was not found, try again.')
    else:
        print('There is no searching. Choose searching by Genre or Actor.')
else:
    print('Invalid search parameter. Try "y" or "n".')
