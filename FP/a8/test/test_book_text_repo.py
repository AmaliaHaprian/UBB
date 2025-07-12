from unittest import TestCase

from src.domain.book import Book
from src.repository.book_repository.book_text_repo import BookTextRepo


class TestBookTextRepo(TestCase):
    def test_repo(self):
        open("test_book.txt", "w").close()

        repo=BookTextRepo("test_book.txt")
        self.assertEqual(len(repo.get_all()), 0)

        repo.add(Book(1, "Harap Alb", "Ion Creanga"))
        self.assertEqual(len(repo.get_all()), 1)
        self.assertEqual(repo.get_all()[0].title, "Harap Alb")
        self.assertEqual(repo.get_all()[0].author, "Ion Creanga")

        repo.remove(1)
        self.assertEqual(len(repo.get_all()), 0)


        repo.add(Book(1, "Harap Alb", "Ion Creanga"))
        repo.update(1, "Luceafarul", "Mihai Eminescu")
        self.assertEqual(repo.get_all()[0].title, "Luceafarul")
        self.assertEqual(repo.get_all()[0].author, "Mihai Eminescu")

        self.assertEqual(repo.get_all()[0].title, "Luceafarul")
        filtered = repo.search_by_title("Luceafarul")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        book_id = repo.get_id_from_title("Luceafarul")
        self.assertEqual(book_id, 1)

        search_book_title = "luceaf"
        filtered = repo.search_by_title(search_book_title)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Luceafarul")

        search_book_author = "Mihai"
        filtered = repo.search_by_author(search_book_author)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].author, "Mihai Eminescu")