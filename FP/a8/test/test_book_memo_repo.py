from unittest import TestCase

from src.domain.book import Book
from src.repository.book_repository.book_memo_repo import BookMemoRepo, DuplicateIDError, BookIDNotFoundError, \
    EmptyInputError, InputError
from src.test.test_book import TestBook


class TestBookMemoRepo(TestCase):
    def test_repo(self):
        repo=BookMemoRepo()
        self.assertEqual(len(repo.get_all()), 0)

        repo.add(Book(1, "Harap Alb", "Ion Creanga"))
        self.assertEqual(len(repo.get_all()), 1)

        self.assertRaises(EmptyInputError, repo.add, Book(2, "", "Ion Creanga"))
        self.assertRaises(InputError, repo.add, Book(2, "ha", "Ion Creanga"))

        repo.remove(1)
        self.assertEqual(len(repo.get_all()), 0)

        repo.add(Book(1, "Harap Alb", "Ion Creanga"))
        repo.update(1, "Luceafarul", "Mihai Eminescu")
        self.assertEqual(repo.get_all()[0].title, "Luceafarul")
        self.assertRaises(DuplicateIDError, repo.add, Book(1, "Harap Alb", "Ion Creanga"))
        self.assertRaises(BookIDNotFoundError, repo.update, 2, "Luceafarul", "Mihai Eminescu")

        self.assertRaises(BookIDNotFoundError, repo.remove, 2)

        book=repo.search_by_id(1)
        self.assertIsInstance(book, Book)
        self.assertEqual(book.book_id, 1)
        self.assertEqual(book.title, "Luceafarul")
        self.assertEqual(book.author, "Mihai Eminescu")


        self.assertEqual(repo.get_all()[0].title, "Luceafarul")
        filtered=repo.search_by_title("Luceafarul")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        book_id=repo.get_id_from_title("Luceafarul")
        self.assertEqual(book_id, 1)

        search_book_title="luceaf"
        filtered=repo.search_by_title(search_book_title)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        search_book_author="Mihai"
        filtered=repo.search_by_author(search_book_author)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].author, "Mihai Eminescu")

