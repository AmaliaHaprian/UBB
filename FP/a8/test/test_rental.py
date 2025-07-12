from datetime import date
from unittest import TestCase

from src.domain.rental import Rental


class TestRental(TestCase):
    def test_rental(self):
        rental=Rental(1000,1,100, date(2024,10,1), date(2024,10,10))
        self.assertEqual(rental.rental_id, 1000)
        self.assertEqual(rental.book_id, 1)
        self.assertEqual(rental.client_id, 100)
        self.assertEqual(rental.rented_date, date(2024,10,1))
        self.assertEqual(rental.returned_date, date(2024 ,10 ,10))
        self.assertIsInstance(rental, Rental)

        rental.rented_date=date(2024,10,2)
        self.assertEqual(rental.rented_date, date(2024,10,2))

        rental.returned_date=date(2024,10,11)
        self.assertEqual(rental.returned_date, date(2024,10,11))


        self.assertEqual(rental.__len__(), 10)
        self.assertEqual(rental.__str__(), str(rental))
        self.assertEqual(rental.__repr__(), repr(rental))