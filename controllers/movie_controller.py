from flask import render_template, Blueprint
from models.movie_catalogue import Movie, movie_catalogue

movie_blueprint = Blueprint("tasks", __name__)