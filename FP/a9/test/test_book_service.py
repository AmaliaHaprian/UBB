from unittest import TestCase

from src.domain.book import Book
from src.repository.book_repository.book_memo_repo import BookMemoRepo
from src.services.book_service import BookService


class TestBookService(TestCase):
    def test_book_service(self):
        book_repo=BookMemoRepo()
        book_service = BookService(book_repo)
        self.assertIsInstance(book_service, BookService)

        self.assertEqual(len(book_service.get_books()), 0)
        book_service.add_book(Book(1, "Harap Alb", "Ion Creanga"))
        self.assertEqual(len(book_service.get_books()), 1)

        #book_service.remove_book(1)
        #self.assertEqual(len(book_service.get_books()), 0)
