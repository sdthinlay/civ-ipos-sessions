class GameLogic:
    def check_win_chance(self, board):
        reversed_board = list(zip(*board))
        for row in board:
            horizontal_win = set(row)
            if len(horizontal_win) == 1 and " " not in horizontal_win:
                #   print("Player", horizontal_win.pop, "wins")
                return horizontal_win.pop()
        for row in reversed_board:
            reversed_horizontal_win = set(row)
            if len(reversed_horizontal_win) == 1 and " " not in reversed_horizontal_win:
                # print("Player", reversed_horizontal_win.pop, "wins")
                return reversed_horizontal_win.pop()

        main_diagonal = [board[i][i] for i in range(len(board))]
        diagonal_win = set(main_diagonal)
        if len(diagonal_win) == 1 and " " not in diagonal_win:
            # print("Player", diagonal_win.pop,"wins")
            return diagonal_win.pop()

        anti_diagonal = [board[i][len(board) - 1 - i] for i in range(len(board))]
        anti_diagonal_win = set(anti_diagonal)
        if len(anti_diagonal_win) == 1 and " " not in anti_diagonal:
            # print("Player", anti_diagonal_win.pop(),"wins")
            return anti_diagonal_win.pop()
        return False

    def check_tie(self, board):
        for row in board:
            if " " in row:
                return False
        print("It is a tie.")
        return True

