import os
from configparser import ConfigParser
from datetime import timedelta, date
from random import randint

from faker import Faker
from jproperties import Properties

from src.repository.book_repository.book_binary_repo import BookBinaryRepo
from src.repository.book_repository.book_memo_repo import BookMemoRepo
from src.repository.book_repository.book_text_repo import BookTextRepo
from src.repository.client_repository.client_binary_repo import ClientBinaryRepo
from src.repository.client_repository.client_memo_repo import ClientMemoRepo
from src.repository.client_repository.client_text_repo import ClientTextRepo
from src.repository.rental_repository.rental_binary_repo import RentalBinaryRepo
from src.repository.rental_repository.rental_memo_repo import RentalMemoRepo
from src.repository.rental_repository.rental_text_repo import RentalTextRepo
from src.ui.gui_class import LibraryManagerApp
from src.ui.ui import *


def generate_books():
    book_list= [Book(1, "Luceafarul", "Mihai Eminescu"), Book(2, "Fratii Karamazov", "Dostoievsky"),
                Book(3, "Crima si pedeapsa", "Dostoievsky"), Book(4, "Anna Karenina", "Leo Tolstoy"),
                Book(5, "Povestea lui Harap-Alb", "Ion Creanga"), Book(6, "Ion", "Liviu Rebreanu"),
                Book(7, "Moara cu Noroc", "Ioan Slavici"), Book(8, "Poezii", "Lucian Blaga"),
                Book(9, "O scrisoare pierduta", "Ion Luca Caragiale"), Book(10, "Ulysses", "James Joyce"),
                Book(11, "The Great Gatsby", "F. Scott Fitzgerald"), Book(12, "Nineteen Eighty-Four", "George Orwell"),
                Book(13, "A Tale of Two Cities", "Charles Dickens"), Book(14, "The Name of the Rose", "Umberto Eco"),
                Book(15, "To Kill a Mockingbird", "Harper Lee"), Book(16, "War and Peace", "Leo Tolstoy"),
                Book(17, "Animal Farm", "George Orwell"), Book(18, "Pride and Prejudice", "Jane Austen"),
                Book(19, "The Chronicles of Narnia", "C. S. Lewis"), Book(20, "Fahrenheit 451", "Ray Bradbury")]
    return book_list

def generate_rentals():
    rental_list = []
    for i in range(1000, 1021):
        rented_date = date(2024, randint(1, 12), randint(1, 30))
        rental_days=timedelta(days=randint(1,20))
        returned_date = rented_date + rental_days
        #returned_date = date(2024, randint(1, 12), randint(1, 30))
        rental_list.append(Rental(i, randint(1,20), randint(100,120), rented_date, returned_date))
        #rental_list.append(Rental(i, randint(1, len(list(self._book_repo))), randint(1, len(list(self._book_repo))), rented_date, returned_date))
        #rental_list.append(Rental(i, random.choice(list(self._book_repo)), random.choice(list(self._client_repo)), rented_date, returned_date))
    return rental_list


def generate_clients():
    client_list = []
    fake = Faker()
    for i in range(100, 121):
        client_list.append(Client(i, fake.name()))
    return client_list

parser = ConfigParser()
parser.read('settings.properties')
repo_style = parser.get('options', 'repository')
book = parser.get('options', 'book')
client = parser.get('options', 'client')
rental = parser.get('options', 'rental')
if repo_style == "memory":

    book_repo = BookMemoRepo()
    for book in generate_books():
        book_repo.add(book)

    client_repo = ClientMemoRepo()
    for client in generate_clients():
        client_repo.add(client)

    rental_repo = RentalMemoRepo()
    for rental in generate_rentals():
        rental_repo.add(rental)

    book_service = BookService(book_repo)
    client_service = ClientService(client_repo)
    rental_service = RentalService(rental_repo, book_repo, client_repo)

    ui = UI(book_service, client_service, rental_service)
    gui=LibraryManagerApp(book_service, client_service, rental_service)

elif repo_style == "pickle":

    book_repo = BookBinaryRepo(book)
    for book in generate_books():
        book_repo.add(book)

    client_repo = ClientBinaryRepo(client)
    for client in generate_clients():
        client_repo.add(client)

    rental_repo = RentalBinaryRepo(rental)
    for rental in generate_rentals():
        rental_repo.add(rental)

    book_service = BookService(book_repo)
    client_service = ClientService(client_repo)
    rental_service = RentalService(rental_repo, book_repo, client_repo)

    ui = UI(book_service, client_service, rental_service)
    gui = LibraryManagerApp(book_service, client_service, rental_service)
elif repo_style == "text":

    book_repo = BookTextRepo(book)
    if os.path.getsize('files/txt/books.txt') == 0:
        for book in generate_books():
            book_repo.add(book)

    client_repo = ClientTextRepo(client)
    if os.path.getsize('files/txt/clients.txt') == 0:
        for client in generate_clients():
            client_repo.add(client)

    rental_repo = RentalTextRepo(rental)
    if os.path.getsize('files/txt/rentals.txt') == 0:
        for rental in generate_rentals():
            rental_repo.add(rental)

    book_service = BookService(book_repo)
    client_service = ClientService(client_repo)
    rental_service = RentalService(rental_repo, book_repo, client_repo)

    ui = UI(book_service, client_service, rental_service)
    gui = LibraryManagerApp(book_service, client_service, rental_service)

choice=input("what type of ui do you want? 1.UI 2.GUI :")
if choice=="1":
    ui.print_ui()
else:
    gui.create_main_ui()





