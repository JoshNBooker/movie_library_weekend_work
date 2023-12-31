from flask import Flask
from controllers.movie_controller import movie_blueprint

app = Flask(__name__)
app.register_blueprint(movie_blueprint)