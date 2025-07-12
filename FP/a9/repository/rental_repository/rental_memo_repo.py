from copy import copy

from src.domain.rental import Rental
class RentalRepositoryError(Exception):
    pass
class DuplicateRentalIDError(RentalRepositoryError):
    pass
class RentalIDNotFoundError(RentalRepositoryError):
    pass

class RentalMemoRepo():
    def __init__(self):
        self._data={}

    def add(self, rental: Rental):
        if rental.rental_id in self._data:
            raise DuplicateRentalIDError("Duplicate rental id error")
        self._data[rental.rental_id] = rental

    def remove(self, rental_id):
        rental=self.get_rental_by_id(rental_id)
        if rental is None:
            raise RentalIDNotFoundError("Rental id not found")
        self._data.pop(rental_id)
        return rental

    def update(self, rental_id, returned_date):
        old_rental=copy(self.get_rental_by_id(rental_id))
        if old_rental is None:
            raise RentalIDNotFoundError("Rental id not found")
        for rental in self._data.values():
            if rental.rental_id == rental_id:
                rental.returned_date = returned_date
        return old_rental

    def get_all(self):
        return list(self._data.values())

    def get_last_rental(self):
        return sorted(self._data.keys())[-1]

    def get_rental_by_book_id(self, search_book_id):
        for rental_id in self._data:
            if self._data[rental_id].book_id == search_book_id:
                return rental_id
        return -1

    def get_book_rented(self, search_book_id):
        for rental_id in self._data:
            if self._data[rental_id].book_id == search_book_id and self._data[rental_id].returned_date=="-":
                return rental_id

    def get_rental_by_id(self, search_rental_id):
        for rental_id in self._data:
            if rental_id == search_rental_id:
                return self._data[rental_id]
        return None



    def __iter__(self):
        return RentalRepositoryIterator(list(self._data.values()))

    #def __getitem__(self, key):
      #  if key not in self._data:
      #      return None
      #  return self._data[key]

class RentalRepositoryIterator():
    def __init__(self, data):
        self.__data=data
        self.__pos=-1
    def __next__(self):
         self.__pos +=1
         if len(self.__data)==self.__pos:
             raise StopIteration()
         return self.__data[self.__pos]


