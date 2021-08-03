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
        user_input = input("What move would you like to make? ('move' to uncover a space, 'flag' to flag a space) ")
        mine_sweeper.clear_screen()
        mine_sweeper.make_move(user_input.lower())
        mine_sweeper.print_board()
if __name__ == "__main__":
    main()
