from random import randint
# This class define the entire game board
# It will be used to create two boards, one for storing what the player sees and one for storing the underlying mines and mine numbers around a given block
# I'm new to classes in python (or anywhere else), so this file will be heavily commented
class Board:

    # This function defines parameters when an instance of the class is created. Here we give it a width and height for the number of positions
    # Later on I will add logic to prevent it from exceeding the terminal window width and height
    # board_mask is what the player will see, and board is used to store things like where the mines are and how many mines area around a given point
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_mask = [['X'] * self.width for _ in range(self.height)]
        self.board = [[0] * self.width for _ in range(self.height)]
        self.mine = "\033[91mM\033[0m"

    # Just a handy helper function to print the board out when I need it
    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.board[j][i], end=' ')
            print('')
        print('')

    # add_mines adds mines at a random positions across the board
    # Mines are red, even though in hindsight the player won't see the mines
    def add_mines(self, num_of_mines):
        mines_remaining = num_of_mines
        running = True
        while running:
            for j in range(self.width):
                for k in range(self.height):
                    if mines_remaining == 0:
                        running = False
                    elif self.board[k][j] != self.mine and randint(1, self.width * self.height) == 1:
                        mines_remaining -= 1
                        self.board[k][j] = self.mine

    def is_mine(self, x_pos, y_pos):
        try:
            if x_pos < 0 or y_pos < 0:
                return False

            elif self.board[y_pos][x_pos] == self.mine:
                return True

            else:
                return False
        except IndexError:
            return False

    def configure_board(self, x_pos, y_pos):
        if not self.is_mine(x_pos, y_pos):
            surrounding_spaces = [[x_pos - 1, y_pos - 1], [x_pos, y_pos - 1], [x_pos + 1, y_pos - 1], [x_pos - 1, y_pos], [x_pos + 1, y_pos], [x_pos - 1, y_pos + 1], [x_pos, y_pos + 1], [x_pos + 1, y_pos + 1]]
            mines_around = [False] * len(surrounding_spaces)
            for i in range(8):
                mines_around[i] = (self.is_mine(surrounding_spaces[i][0], surrounding_spaces[i][1]))
            for j in range(len(mines_around)):
                if mines_around[j] == True:
                    self.board[y_pos][x_pos] += 1
