import fresh_tomatoes
import media

# Create Movie objects for your favorite movies here.
laurence_of_arabia = media.Movie(
    title='Laurence Of Arabia',
    poster_url='https://upload.wikimedia.org/wikipedia/'
               'commons/thumb/c/c5/Lawrence_of_arabia_ver3_xxlg.jpg/'
               '786px-Lawrence_of_arabia_ver3_xxlg.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=zmr1iSG3RTA'
)

inception = media.Movie(
    title='Inception',
    poster_url='https://upload.wikimedia.org/'
               'wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=YoHD9XEInc0'
)

fight_club = media.Movie(
    title='Fight Club',
    poster_url='https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=SUXWAEX2jlg'
)

interstellar = media.Movie(
    title='Interstellar',
    poster_url='https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=zSWdZVtXT7E'
)

schindlers_list = media.Movie(
    title="Schindler's List",
    poster_url='https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg',
    trailer_youtube_url='https://www.youtube.com/watch?v=gG22XNhtnoY'
)


# Add all the movies to a movies list.
movies = [
    laurence_of_arabia,
    inception,
    fight_club,
    interstellar,
    schindlers_list
]

# Call the open_movies_page funtion
fresh_tomatoes.open_movies_page(movies)
