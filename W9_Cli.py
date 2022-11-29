# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from W9_Logic import Game
def show_board(board):
    for x in range(3):
        for y in range(3):
            print(board[x][y],end=" ")
        print('\n')

if __name__ == '__main__':
    game=Game()
    board = game.make_empty_board()
    winner = None
    player = "O"
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        show_board(board)
        # TODO: Input a move from the player.
        x = input("[x]")
        y = input("[y]")
        # TODO: Update the board.
        board[int(x)][int(y)]= player
        show_board(board)
        player = game.other_player(player)
        # TODO: Update who's turn it is.
        winner = game.get_winner(board)
    print(winner)