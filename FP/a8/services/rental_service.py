import random
from datetime import date
from random import randint

from src.domain.rental import Rental


class RentalService:
    def __init__(self,rental_repo,book_repo,client_repo):
        self._rental_repo = rental_repo
        self._book_repo = book_repo
        self._client_repo = client_repo
        #self.generate_rentals()
   # @property
    #def books(self):
    #    return list(self._book_repo)
    #def clients(self):
     #   return list(self._client_repo)

    def get_rentals(self, rental_id):
        rentals=self._rental_repo.get_all()
        for rental in rentals:
            if rental.rental_id==rental_id:
                return rental

    def add_rental(self, rental):
        """
        Add a rental
        :param rental: the rental entity to be added
        :return: None
        """
        self._rental_repo.add(rental)

    def remove_rental(self, rental_id):
        """
        Removes a rental
        :param rental_id: the rental id that points to the rental to be removed
        :return: None
        """
        self._rental_repo.remove(rental_id)

    def update_rental(self, rental_id, returned_date):
        """
        Updates a rental
        :param rental_id: the rental id that points to the rental to be updated
        :param returned_date: the date when the book was returned
        :return: None
        """

        self._rental_repo.update(rental_id, returned_date)

    def rentals(self):
        return self._rental_repo.get_all()

    def rental_by_book_id(self, book_id):
        return self._rental_repo.get_rental_by_book_id(book_id)
    def last_rental(self):
        return self._rental_repo.get_last_rental()

    def book_rented(self, book_id):
        return self._rental_repo.get_book_rented(book_id)





    def generate_rentals(self):

        rental_list = []
        for i in range(1000, 1021):
            rented_date = date(2024, randint(1, 12), randint(1, 30))
            returned_date = date(2024, randint(1, 12), randint(1, 30))
            #rental_list.append(Rental(i, randint(1,20), randint(100,120), rented_date, returned_date))
            rental_list.append(Rental(i, randint(1, len(list(self._book_repo))), randint(1, len(list(self._book_repo))), rented_date, returned_date))
            #rental_list.append(Rental(i, random.choice(list(self._book_repo)), random.choice(list(self._client_repo)), rented_date, returned_date))
        for rental in rental_list:
            self.add_rental(rental)
