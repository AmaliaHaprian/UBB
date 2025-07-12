from enum import Enum

import pygame
from game import Game, SmartStrategy
from validators.errors import InvalidMove


class CELLState(Enum):
    EMPTY = 0
    X = 1
    O = 2
    BLOCKED = 3

class Cell(pygame.sprite.Sprite):
    def __init__(self, main_surface, dimension, position, color):
        super().__init__()
        self.main_surface=main_surface
        self.color=color
        self.surface=pygame.Surface([dimension, dimension])
        self.surface.fill(self.color)
        self.__rectangle=self.surface.get_rect(topleft=position)
        self.state=CELLState.EMPTY

    def draw(self):
        self.main_surface.blit(self.surface, self.__rectangle)
        pygame.draw.rect(self.surface, color='black', rect=(0, 0, self.surface.get_width(), self.surface.get_height()), width=2) # draw margin

    def draw_x(self):
        pygame.draw.line(self.surface, 'black',  (0 , 0), (self.surface.get_width(), self.surface.get_height()), width=3)
        pygame.draw.line(self.surface, 'black', (0, self.surface.get_height()), (self.surface.get_width(), 0), width=3)

    def draw_o(self):
        pygame.draw.circle(self.surface, 'black', (self.surface.get_width()//2, self.surface.get_height()//2), 50, width=3)

    def block(self):
        self.surface.fill('gray')

    def free(self):
        self.surface.fill(self.color)

class GuiBoard(pygame.sprite.Sprite):
    def __init__(self, main_surface,size):
        super().__init__()
        self.main_surface=main_surface
        self.size=size
        self.surface=pygame.Surface([600, 600])
        self.cell_side=600//size
        self.board=[]
        for row in range(self.size):
            self.board.append([])
            for col in range(self.size):
                self.board[row].append(Cell(self.surface, self.cell_side, (self.cell_side*row, self.cell_side*col), 'white'))

    def get(self, row, col):
        return self.board[row][col]
    def draw(self):
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col].draw()
        self.main_surface.blit(self.surface, self.surface.get_rect())

    def update(self):
        for row in range(self.size):
            for col in range(self.size):
                state_dict = {CELLState.X: self.board[row][col].draw_x,
                              CELLState.O: self.board[row][col].draw_o,
                              CELLState.EMPTY: self.board[row][col].free,
                              CELLState.BLOCKED: self.board[row][col].block}
                state_dict[self.board[row][col].state]()

class GUI:
    def __init__(self,size,strategy):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("OBSTRUCTION GAME")
        self.size=size
        self.game=Game(self.size,strategy())
        self.board=GuiBoard(self.screen, self.size)
        self.cell_side=600//size
        print(self.cell_side)
        run=True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    x=pos[0]//self.cell_side
                    y=pos[1]//self.cell_side
                    if self.handle_human(x,y) is not -1:
                        if len(self.game.get_board().free_spaces())==0:
                            run=False
                            self.display_winner('You')
                            break
                        #print(self.game.get_board().free_spaces())
                        self.handle_computer()
                        if len(self.game.get_board().free_spaces())==0:
                            run=False
                            self.display_winner('Computer')
                        #print(self.game.get_board().free_spaces())

            self.screen.fill('white')
            self.board.draw()
            pygame.display.flip()
        pygame.quit()

    def display_winner(self, winner):
        font=pygame.font.SysFont('Times New Roman', 45)
        text=font.render('{} won the game!'.format(winner), True, 'dark green')
        textRect=text.get_rect(center=(300, 300))
        self.board.draw()
        self.screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def handle_human(self,x,y):
        try:
            self.game.move_human(y + 1, x + 1)
            self.block_around(x,y)
            cell = self.board.get(x,y)
            cell.state = CELLState.X
            self.board.update()
            self.screen.fill('white')
            self.board.draw()
            pygame.display.flip()
        except InvalidMove:
            return -1

    def handle_computer(self):
        move=self.game.move_computer()
        if move is None:
            return
        print("computer move:",move[0],move[1])
        self.block_around(move[1]-1,move[0]-1)
        cell=self.board.get(move[1]-1,move[0]-1)
        cell.state=CELLState.O
        self.board.update()
        self.screen.fill('white')
        self.board.draw()
        pygame.display.flip()

    def block_around(self,row, col):
        directions=[-1,0,1]
        for row_d in directions:
            for col_d in directions:
                if 0 <= row+row_d < self.size and 0 <= col + col_d < self.size:
                    #print(self.board.get(row+row_d,col+col_d).state)
                    self.board.get(row+row_d,col+col_d).state=CELLState.BLOCKED
