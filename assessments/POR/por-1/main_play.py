from game_conditions import GameLogic
from game_loop import TicTacToeBoard

print("Welcome to Game World!!!")
player_one = "X"
player_two = "O"
empty_cells = " "

tic_board = TicTacToeBoard()
game_play = GameLogic()


def game_playing():
    current_player = player_one if sum(row.count(empty_cells) for row in tic_board.board) % 2 == 1 else player_two
    while True:
        tic_board.show_board()
        move = input(f"Enter for player {current_player} (0-8):")

        try:

            if move.isdigit():
                move = int(move)
                row = move // 3
                col = move % 3

                if 0 <= row < 3 and 0 <= col < 3 and tic_board.board[row][col] == empty_cells:
                    tic_board.board[row][col] = current_player

                    if current_player == player_one:

                        current_player = player_two
                    else:
                        current_player = player_one

                    winner = game_play.check_win_chance(tic_board.board)

                    if winner:
                        tic_board.show_board()
                        print(f"Player {winner} wins!!!")
                        break

                    if game_play.check_tie(tic_board.board):
                        tic_board.show_board()
                        break

                else:
                    print("Invalid move, try again!")
            else:
                print("Invalid move, Please enter a number between 0-8")
        except ValueError:
            print("Invalid input. Please enter a valid number between 0-8")


game_playing()
