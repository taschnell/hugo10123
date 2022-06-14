"""
Module tic_tac_toe contains the TicTacToe class, instances of which model Tic-Tac-Toe games.
"""
__author__ = "Teo Schnell, taschnell@jeff.cis.cabrillo.edu"


class TicTacToe:
    """
    Models a game of Tic-Tac-Toe. Player can be given names, but are still represented as
    'X' and 'O'
    on the grid. X has the first turn.
    Grid squares are claimed by calling the mark() method. Row and
    column values are specified by indexes 0–2.
    """

    players = ["X", "O"]
    play = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    index = 0
    index_2 = 0
    playernames = []
    win_player = None
    game_state = True

    def __init__(self, x="X", o="O"):
        """
        Initializes a Tic-Tac-Toe game with player names defaulting to 'X' and 'O'.
        Turns alternate, with player x getting the first turn.

        >>> g = TicTacToe()
        >>> bool(g)
        True
        >>> g.winner()
        >>> print(g)
        |_|_|_|
        |_|_|_|
        |_|_|_|
        >>> g.mark(1, 1)
        >>> print(g)
        |_|_|_|
        |_|X|_|
        |_|_|_|
        """
        self.playernames = [x, o]
        self.gamestate = True
        self.players = ["X", "O"]
        self.play = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.index = 0
        self.index_2 = 0
        self.win_player = None
        pass

    def __bool__(self):
        """
        A Tic-Tac-Toe game is
        considered Boolean True if it is still in play, i.e. there is no winner
        and possible moves remain.

        >>> g = TicTacToe()
        >>> for move in ((0, 0), (1, 0), (1, 1), (2, 0), (2, 2)):
        ...   g.mark(*move)
        ...   print(bool(g))
        ...
        True
        True
        True
        True
        False
        """

        if self.winner() is not None:
            self.game_state = False
        elif None in self.grid():
            self.game_state = True
        else:
            self.game_state = False
        return self.game_state

    def __str__(self):
        """
        Returns a string representation of the game grid, formatted as in the following:

        >>> g = TicTacToe()
        >>> for move in ((0, 0), (1, 0), (1, 1), (2, 0), (2, 2)):
        ...   g.mark(*move)
        ...   print(g)
        ...
        |X|_|_|
        |_|_|_|
        |_|_|_|
        |X|_|_|
        |O|_|_|
        |_|_|_|
        |X|_|_|
        |O|X|_|
        |_|_|_|
        |X|_|_|
        |O|X|_|
        |O|_|_|
        |X|_|_|
        |O|X|_|
        |O|_|X|
        """
        output_grid_1 = "|"
        output_grid_2 = "|"
        output_grid_3 = "|"

        for value in self.play[0:3]:
            output_grid_1 += value + "|"
        for value in self.play[3:6]:
            output_grid_2 += value + "|"
        for value in self.play[6:]:
            output_grid_3 += value + "|"

        x = output_grid_1, output_grid_2, output_grid_3
        output_grid = "\n".join(x)

        return output_grid

    def grid(self):
        """
        Returns a tuple representing
        the state of the grid, consisting of 9 values that are either the
        string 'X', the
        string 'O', or None. grid()[:3] represents the first row, grid()[3:6] represents
        the second row, and grid()[6:] the third row.

        >>> g = TicTacToe()
        >>> for move in ((0, 0), (1, 0), (1, 1), (2, 0), (2, 2)):
        ...   g.mark(*move)
        ...   g.grid()
        ...
        ('X', None, None, None, None, None, None, None, None)
        ('X', None, None, 'O', None, None, None, None, None)
        ('X', None, None, 'O', 'X', None, None, None, None)
        ('X', None, None, 'O', 'X', None, 'O', None, None)
        ('X', None, None, 'O', 'X', None, 'O', None, 'X')
        """
        output = []
        for element in self.play:
            if element == "_":
                output.append(None)
            elif element == "X":
                output.append("X")
            elif element == "O":
                output.append("O")

        return tuple(output)

    def mark(self, row: int, col: int):
        """
        Takes a turn by marking the given row and column (0–2) with the current player.
        Turns alternate, with player x getting the first turn. Raises a ValueError if the turn is
        invalid, i.e. if the row and column were already claimed or out of bounds, or the game is
        no longer in play.

        >>> g = TicTacToe()
        >>> for move in ((0, 0), (1, 0), (1, 1), (2, 0), (2, 2)):
        ...   g.mark(*move)
        ...   print(g)
        ...
        |X|_|_|
        |_|_|_|
        |_|_|_|
        |X|_|_|
        |O|_|_|
        |_|_|_|
        |X|_|_|
        |O|X|_|
        |_|_|_|
        |X|_|_|
        |O|X|_|
        |O|_|_|
        |X|_|_|
        |O|X|_|
        |O|_|X|
        >>> g = TicTacToe()
        >>> g.mark(0, 0)
        >>> try:
        ...   g.mark(0, 0)
        ... except ValueError:
        ...   print('error raised as expected')
        ...
        error raised as expected
        >>> g.mark(0, 1)
        >>> print(g)
        |X|O|_|
        |_|_|_|
        |_|_|_|
        """
        if bool(self) is False:
            raise ValueError("Game Over")
        if row > 2:
            raise ValueError("Row Greater than 2")
        if col > 2:
            raise ValueError("Colume Greater than 2")
        if col < 0:
            raise ValueError("Colume Less than 0")
        if row < 0:
            raise ValueError("Row Less than 0")
        if self.play[row * 3 + col] != "_":
            raise ValueError("Tile Taken")
        else:
            self.play[(row * 3) + col] = self.players[self.index]
        # self.index = ~self.index

        if self.index == 0:
            self.index += 1
        elif self.index == 1:
            self.index -= 1

        pass

    def winner(self):
        """
        Returns the winner of the game,
        or None if the game has not ended or has ended without a winner.

        >>> g = TicTacToe(x='Xitlali', o='Osiris')
        >>> for move in ((0, 0), (1, 0), (1, 1), (2, 0), (2, 2)):
        ...   g.mark(*move)
        ...   print(g.winner())
        ...
        None
        None
        None
        None
        Xitlali
        """
        index_2 = 0
        for player in self.players:

            # Col Checker
            if player == self.play[0] and player == self.play[3] and player == self.play[6]:
                self.win_player = self.playernames[index_2]
            elif player == self.play[1] and player == self.play[4] and player == self.play[7]:
                self.win_player = self.playernames[index_2]
            elif player == self.play[2] and player == self.play[5] and player == self.play[8]:
                self.win_player = self.playernames[index_2]

            # Row Checker
            elif player == self.play[0] and player == self.play[1] and player == self.play[2]:
                self.win_player = self.playernames[index_2]
            elif player == self.play[3] and player == self.play[4] and player == self.play[5]:
                self.win_player = self.playernames[index_2]
            elif player == self.play[6] and player == self.play[7] and player == self.play[8]:
                self.win_player = self.playernames[index_2]

            # Diagonal Checker
            elif player == self.play[0] and player == self.play[4] and player == self.play[8]:
                self.win_player = self.playernames[index_2]
            elif player == self.play[2] and player == self.play[4] and player == self.play[6]:
                self.win_player = self.playernames[index_2]

            index_2 += 1
        return self.win_player

    # feel free to define other methods and/or a main block, if you'd like
    def reset(self):
        self.players = ["X", "O"]
        self.play = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.index = 0
        self.index_2 = 0
        self.win_player = None
