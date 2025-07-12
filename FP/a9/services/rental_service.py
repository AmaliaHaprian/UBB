import copy
import random
from datetime import date
from random import randint

from src.domain import book
from src.domain.rental import Rental
from src.services.undo_service import UndoService, FunctionCall, Operation


class RentalService:
    def __init__(self,rental_repo, undo_service:UndoService,book_repo,client_repo):
        self._rental_repo = rental_repo
        self._book_repo = book_repo
        self._client_repo = client_repo
        self._undo_service=undo_service
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

        function_undo=FunctionCall(self._rental_repo.remove,rental.rental_id)
        function_redo=FunctionCall(self._rental_repo.add,rental)

        self._undo_service.record(Operation(function_undo,function_redo))

    def remove_rental(self, rental_id):
        """
        Removes a rental
        :param rental_id: the rental id that points to the rental to be removed
        :return: None
        """
        rental=self._rental_repo.remove(rental_id)
        return rental

    def update_rental(self, rental_id, returned_date):
        """
        Updates a rental
        :param rental_id: the rental id that points to the rental to be updated
        :param returned_date: the date when the book was returned
        :return: None
        """

        rental=self._rental_repo.update(rental_id, returned_date)
        function_undo = FunctionCall(self._rental_repo.update, rental.rental_id, rental.returned_date)
        function_redo = FunctionCall(self._rental_repo.update, rental_id, returned_date)

        self._undo_service.record(Operation(function_undo, function_redo))
        return rental
    def rentals(self):
        return copy.deepcopy(self._rental_repo.get_all())

    def rental_by_book_id(self, book_id):
        return self._rental_repo.get_rental_by_book_id(book_id)
    def last_rental(self):
        return self._rental_repo.get_last_rental()

    def book_rented(self, book_id):
        return self._rental_repo.get_book_rented(book_id)

    def frequency_rentals(self):
        dict_of_app={}
        last_book_id=self._book_repo.get_last_book()
        for i in range(1,last_book_id+1):
            dict_of_app.update({i: 0})
        for rental in self._rental_repo.get_all():
            dict_of_app[rental.book_id]+=1

        sorted_dict=dict(sorted(dict_of_app.items(), key=lambda x: x[1] , reverse=True))
        #return sorted_dict # a dictionary where the key is the book id and the value is it s appearance in the rental repo
        list_of_books=[]
        for key in sorted_dict:
            list_of_books.append([self._book_repo.get_book_by_id(key), sorted_dict[key]])
        return list_of_books


    def rental_days_clients(self):
        dict_of_app={}
        last_client_id=self._client_repo.get_last_client()
        for i in range(100,last_client_id+1):
            dict_of_app.update({i: 0})
        for rental in self._rental_repo.get_all():
            if rental.returned_date=='-':
                returned_date=date.today()
                dict_of_app[rental.client_id]=(returned_date-rental.rented_date).days
            else:
                dict_of_app[rental.client_id]+=(rental.returned_date-rental.rented_date).days
        sorted_dict=dict(sorted(dict_of_app.items(), key=lambda x: x[1] , reverse=True))
        list_of_clients=[]
        for key in sorted_dict:
            list_of_clients.append([self._client_repo.search_by_client_id(key), sorted_dict[key]])
        return list_of_clients

    def most_rented_author(self):
        authors=self._book_repo.list_of_authors()
        dict_of_app={}

        for i in range(len(authors)):
            dict_of_app.update({authors[i]: 0})
        for rental in self._rental_repo.get_all():
            book=self._book_repo.get_book_by_id(rental.book_id)
            dict_of_app[book.author]+=1
        sorted_dict=dict(sorted(dict_of_app.items(), key=lambda x: x[1] , reverse=True))
        list_of_authors=[]
        for key in sorted_dict:
            list_of_authors.append([key, sorted_dict[key]])
        return list_of_authors
        #return sorted_dict

    def getRepo(self):
        return self._rental_repo



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
