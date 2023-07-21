from flask import render_template, Blueprint
from models.movie_catalogue import movie

movie_blueprint = Blueprint("tasks", __name__)