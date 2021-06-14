from board_class import Board
import os
def main():
    width = int(os.get_terminal_size()[0] / 2)
    height = os.get_terminal_size()[1] - 2
    num_of_mines = int(width * height / 4.84)
    mine_sweeper = Board(height, width)
    mine_sweeper.print_board()
    mine_sweeper.add_mines(num_of_mines)
    mine_sweeper.print_board()
    for i in range(width):
        for j in range(height):
            mine_sweeper.configure_board(j, i)
    mine_sweeper.print_board()
    input("Print something")
if __name__ == "__main__":
    main()
