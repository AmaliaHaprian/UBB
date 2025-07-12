from unittest import TestCase

from board import Board
from validators.errors import InvalidMove


class TestBoard(TestCase):
    def setUp(self):
        self.__board=Board(6)

    def test_size(self):
        self.assertEqual(self.__board.size(),6)

    def test_free_spaces(self):
        self.assertEqual(len(self.__board.free_spaces()), 36)

    def test_get_symbol(self):
        self.assertEqual(self.__board.get_symbol(1,1),' ')

    def test_hit(self):
        self.__board.hit('X',1,1)
        self.assertEqual(self.__board.get_symbol(1,1),'X')
        self.assertEqual(len(self.__board.free_spaces()), 32)

        self.__board.hit('O', 6,6)
        self.assertEqual(self.__board.get_symbol(6,6), 'O')

        self.assertRaises(InvalidMove, self.__board.hit, 'X', 1, 1)

        self.assertEqual(self.__board.get_symbol(1,2),'.')

