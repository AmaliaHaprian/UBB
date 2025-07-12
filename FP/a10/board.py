from enum import Enum
from texttable import Texttable
from validators.errors import InvalidMove

class Symbol(Enum):
    X=0
    O=1

class Board:
    def __init__(self,size:int):
        """
        ' ' - empty space
         .  - inaccessible space
         X  -human move
         O  -computer move
        :param size: the size of the board
        """
        self._data=[]
        self._size=size
        for i in range(size):
            self._data.append([0]*size)

        self.__free_spaces=[]
        for i in range(size):
            for j in range(size):
                self.__free_spaces.append((i+1,j+1))

    def board(self):
        """

        :return: the list representing the board
        """

        return self._data

    def size(self):
        """

        :return: the size of the board
        """
        return self._size

    def get_symbol(self,row:int,col:int)->str:
        """
        The function return the symbol corresponding to the given row and col
        :param row: row of the board
        :param col: column of the board
        :return: the symbol corresponding to the given row and col
        """

        if self._data[row-1][col-1]==1:
            return 'X'
        elif self._data[row-1][col-1]==2:
            return 'O'
        elif self._data[row-1][col-1]==3:
            return '.'
        else:
            return ' '

    def hit(self,symbol:str,row:int,col:int):
        """
        The function makes a move on the board and blocks the cells around. It raises an error if the given cell is already occupied
        :param symbol: X / O , depending on the player who made the move
        :param row: the row where to move
        :param col: the column where to move
        :return: None
        """

        row-=1
        col-=1
        if self._data[row][col]!=0:
            raise InvalidMove

        self._data[row][col]=1 if symbol=='X' else 2
        self.__free_spaces.remove((row+1,col+1))

        if col !=self._size-1:
            if self._data[row][col+1]==0:
                self._data[row][col + 1]=3
                self.__free_spaces.remove((row + 1, col + 2))
        if col !=0:
            if self._data[row][col-1]==0:
                self._data[row][col - 1] = 3
                self.__free_spaces.remove((row + 1, col))
        if row !=0 and col !=self._size-1:
            if self._data[row-1][col+1]==0:
                self._data[row-1][col + 1] = 3
                self.__free_spaces.remove((row, col + 2))
        if row != 0 and col != 0:
            if self._data[row-1][col-1]==0:
                self._data[row-1][col - 1] = 3
                self.__free_spaces.remove((row, col))
        if row !=0:
            if self._data[row-1][col]==0:
                self._data[row-1][col] = 3
                self.__free_spaces.remove((row, col + 1))
        if row !=self._size-1 and col !=self._size-1:
            if self._data[row+1][col+1]==0:
                self._data[row+1][col + 1] = 3
                self.__free_spaces.remove((row + 2, col + 2))
        if row != self._size-1 and col != 0:
            if self._data[row+1][col-1]==0:
                self._data[row+1][col - 1] = 3
                self.__free_spaces.remove((row + 2, col))
        if row !=self._size-1:
            if self._data[row+1][col]==0:
                self._data[row+1][col] = 3
                self.__free_spaces.remove((row + 2, col + 1))

    def free_spaces(self):
        """

        :return: A list with the all the free spaces
        """

        return self.__free_spaces

    def __str__(self):
        t=Texttable()
        #t.header(['/','1','2','3','4','5','6'])
        list=['/']
        for i in range(self._size):
            list.append(i+1)
        t.header(list)
        for row in range(self._size):
            row_data=[row+1]+[' ']*self._size
            for col in range(self._size):
                symbol=' '
                if self._data[row][col]==1: #human hit
                    symbol='X'
                elif self._data[row][col]==2: #computer hit
                    symbol='O'
                elif self._data[row][col]==3: #inaccessible place
                    symbol='.'
                row_data[col+1]=symbol
            t.add_row(row_data)
        return t.draw()
