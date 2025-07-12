from unittest import TestCase

from board import Board
from game import Game, RandomStrategy, SmartStrategy, AI


class TestGame(TestCase):
    def test_game(self):
        game = Game(6, SmartStrategy())
        board=game.get_board()
        strategy=game.get_strategy()
        self.assertEqual(type(strategy), SmartStrategy)
        self.assertEqual(game.get_board().size(), 6)
        self.assertEqual(game.get_board(), board)

        game.move_human(1,1)
        self.assertEqual(game.get_board().get_symbol(1,1),'X')
        self.assertEqual(board.get_symbol(1,1), 'X')

        move=game.move_computer()
        self.assertEqual(board.get_symbol(move[0],move[1]),'O')

    def test_smart_strategy(self):
        game = Game(3, SmartStrategy())
        board=game.get_board()
        strategy=game.get_strategy()
        self.assertEqual(type(strategy), SmartStrategy)
        self.assertEqual(game.get_board().size(), 3)
        self.assertEqual(game.get_board(), board)

        move=strategy.winning_move(board)
        self.assertEqual(move,(2,2))

        possible_moves=strategy.defensive_move(board)
        self.assertEqual(possible_moves,[(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)])

        game.move_human(2,2)
        possible_moves=strategy.defensive_move(board)
        self.assertEqual(possible_moves,[])

    def test_random_strategy(self):
        game = Game(2, RandomStrategy())
        board=game.get_board()
        strategy=game.get_strategy()
        self.assertEqual(type(strategy), RandomStrategy)
        self.assertEqual(game.get_board().size(), 2)
        self.assertEqual(len(board.free_spaces()), 4)
        move=strategy.play(board)
        self.assertIsNot(move,None)

        move=strategy.play(board)
        self.assertEqual(move, None)

    def test_ai(self):
        game=Game(3,AI())
