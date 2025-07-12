from unittest import TestCase

from src.domain.book import Book


class TestBook(TestCase):
    def test_book(self):
        book=Book(1, "Harap Alb", "Ion Creanga")
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Harap Alb")
        self.assertEqual(book.author, "Ion Creanga")