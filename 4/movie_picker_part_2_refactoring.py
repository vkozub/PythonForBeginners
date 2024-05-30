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

PG = {
    13: {'Meet the Parents', 'Anger Management', 'Mummy', 'Meet Joe Black', 'Mission Impossible'},
    16: {'Vanilla Sky'}
}

# ----------------------------------------------------------------Methods---------------------------------------------

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

def is_integer(string):
    """Verify if string is an integer"""

    try:
        integer = int(string)
        return isinstance(integer, int)
    except ValueError:
        return False

def get_movies_based_on_pg_rate(pg_rate):
    """Get movies based on pg_rate"""

    get_pg_keys = list(PG.keys())
    allowed_keys = []
    for key in get_pg_keys:
        if key <= pg_rate:
            allowed_keys.append(key)
    allowed_movies_based_on_pg_rate = []
    for key in allowed_keys:
        allowed_movies_based_on_pg_rate += PG[key]
    return allowed_movies_based_on_pg_rate

def update_by_pg_rate(pg_rate):
    """Update data GENRES and CAST based on PG rate"""

    # get movies based on pg rate
    allowed_movies_based_on_pg_rate = get_movies_based_on_pg_rate(pg_rate)
    # update cast table
    new_cast = CAST.copy()
    for movie in CAST:
        if not movie in allowed_movies_based_on_pg_rate:
            new_cast.pop(movie)
    # update genres table
    new_genres = {}
    for genre_old, films in GENRES.items():
        movies = []
        for movie in films:
            if movie in allowed_movies_based_on_pg_rate:
                movies.append(movie)
        if len(movies) > 0:
            new_genres[genre_old] = movies
    return dict(cast=new_cast, genres=new_genres)

# ----------------------------------------------------------------Main Programm----------------------------------------------------------------

# Input of user`s age and verify it is valid integer value
pg_input = input('Input your age in full years: ')
intBool = is_integer(pg_input)
while not intBool:
    pg_input = input('Input your full years: ')
    intBool = is_integer(pg_input)

if len(get_movies_based_on_pg_rate(int(pg_input))) > 0:
    search_input = input('Search by Genre: ')

    if search_input == 'y':

        # Find genre
        updated_data = update_by_pg_rate(int(pg_input))
        genre = search(list(updated_data['genres'].keys()))
        # Find movie by genre
        movie_by_genre = search(updated_data['genres'][genre], 'movie')

        print(f'Movie to watch: {movie_by_genre}. Genre: {genre}.\n')
    elif search_input == 'n':
        search_input = input('Search by Actor: ')
        if search_input == 'y':
            # Get available actors
            updated_data = update_by_pg_rate(int(pg_input))
            available_actors = get_available_values(updated_data['cast'])

            # Find actor
            actor = search(available_actors, 'actor')

            # find films with actor
            available_movies_with_actor = find_movies_by_actor(actor, updated_data['cast'])

            # Find movie by actor
            movie_by_actor = search(available_movies_with_actor, 'movie')
            print(f'Movie to watch: {movie_by_actor}. Starring: {actor}.\n')
        else:
            print('There is no searching. Choose searching by Genre or Actor.')
    else:
        print('Invalid search parameter. Try "y" or "n".')
else:
    print('There are no available movies based on your age')
