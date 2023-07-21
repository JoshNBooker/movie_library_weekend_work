from flask import render_template, Blueprint
from models.movie_catalogue import *

movie_blueprint = Blueprint("movie", __name__)

@movie_blueprint.route("/")
def index():
    return render_template("index.jinja", title="80s Emporium", movie_catalogue=movie_catalogue)