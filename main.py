# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import MovieCatalog
from rental import Rental, PriceCode
from customer import Customer

def make_movies():
    catalog = MovieCatalog()
    movies = [
        # Movie("The Irishman", PriceCode.new_release),
        # Movie("CitizenFour", PriceCode.regular),
        # Movie("Frozen", PriceCode.children),
        # Movie("El Camino", PriceCode.new_release),
        # Movie("Particle Fever", PriceCode.regular)
        catalog.get_movie("The Martian"),
        catalog.get_movie("Hacksaw Ridge")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
