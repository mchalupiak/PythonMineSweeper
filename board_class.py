from random import randint
import os
# This class define the entire game board
# It will be used to create two boards, one for storing what the player sees and one for storing the underlying mines and mine numbers around a given block
# I'm new to classes in python (or anywhere else), so this file will be heavily commented
class Board:

    # This function defines parameters when an instance of the class is created. Here we give it a width and height for the number of positions
    # Later on I will add logic to prevent it from exceeding the terminal window width and height
    # board_mask is what the player will see, and board is used to store things like where the mines are and how many mines area around a given point
    def __init__(self, width, height, num_of_mines):
        self.width = width
        self.height = height
        self.board_mask = [['X'] * self.width for _ in range(self.height)]
        self.board = [[0] * self.width for _ in range(self.height)]
        self.mine = "\033[91mM\033[0m"
        self.num_of_mines = num_of_mines
        self.num_of_open_spaces = (self.width * self.height) - num_of_mines
        self.num_of_unflagged_mines = num_of_mines
        self.game_over = False
        running = True
        while running:
            for j in range(self.width):
                for k in range(self.height):
                    if num_of_mines == 0:
                        running = False
                    elif self.board[k][j] != self.mine and randint(1, self.width * self.height) == 1:
                        num_of_mines -= 1
                        self.board[k][j] = self.mine
    # Just a handy helper function to print the board out when I need it
    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.board_mask[j][i], end=' ')
            print('')
        print('')

    def is_val(self, x_pos, y_pos, val):
        try:
            if x_pos < 0 or y_pos < 0:
                return False

            elif self.board[y_pos][x_pos] == val:
                return True

            else:
                return False
        except IndexError:
            return False

    def end_screen(self, did_win):
        self.game_over = True

    def configure_board(self, x_pos, y_pos):
        if not self.is_val(x_pos, y_pos, self.mine):
            surrounding_spaces = [[x_pos - 1, y_pos - 1], [x_pos, y_pos - 1], [x_pos + 1, y_pos - 1], [x_pos - 1, y_pos], [x_pos + 1, y_pos], [x_pos - 1, y_pos + 1], [x_pos, y_pos + 1], [x_pos + 1, y_pos + 1]]
            mines_around = [False] * len(surrounding_spaces)
            for i in range(8):
                mines_around[i] = (self.is_val(surrounding_spaces[i][0], surrounding_spaces[i][1], self.mine))
            for j in range(len(mines_around)):
                if mines_around[j] == True:
                    self.board[y_pos][x_pos] += 1

    def make_move(self, user_input):

       if self.num_of_open_spaces <= 0 or self.num_of_unflagged_mines <= 0:
            self.end_screen(True)

       x_pos = int(input("Enter an X coordinate: "))
       self.clear_screen()
       y_pos = int(input("Enter a Y coordinate: "))
       self.clear_screen()

       if user_input == "move":
            self.board_mask[y_pos][x_pos] = self.board[y_pos][x_pos]
            if self.is_val(x_pos, y_pos, self.mine):
                self.end_screen(False)
            self.num_of_open_spaces -= 1

       elif user_input == "flag":
            self.board_mask[y_pos][x_pos] = "\033[91mF\033[0m"
            self.num_of_unflagged_mines -= 1

    def clear_screen(self):
        if os.name == 'posix':
            os.system("clear")

        elif os.name == 'nt':
            os.system("cls")

        self.print_board()
