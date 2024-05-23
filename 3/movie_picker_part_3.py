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

search_input = input('Search by Genre: ')

if search_input == 'y':
    print(f'Available Movies: {GENRES.keys()}\n')
    genre = input('Enter Genre: ')
    while not GENRES.get(genre):
        print(f'Genre {genre} not found. Please try again.')
        genre = input('Enter Genre: ')
    print(f'Available Movies: {GENRES[genre]}\n')
    movie_by_genre = input('Enter Movie: ')
    while not movie_by_genre in GENRES[genre]:
        print(f'Movie {movie_by_genre} not found. Please try again.')
        movie_by_genre = input('Enter Movie: ')
    print(f'Movie to watch: {movie_by_genre}. Genre: {genre}.\n')
elif search_input == 'n':
    search_input = input('Search by Actor: ')
    if search_input == 'y':
        # flatten the list to create a Set
        actors = [item for sublist in CAST.values() for item in sublist]
        # create a Set of actors
        available_actors = set(actors)
        print(f'Available Actors: {available_actors}\n')
        # input actor to search
        actor = input('Enter Actor: ')
        while not actor in available_actors:
            print(f'Actor {actor} not found. Please try again.')
            actor = input('Enter Actor: ')
        available_movies_with_actor = []
        # find films with actor
        i = 0
        films_array = list(CAST.keys())
        while i < len(films_array):
            FILM = films_array[i]
            if actor in CAST.get(FILM):
                available_movies_with_actor.append(FILM)
            i += 1
        print(f'Available Movies: {available_movies_with_actor} with {actor}\n')
        # find movie
        movie_by_actor = input('Enter Movie: ')
        while not movie_by_actor in available_movies_with_actor:
            print(f'Movie {movie_by_actor} with actor {actor} not found. Please try again.')
            movie_by_actor = input('Enter Movie: ')
        print(f'Movie to watch: {movie_by_actor}. Starring: {actor}.\n')
    else:
        print('There is no searching. Choose searching by Genre or Actor.')
else:
    print('Invalid search parameter. Try "y" or "n".')
