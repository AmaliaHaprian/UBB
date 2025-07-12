import os
from configparser import ConfigParser

from src.repository.book_repository.book_binary_repo import BookBinaryRepo
from src.repository.book_repository.book_memo_repo import BookMemoRepo
from src.repository.book_repository.book_text_repo import BookTextRepo
from src.repository.client_repository.client_binary_repo import ClientBinaryRepo
from src.repository.client_repository.client_memo_repo import ClientMemoRepo
from src.repository.client_repository.client_text_repo import ClientTextRepo
from src.repository.rental_repository.rental_binary_repo import RentalBinaryRepo
from src.repository.rental_repository.rental_memo_repo import RentalMemoRepo
from src.repository.rental_repository.rental_text_repo import RentalTextRepo
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from src.ui.ui import UI


class Settings:
    def __init__(self):
        parser=ConfigParser()
        parser.read('settings.properties')
        repo_style=parser.get('options', 'repository')
        book=parser.get('options', 'book')
        client=parser.get('options', 'client')
        rental=parser.get('options', 'rental')
        if repo_style=="memory":

            book_repo=BookMemoRepo()
            client_repo=ClientMemoRepo()
            rental_repo=RentalMemoRepo()

            book_service = BookService(book_repo)
            client_service = ClientService(client_repo)
            rental_service = RentalService(rental_repo,book_repo,client_repo)

            self._ui=UI(book_service, client_service, rental_service)
        elif repo_style=="pickle":

            book_repo = BookBinaryRepo(book)
            client_repo = ClientBinaryRepo(client)
            rental_repo = RentalBinaryRepo(rental)

            book_service = BookService(book_repo)
            client_service = ClientService(client_repo)
            rental_service = RentalService(rental_repo,book_repo,client_repo)

            self._ui = UI(book_service, client_service, rental_service)
        elif repo_style=="text":

            book_repo = BookTextRepo(book)
            client_repo = ClientTextRepo(client)
            rental_repo = RentalTextRepo(rental)

            book_service = BookService(book_repo)
            client_service = ClientService(client_repo)
            rental_service = RentalService(rental_repo,book_repo,client_repo)

            self._ui = UI(book_service, client_service, rental_service)

    @property
    def ui(self):
        return self._ui
