from typing import List
import csv


class Movie:
    """A movie available for rent."""
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title:str, year: int, genre: List[str], price_code):
        """Initialize a new movie."""
        self.title = title
        self.year = year
        self.genre = genre
        self._price_code = price_code

    def get_genre(self):
        return self.genre

    def is_genre(self, genre:str):
        return genre in self.genre

    def get_year(self):
        return self.year

    def get_title(self):
        return self.title
    
    def get_price_code(self):
        return self._price_code

    def __str__(self):
        return self.title


class MovieCatalog:

    def __init__(self):
        """Initialize a new movie."""
        self.movie_list = {}
        with open('movies.csv') as file:
            reader = csv.DictReader(file)
        for i in reader:
            self.movie_list[i["title"]] = {
                "#id": i["#id"],
                "year": i["year"],
                "genre": [j for j in i["genres"].split("|")]
            }

    def get_movie(self, title):
        movie = self.movie_list[title]
        return Movie(title, movie["year"], movie["genre"])
