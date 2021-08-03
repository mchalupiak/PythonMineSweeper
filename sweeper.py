from board_class import Board
import os

def main():
    width = int(os.get_terminal_size()[0] / 2)
    height = os.get_terminal_size()[1] - 2
    num_of_mines = int(width * height / 4.84)
    mine_sweeper = Board(height, width, num_of_mines)
    mine_sweeper.print_board()
    mine_sweeper.print_board()
    for i in range(width):
        for j in range(height):
            mine_sweeper.configure_board(j, i)
    mine_sweeper.print_board()
    while mine_sweeper.game_over == False:
        x_pos = input("Enter an X coordinate: ")
        y_pos = input("Enter a Y coordinate: ")
        mine_sweeper.make_move(int(x_pos), int(y_pos))
        mine_sweeper.print_board()
if __name__ == "__main__":
    main()
