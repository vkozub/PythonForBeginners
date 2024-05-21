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

# Part 1. If statement
print('Part 1. If statement. Searching by Genre.\n')

genre = input('Search by Genre: ')

if GENRES.get(genre, None):
    print(f'Available Movies: {GENRES[genre]}\n')
    movie_by_genre = input('Enter Movie: ')
else:
    print(f'Available Genres: {GENRES.keys()}\n')
    genre = input('Enter Genre: ')
    print(f'Available Movies: {GENRES[genre]}\n')
    movie_by_genre = input('Enter Movie: ')

print(f'Movie to watch: {movie_by_genre}. Genre: {genre}.\n')

print('Part 1. If statement. Searching by Actor.\n')

actor = input('Search by Actor: ')

if ACTORS.get(actor, None):
    print(f'Available Movies: {ACTORS[actor]}\n')
    movie_by_actor = input('Enter Movie: ')
else:
    print(f'Available Actors: {ACTORS.keys()}\n')
    actor = input('Enter Actor: ')
    print(f'Available Movies: {ACTORS[actor]} with {actor}\n')
    movie_by_actor = input('Enter Movie: ')

print(f'Movie to watch: {movie_by_actor}. Starring: {actor}.\n')
