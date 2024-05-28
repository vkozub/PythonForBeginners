"""Module Using functions"""

GENRES = {
    'comedy': ['Meet the Parents', 'Anger Management'],
    'adventures': ['Mummy'],
    'romantic': ['Vanilla Sky', 'Meet Joe Black'],
    'drama': ['Meet Joe Black'],
    'thriller': ['Vanilla Sky'],
    'action': ['Mission Impossible']
}

CAST = {
    'Meet the Parents': ['Robert De Niro', 'Ben Stiller'],
    'Anger Management': ['Adam Sandler', 'Jack Nicholson'],
    'Mummy': ['Brendan Fraser', 'Rachel Weisz'],
    'Vanilla Sky': ['Tom Cruise', 'Penelope Cruz', 'Cameron Diaz'],
    'Meet Joe Black': ['Brad Pitt', 'Anthony Hopkins'],
    'Mission Impossible': ['Tom Cruise', 'Jeremy Renner']
}

def search(source, source_name='genre'):
    """Function to search by source"""

    print(f'Available {source_name}(s): {source}\n')
    input_source = input(f'Enter {source_name}: ')
    while not input_source in source:
        print(f'The {source_name} was not found. Please try again.')
        input_source = input(f'Enter {source_name}: ')
    return input_source

def get_available_values(source):
    """Function to return list of unique values"""

    return set([item for sublist in source.values() for item in sublist])

def find_movies_by_actor(actor_name, cast):
    """Function to return list of movies by actor"""

    movies = []
    for film, roles in cast.items():
        if actor_name in roles:
            movies.append(film)
    print(f'Available Movies: {movies} with {actor_name}\n')
    return movies

# ----------------------------------------------------------------

search_input = input('Search by Genre: ')

if search_input == 'y':
    # Find genre
    genre = search(list(GENRES.keys()))
    # Find movie by genre
    movie_by_genre = search(GENRES[genre], 'movie')

    print(f'Movie to watch: {movie_by_genre}. Genre: {genre}.\n')
elif search_input == 'n':
    search_input = input('Search by Actor: ')
    if search_input == 'y':
        # Get available actors
        available_actors = get_available_values(CAST)

        # Find actor
        actor = search(available_actors, 'actor')

        # find films with actor
        available_movies_with_actor = find_movies_by_actor(actor, CAST)

        # Find movie by actor
        movie_by_actor = search(available_movies_with_actor, 'movie')
        print(f'Movie to watch: {movie_by_actor}. Starring: {actor}.\n')
    else:
        print('There is no searching. Choose searching by Genre or Actor.')
else:
    print('Invalid search parameter. Try "y" or "n".')
