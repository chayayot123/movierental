from movie import Movie

from datetime import datetime

from enum import Enum

class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frequent_renter_points": lambda days: days}
    regular = {"price": lambda days: (1.5 * days) + 2.0 if (days > 2) else 2,
               "frequent_rental_points": lambda days: 1}
    children = {"price": lambda days: (1.5 * days) + 2.5 if (days > 3) else 1.5,
                "frequent_rental_points": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def points(self, days: int) -> float:
        """Return the rental points for a given number of days."""
        point = self.value["frequent_rental_points"]
        return point(days)


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.get_movie().get_price_code().price(self.get_days_rented())

    def get_rental_point(self):
        return self.get_movie().get_price_code().points(self.get_days_rented())

    @classmethod
    def for_movie(cls, movies: Movie):
        price_code = PriceCode.regular
        if int(movies.get_year()) == datetime.now().year:
            price_code = PriceCode.new_release
        elif movies.is_genre("Children"):
            price_code = PriceCode.children
        return price_code


