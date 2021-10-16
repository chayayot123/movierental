from enum import Enum


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frequent_renter_points": lambda days: days}
    normal = {"price": lambda days: (1.5 * days) + 2.0 if (days > 2) else 2,
              "frequent_rental_points": lambda days: 1}
    children = {"price": lambda days: (1.5 * days) + 2.5 if (days > 3) else 1.5,
                "frequent_rental_points": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).

    def __init__(self, title, price_code):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
