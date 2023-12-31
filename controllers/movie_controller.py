from flask import render_template, Blueprint, request, redirect
from models.movie_catalogue import Movie, submit_new_movie, movie_catalogue, rent_movie, return_movie, show_movie

movie_blueprint = Blueprint("movie", __name__)

@movie_blueprint.route("/")
def index():
    return render_template("index.jinja", title="80s Emporium", movie_catalogue=movie_catalogue)

@movie_blueprint.route("/movies")
def add_movie():
    return render_template("add_movie.jinja", title="Add your movie!")

@movie_blueprint.route("/movies", methods=["POST"])
def submit_movie():
    movie_name = request.form["name"]
    movie_director = request.form["director"]
    movie_genre = request.form["genre"]
    movie_release = request.form["release"]
    movie_description = request.form["description"]
    movie_price = "User submitted - not for rent (yet)"
    new_movie = Movie(movie_name, movie_director, movie_genre, movie_release, movie_description, movie_price)
    submit_new_movie(new_movie)
    return redirect("/")

@movie_blueprint.route("/movies/<index>/delete", methods=["GET", "POST"])
def delete_movie(index):
    del movie_catalogue[int(index)]
    return redirect("/")

@movie_blueprint.route("/movies/<index>/rent", methods=["GET", "POST"])
def rent_movie_request(index):
    rent_movie(movie_catalogue[int(index)])
    return redirect("/")

@movie_blueprint.route("/movies/<index>", methods = ["POST"])
def return_movie_request(index):
    return_movie(movie_catalogue[int(index)])
    return redirect("/")

@movie_blueprint.route("/movies/<index>")
def single_movie(index):
    index = movie_catalogue[int(index)]
    requested_movie = show_movie(index)
    return render_template ("single_movie.jinja", title=requested_movie[0].title, requested_movie=requested_movie, movie_catalogue=movie_catalogue)