from unittest import TestCase

from src.domain.client import Client
from src.repository.book_repository.book_memo_repo import DuplicateIDError, EmptyInputError, InputError
from src.repository.client_repository.client_memo_repo import ClientMemoRepo, DuplicateClientIDError, \
    ClientIDNotFoundError


class TestClientMemoRepo(TestCase):
    def test_memo(self):
        repo=ClientMemoRepo()
        repo.add(Client(100, "John Smith"))
        self.assertEqual(repo.get_all()[0].name, "John Smith")
        self.assertEqual(len(repo.get_all()), 1)

        self.assertRaises(EmptyInputError, repo.add, Client(101, ""))
        self.assertRaises(InputError, repo.add, Client(101, "Jo"))

        last_client_id=repo.get_last_client()
        self.assertEqual(last_client_id, 100)

        #self.assertEqual(repo.search_by_client_id(100),  Client(100, "John Smith"))

        repo.remove(100)
        self.assertEqual(len(repo.get_all()), 0)

        repo.add(Client(100, "John Smith"))
        self.assertRaises(DuplicateClientIDError, repo.add, Client(100, "John Smith"))
        repo.update(100, "Daniel Smith")
        self.assertEqual(repo.get_all()[0].name, "Daniel Smith")

        self.assertRaises(ClientIDNotFoundError, repo.remove, 101)

        self.assertRaises(ClientIDNotFoundError, repo.update, 101, "John Smith")


        self.assertEqual(repo.get_all()[0].name, "Daniel Smith")
        search_name='daniel'
        filtered=repo.search_by_name(search_name)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].name, "Daniel Smith")