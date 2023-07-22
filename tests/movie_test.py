import unittest
from models.movie import Movie

class TestMovie(unittest.TestCase):

    def SetUp(self):
        self.movie = Movie("Gremlins", "Joe Dante", "Horror Comedy", 1984, "Little monsters and stuff", 1.50)

    def test_has_attributes(self):
        self.assertEqual("hkfh", self.movie.title)