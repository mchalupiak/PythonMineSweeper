from board_class import Board
import os
from board_class import Board
from functions import add_mines

def main():	
    mine_sweeper = Board(7, 7)
    mine_sweeper.print_board()
    add_mines(14, mine_sweeper)
    mine_sweeper.print_board()

if __name__ == "__main__":
    main()