from board import Board
from game import Game, SmartStrategy, AI
from validators.errors import InvalidMove
from validators.validator import Validator


class UI:
    def __init__(self, size:int,validate:Validator, strategy):
        self.__board_size=size
        self.__game=Game(self.__board_size, strategy() )
        self.__validate=validate


    def move(self)->tuple[int,int]:
        print("Enter the coordinates:")
        hit_row = input("X=")
        hit_col = input("Y=")

        try:
            hit_row=int(hit_row)
            hit_col=int(hit_col)
            if self.__validate.validate_coordinate(hit_row, 1, self.__board_size) and self.__validate.validate_coordinate(hit_col, 1, self.__board_size):
                return hit_row, hit_col
            else:
                print("Invalid coordinates. Integer between 1 and", self.__board_size)
                return self.move()
        except ValueError:
            print("Invalid coordinates. Integers expected")
            return self.move()

    def play(self):
        is_player_turn=True
        board=self.__game.get_board()
        while True:
            print(board)
            if is_player_turn:
                try:
                    row, col = self.move()
                    self.__game.move_human(row,col)
                except InvalidMove:
                    print("Invalid move. Cell is not free.Try again")
                    row,col=self.move()
                    self.__game.move_human(row,col)
            else:
                move=self.__game.move_computer()
                if move:
                    print("Computer moved at",move[0],move[1])
                else:
                    print("Computer has no more moves.You win")
                    break
            if len(board.free_spaces())==0:
                if is_player_turn:
                    print("You won")
                    print(self.__game.get_board())
                else :
                    print("Computer won")
                    print(self.__game.get_board())
                break
            is_player_turn = not is_player_turn

if __name__=='__main__':
    validator=Validator()
    size=int(input("What should the size of the board be?"))
    ui=UI(size, validator)
    ui.play()