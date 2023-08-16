class TicTacToeBoard:
    def __init__(self):
        self.empty = " "
        self.board = [[self.empty for _ in range(3)] for _ in range(3)]

    def show_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("__________")

