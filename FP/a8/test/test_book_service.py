from unittest import TestCase

from src.domain.book import Book
from src.repository.book_repository.book_memo_repo import BookMemoRepo
from src.services.book_service import BookService
from src.validators.errors import StringError


class TestBookService(TestCase):
    def test_book_service(self):
        book_repo=BookMemoRepo()
        book_service = BookService(book_repo)
        self.assertIsInstance(book_service, BookService)

        self.assertEqual(len(book_service.get_books()), 0)
        book_service.add_book(Book(1, "Harap Alb", "Ion Creanga"))
        self.assertEqual(len(book_service.get_books()), 1)


        book_service.remove_book(1)
        self.assertEqual(len(book_service.get_books()), 0)

        self.assertRaises(StringError, book_service.add_book, Book(1, "574e", "Ion Creanga"))
        book_service.add_book(Book(1, "Harap Alb", "Ion Creanga"))
        book_service.update_book(1, "Luceafarul", "Mihai Eminescu")
        self.assertEqual(book_service.get_books()[0].title, "Luceafarul")
        self.assertEqual(book_service.get_books()[0].author, "Mihai Eminescu")

        book=book_service.search_id(1)
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Luceafarul")
        self.assertEqual(book.author, "Mihai Eminescu")

        self.assertEqual(book_service.get_books()[0].title, "Luceafarul")
        filtered = book_service.search_title("Luceafarul")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        book_id = book_service.get_book_id("Luceafarul")
        self.assertEqual(book_id, 1)

        search_book_title = "luceaf"
        filtered = book_service.search_title(search_book_title)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        search_book_author = "Mihai"
        filtered = book_service.search_author(search_book_author)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].author, "Mihai Eminescu")