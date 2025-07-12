from datetime import date

from src.domain.book import Book
from src.domain.client import Client


class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id
    @property
    def book_id(self):
        return self.__book_id
    @property
    def client_id(self):
        return self.__client_id
    @property
    def rented_date(self):
        return self.__rented_date
    @property
    def returned_date(self):
        return self.__returned_date
    @rented_date.setter
    def rented_date(self, rented_date):
        self.__rented_date = rented_date
    @returned_date.setter
    def returned_date(self, returned_date):
        self.__returned_date = returned_date

    def __len__(self):
        return self.__returned_date - self.__rented_date+1

    def __str__(self):
        if self.__rented_date!="-":
            from_date=self.__rented_date.strftime('%Y-/%m-/%d')
        else:
            from_date=self.__rented_date
        if self.__returned_date!="-":
            to_date=self.__returned_date.strftime('%Y-/%m-/%d')
        else:
            to_date=self.__returned_date
        return f"Rental with id={self.__rental_id} was book with id={self.__book_id} rented from {from_date} to {to_date} by client with id={self.__client_id}"

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    book=Book(1, "Harap Alb", "Ion Creanga")
    client=Client(100, "John Smith")
    rent=Rental(300, book.book_id, client.client_id, date(2024, 10, 1), date(2024, 11, 1))
    print(rent)