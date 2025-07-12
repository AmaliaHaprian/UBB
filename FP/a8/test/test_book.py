from unittest import TestCase

from src.domain.book import Book


class TestBook(TestCase):
    def test_book(self):
        book=Book(1, "Harap Alb", "Ion Creanga")
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Harap Alb")
        self.assertEqual(book.author, "Ion Creanga")

        self.assertIsInstance(book, Book)

        book.title="Luceafarul"
        book.author="Mihai Eminescu"
        self.assertEqual(book.title, "Luceafarul")
        self.assertEqual(book.author, "Mihai Eminescu")

        self.assertEqual(book.__str__(),"Book id=1 is Luceafarul by Mihai Eminescu")
        self.assertEqual(book.__repr__(), str(book))