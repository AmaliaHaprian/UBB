from src.domain.book import Book
from src.validators.errors import StringError
from src.validators.validator import Validator


class BookService:
    def __init__(self, repo):
        self._repo = repo
        self._validator=Validator()
        #self.generate_books()

    def get(self, book_id):
        return self._repo[book_id]

    def add_book(self, book: Book):
        """
        The function adds a new book
        :param book: the book entity
        :return: None
        """
        if not self._validator.validate_string(book.title):
            raise StringError
        if not self._validator.validate_string(book.author):
            raise StringError
        self._repo.add(book)

    def remove_book(self, book_id):
        """
        Removes a book
        :param book_id: the id of the book to be removed
        :return: None
        """

        self._repo.remove(book_id)

    def update_book(self, book_id, new_title, new_author):
        """
        Updates a book
        :param book_id: the id of the book to be updated
        :param new_title: the new title of the book
        :param new_author: the new author of the book
        :return: None
        """

        self._repo.update(book_id, new_title, new_author)

    def get_books(self):
        return self._repo.get_all()

    def search_id(self, book_id):
        return self._repo.search_by_id(book_id)

    def search_title(self, book_title):

        return self._repo.search_by_title(book_title)

    def search_author(self, book_author):

        return self._repo.search_by_author(book_author)

    def get_book_id(self, book_title):
        return self._repo.get_id_from_title(book_title)










    def generate_books(self, ):

        self.add_book(Book(1, "Luceafarul", "Mihai Eminescu"))
        self.add_book(Book(2, "Fratii Karamazov", "Dostoievsky"))
        self.add_book(Book(3, "Crima si pedeapsa", "Dostoievsky"))
        self.add_book(Book(4, "Anna Karenina", "Leo Tolstoy"))
        self.add_book(Book(5, "Povestea lui Harap-Alb", "Ion Creanga"))
        self.add_book(Book(6, "Ion", "Liviu Rebreanu"))
        self.add_book(Book(7, "Moara cu Noroc", "Ioan Slavici"))
        self.add_book(Book(8, "Poezii", "Lucian Blaga"))
        self.add_book(Book(9, "O scrisoare pierduta", "Ion Luca Caragiale"))
        self.add_book(Book(10, "Ulysses", "James Joyce"))
        self.add_book(Book(11, "The Great Gatsby", "F. Scott Fitzgerald"))
        self.add_book(Book(12, "Nineteen Eighty-Four", "George Orwell"))
        self.add_book(Book(13, "A Tale of Two Cities", "Charles Dickens"))
        self.add_book(Book(14, "The Name of the Rose", "Umberto Eco"))
        self.add_book(Book(15, "To Kill a Mockingbird", "Harper Lee"))
        self.add_book(Book(16, "War and Peace", "Leo Tolstoy"))
        self.add_book(Book(17, "Animal Farm", "George Orwell"))
        self.add_book(Book(18, "Pride and Prejudice", "Jane Austen"))
        self.add_book(Book(19, "The Chronicles of Narnia", "C. S. Lewis"))
        self.add_book(Book(20, "Fahrenheit 451", "Ray Bradbury"))
