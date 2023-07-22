from models.movie import Movie

The_Shining = Movie("The Shining", "Stanley Kubrick", "Horror", 1980, "Surreal horror from a legendary director, and outstanding acting.", 2.49)
The_Terminator = Movie("The Terminator", "James Cameron", "Sci-Fi Action", 1984, "Time-bending Sci-Fi and dodgy accents.", 2.75)
Legend = Movie("Legend", "Ridley Scott", "Fantasy", 1985, "Some fantasy film, I've never seen it.", 1.89)

movie_catalogue = [The_Shining, The_Terminator, Legend]

def submit_new_movie(movie):
    movie_catalogue.append(movie)

def rent_movie(movie):
    movie.available = False