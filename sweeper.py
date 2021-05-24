import os


class Board:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = [['X'] * self.width] * self.height
	
	def print_board(self):
		for i in range(self.width):
			for j in range(self.height):
				print(self.board[i][j], end=' ')
			print('')
		print('')

	def update_board(self, pos_x, pos_y):
		self.board[pos_x][pos_y] = 'w'

def main():	
	mine_sweeper = Board(7, 7)
	mine_sweeper.print_board()
	mine_sweeper.update_board(4, 3)
	mine_sweeper.print_board()

if __name__ == "__main__":
	main()