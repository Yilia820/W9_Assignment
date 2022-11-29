# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class Game:
    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self, board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None.
    
        a = board[0][0]
        b = board[0][1]
        c = board[0][2]
        if a == b and b == c and c == 'O':
            return 'O'
        elif a == b and b == c and c == 'X':
            return 'X'

        d = board[1][0]
        e = board[1][1]
        f = board[1][2]
        if d == e and e == f and f =='O':
            return 'O'
        elif d == e and e == f and f == 'X':
            return 'X'
        
        g = board[2][0]
        h = board[2][1]
        i = board[2][2]
        if g == h and h == i and i =='O':
            return 'O'
        elif g == h and h == i and i == 'X':
            return 'X'    """
        
        for x in range(3):
            container = ""

            for y in range (3):
                container = container +str(board[x][y])

            if container == "OOO":
                return "O"

            elif container == "XXX":
                return "X"

        for x in range(3):
            container = ""
            for y in range (3):
                container = container +str(board[y][x])
            if container == "OOO":
                return "O"
            elif container == "XXX":
                return "X"

        container = ""
        for x in range(3):     
            container = container + str(board[x][x])
            if container == "OOO":
                return "O"
            elif container == "XXX":
                return "X"
                
        container = ""
        for x in range(3):
            container = container + str(board[2-x][x])
            if container == "OOO":
                return "O"
            elif container == "XXX":
                return "X"
        return None



    def other_player(self, player):
        """Given the character for a player, returns the other player."""
        if player == 'O':
            return 'X'
        if player == 'X':
            return 'O'
