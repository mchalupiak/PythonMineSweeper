from board_class import Board

def main():	
    mine_sweeper = Board(7, 7)
    mine_sweeper.print_board()
    mine_sweeper.add_mines(5)
    mine_sweeper.print_board()

if __name__ == "__main__":
    main()