# class Tictactoe:
#     def __init__(self):
#         self.empty = " "
#         self.rows = 3
#         self.columns = 3
#         self.board = [[self.empty for _ in range(self.rows)] for _ in range(self.columns)]
#         self.p1 = "X"
#         self.p2 = "O"
#         self.current_player = self.p1
#
#
#     def show_board(self):
#         for row in self.board:
#             print(" | ".join(row))
#             print("__________")
#
#     def check_win_chances(self):
#         win_chances = [
#             [(0, 0), (0, 1), (0, 2)],  # Top row
#             [(1, 0), (1, 1), (1, 2)],  # Middle row
#             [(2, 0), (2, 1), (2, 2)],  # Bottom row
#             [(0, 0), (1, 0), (2, 0)],  # Left column
#             [(0, 1), (1, 1), (2, 1)],  # Middle column
#             [(0, 2), (1, 2), (2, 2)],  # Right column
#             [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
#             [(0, 2), (1, 1), (2, 0)],  # Diagonal from top-right to bottom-left
#         ]
#         for win in win_chances:
#             cells = [self.board[row][col] for row, col in win]
#             if len(set(cells)) == 1 and cells[0] != self.empty:
#                 return True, cells[0]
#             else:
#                 return False, None
#
#     def check_tie(self):
#         for row in self.board:
#             if self.empty in row:
#                 return False
#         print("It is a tie.")
#         return True
#
#     def game_play(self):
#         while True:
#             self.show_board()
#             move = input(f"Enter for player {self.current_player} (0-8):")
#
#             try:
#
#                 if move.isdigit():
#                     move = int(move)
#                     row = move // self.rows
#                     col = move % self.columns
#
#                     if 0 <= row < self.rows and 0 <= col < self.columns and self.board[row][col] == self.empty:
#                         self.board[row][col] = self.current_player
#
#                         if self.current_player == self.p1:
#                             self.current_player = self.p2
#                         else:
#                             self.current_player = self.p1
#
#                         win, winner = self.check_win_chances()
#                         print("win:" ,win)
#                         print("winner:" ,winner)
#                         if win:
#                             self.show_board()
#                             print(f"Player {winner} wins!!!")
#                             break
#
#                         if self.check_tie():
#                             self.show_board()
#                             break
#
#                     else:
#                         print("Invalid move, try again!")
#                 else:
#                     print("Invalid move, Please enter a number between 0-8")
#             except ValueError:
#                 print("Invalid input. Please enter a valid number between 0-8")



# from game_conditions import Tictactoe
#
#
# def main_program():
#     tic_tac_toe = Tictactoe()
#     #tic_tac_toe.show_board()
#     tic_tac_toe.game_play()