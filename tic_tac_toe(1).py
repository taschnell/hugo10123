"""
Module tic_tac_toe contains the TicTacToe class, instances of which model Tic-Tac-Toe games.
"""
__author__ = 'A student in CS 12P, someone@jeff.cis.cabrillo.edu'


from re import M


class TicTacToe:
  """
  Models a game of Tic-Tac-Toe. Player can be given names, but are still represented as 'X' and 'O'
  on the grid. X has the first turn. Grid squares are claimed by calling the mark() method. Row and
  column values are specified by indexes 0–2.
  """
  grid = tuple(None, None, None, None, None, None, None, None, None)
  active_player = ''

  def __init__(self, x='X', o='O'):
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
    players = [x,o]
    active_player = players[0]
    pass

  def __bool__(self):
    """
    A Tic-Tac-Toe game is considered Boolean True if it is still in play, i.e. there is no winner
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

    if TicTacToe.winner() != None:
      return False
    elif None not in TicTacToe.grid():
      return False
    else:
      return True
      

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
    pass  # TODO

  def grid(self):
    """
    Returns a tuple representing the state of the grid, consisting of 9 values that are either the
    string 'X', the string 'O', or None. grid()[:3] represents the first row, grid()[3:6] represents
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
        

    return self.grid


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
    if row > 2 or col > 2:
      KeyError
    

    
    if self.grid[(row *3) + col] != None:
      KeyError
    else:
      self.grid[(row *3) + col] = self.active_player
    pass

  def winner(self):
    """
    Returns the winner of the game, or None if the game has not ended or has ended without a winner.

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
    pass  # TODO


# feel free to define other methods and/or a main block, if you'd like

print('|_|_|_|\n|_|_|_|\n|_|_|_|')
