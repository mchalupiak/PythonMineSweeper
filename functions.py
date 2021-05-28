from random import randint
from board_class import Board

def add_mines(num_of_mines, board):
    used_x = []
    used_y = []
    i = 1
    while i <= num_of_mines:
        x_pos = randint(0, board.width - 1)
        y_pos = randint(0, board.height - 1)
        if not(x_pos in used_x) and not(y_pos == used_y[used_x.index(x_pos)]):
            board.update_board(x_pos, y_pos, '\033[91mM\033[0m') 
            used_x.append(x_pos)
            used_y.append(y_pos)
        i += 1