from unittest import TestCase

from src.domain.rental import Rental


class TestRental(TestCase):
    def test_rental(self):
        rental=Rental(1000,1,100, 2024-10-1, 2024-10-10)
        self.assertEqual(rental.rental_id, 1000)
        self.assertEqual(rental.book_id, 1)
        self.assertEqual(rental.client_id, 100)
        self.assertEqual(rental.rented_date, 2024-10-1)
        self.assertEqual(rental.returned_date, 2024 - 10 - 10)
        self.assertIsInstance(rental, Rental)