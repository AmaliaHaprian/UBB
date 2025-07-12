import copy
import random
from board import Board


class Strategy:
    pass

class AI(Strategy):
    #def __init__(self,board:Board):
     #   self.__board=copy.deepcopy(board)

    def evaluate(self, board, maximizing_player:bool):
        """

        :param maximizing_player: True if it is maximizing player's turn, false otherwise
        :return: -1 if the minimizer won, 1 otherwise
        """

        #board=self.__board.board()

        if maximizing_player: #if it was maximizing player turn, but the board is full, then the minimizing player made the last move, so he won
            return -1

        return 1
    def undo_move(self,row:int,col:int, board:Board):
        b=board
        b.board()[row-1][col-1]=0
        b.free_spaces().append((row,col))
        size=b.size()
        col-=1
        row-=1
        if col !=size-1:
            if b.board()[row][col+1]==3:
                self.__board.board()[row][col + 1]=0
                self.__board.free_spaces().append((row+1,col+2))
        if col !=0:
            if self.__board.board()[row][col-1]==3:
                self.__board.board()[row][col - 1] = 0
                self.__board.free_spaces().append((row+1,col))
        if row !=0 and col !=size-1:
            if self.__board.board()[row-1][col+1]==3:
                self.__board.board()[row-1][col + 1] = 0
                self.__board.free_spaces().append((row,col+2))
        if row != 0 and col != 0:
            if self.__board.board()[row-1][col-1]==3:
                self.__board.board()[row-1][col - 1] = 0
                b.free_spaces().append((row,col))
        if row !=0:
            if self.__board.board()[row-1][col]==3:
                self.__board.board()[row-1][col] = 0
                self.__board.free_spaces().append((row,col+1))
        if row !=size-1 and col !=size-1:
            if self.__board.board()[row+1][col+1]==3:
                self.__board.board()[row+1][col + 1] = 0
                self.__board.free_spaces().append((row+2,col+2))
        if row != size-1 and col != 0:
            if self.__board.board()[row+1][col-1]==3:
                self.__board.board()[row+1][col - 1] = 0
                self.__board.free_spaces().append((row+2,col))
        if row !=size-1:
            if self.__board.board()[row+1][col]==3:
                self.__board.board()[row+1][col] = 0
                self.__board.free_spaces().append((row+2,col+1))

    def minimax(self,depth:int, maximizing_player:bool, board:Board):
        """

        :param depth: the depth to which the minimax algorithm will go
        :param maximizing_player: True if it is maximizing player's turn, false otherwise'
        :param board: the board corresponding to the game
        :return: the evaluation of the game
        """

        b=board
        if len(b.free_spaces())==0:
            return self.evaluate(b,maximizing_player)
        if depth ==0 :
            return 0
        if self.winning_move(b) is not None:
            return self.evaluate(b,not maximizing_player)

        if maximizing_player:
            max_score=-10000
            for move in b.free_spaces():
                copy_board=copy.deepcopy(b)
                copy_board.hit('O',move[0],move[1])
                score=self.minimax(depth-1,False, copy_board)
                #self.undo_move(move[0],move[1])
                max_score=max(max_score,score)
            return max_score
        else:
            min_score=10000
            for move in b.free_spaces():
                copy_board=copy.deepcopy(b)
                copy_board.hit('X',move[0],move[1])
                score=self.minimax(depth-1,True, copy_board)
                #self.undo_move(move[0],move[1])
                min_score=min(min_score,score)
            return min_score

    def play(self,board:Board):
        """
        The function determines the best move the computer can make, through the minimax algorithm
        :param board: the current board
        :return: the best move to make
        """

        best_score=-10000
        best_move=None

        for move in board.free_spaces():
            first_copy=copy.deepcopy(board)
            first_copy.hit('O',move[0],move[1])
            score=self.minimax(2                                                                                                                                    ,False ,first_copy)
            #self.undo_move(move[0],move[1])
            if score>=best_score:
                best_score=score
                best_move=move
        if best_move is not None:
            board.hit('O',best_move[0],best_move[1])
        return best_move

    def winning_move(self, board:Board)->tuple or None:
        """
        The function checks if a move from the free spaces is a winning move
        :param board: the current board
        :return: The winning move if any, None otherwise
        """

        for move in board.free_spaces():
            copy_board = copy.deepcopy(board)
            copy_board.hit('O',move[0],move[1])
            if len(copy_board.free_spaces())==0:
                return move
        return None


class RandomStrategy(Strategy):
    """
    The computer makes a random move on the board, from the free spaces. It does not try to win or play defensively
    """

    def play(self, board: Board)->tuple or None :
        if len(board.free_spaces())==0:
            return None
        move = random.choice(board.free_spaces())
        board.hit('O', move[0], move[1])
        return move

class SmartStrategy(Strategy):
    """
    The smart strategy the computer can play. It checks if there is a winning move and it also plays defensively
    """

    def play(self, board: Board)->tuple or None :
        winning_move=self.winning_move(board)
        if winning_move:
            board.hit('O', winning_move[0], winning_move[1])
            return winning_move
        if len(board.free_spaces())==0:
            return None
        possible_moves=self.defensive_move(board)
        if possible_moves:
            move=random.choice(possible_moves)
            board.hit('O',move[0],move[1])
            return move
        move=random.choice(board.free_spaces())
        board.hit('O',move[0],move[1])
        return move

    def winning_move(self, board:Board)->tuple or None:
        """
        The function checks if a move from the free spaces is a winning move
        :param board: the current board
        :return: The winning move if any, None otherwise
        """
        for move in board.free_spaces():
            copy_board = copy.deepcopy(board)
            copy_board.hit('O',move[0],move[1])
            if len(copy_board.free_spaces())==0:
                return move
        return None

    def defensive_move(self,board:Board)->tuple or None:
        possible_moves=[]
        for move in board.free_spaces():
            copy_board=copy.deepcopy(board)
            copy_board.hit('O',move[0],move[1])
            if not self.winning_move(copy_board):
                possible_moves.append(move)
        return possible_moves


class Game:
    def __init__(self, size:int, computer_strategy):
        """
        Game class - implements the actual game functions
        :param size: The size of the board
        :param computer_strategy: the time of strategy the computer plays: Random, Smart or Minimax
        """

        self._size=size
        self.__board=Board(size)
        self.__strategy=computer_strategy

    def get_board(self)->Board:
        """

        :return: The current board
        """

        return self.__board

    def get_strategy(self):
        """

        :return: The current strategy
        """
        return self.__strategy

    def move_human(self,row:int,col:int):
        """

        :param row: the row where the human wants to move
        :param col: the column where the human wants to move
        :return: None
        """

        self.__board.hit('X',row,col)

    def move_computer(self)->tuple:
        """
        The function calls the playing implementation of the computer strategy and return the move the computer made
        :return:
        """

        return self.__strategy.play(self.__board)


