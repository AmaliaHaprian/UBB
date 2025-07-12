from datetime import date
from unittest import TestCase

from src.domain.rental import Rental
from src.repository.rental_repository.rental_memo_repo import RentalIDNotFoundError
from src.repository.rental_repository.rental_text_repo import RentalTextRepo


class TestRentalTextRepo(TestCase):
    def test_rental_text_repo(self):
        open("test_rental.txt", "w").close()
        repo=RentalTextRepo("test_rental.txt")
        repo.add(Rental(1000, 1, 100, date(2024, 10, 11), date(2024, 11, 11)))
        self.assertEqual(len(repo.get_all()), 1)
        self.assertEqual(repo.get_all()[0].rental_id, 1000)
        self.assertEqual(repo.get_all()[0].book_id, 1)
        self.assertEqual(repo.get_all()[0].client_id, 100)
        self.assertEqual(repo.get_all()[0].rented_date, date(2024, 10, 11))
        self.assertEqual(repo.get_all()[0].returned_date, date(2024, 11, 11))

        repo.remove(1000)
        self.assertEqual(len(repo.get_all()), 0)
        self.assertRaises(RentalIDNotFoundError, repo.remove, 1000)

        repo.add(Rental(1000, 1, 100, date(2024, 10, 11), '-'))
        self.assertEqual(len(repo.get_all()), 1)
        repo.update(1000, date(2024, 10, 11))
        self.assertEqual(repo.get_all()[0].rental_id, 1000)
        self.assertEqual(repo.get_all()[0].book_id, 1)
        self.assertEqual(repo.get_all()[0].client_id, 100)
        self.assertEqual(repo.get_all()[0].rented_date, date(2024, 10, 11))
        self.assertEqual(repo.get_all()[0].returned_date, date(2024, 10, 11))

        repo.add(Rental(1001, 1, 100, date(2024, 10, 11), date(2024, 11, 11)))
        last_rental = repo.get_last_rental()
        self.assertEqual(last_rental, 1001)

        self.assertEqual(repo.get_rental_by_book_id(1), 1000)
        self.assertEqual(repo.get_rental_by_book_id(2), -1)