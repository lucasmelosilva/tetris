import numpy as np 

class Board:
  def __init__(self, screen,  height = 20, width = 10):
    self._height = height
    self._width = width
    self._screen = screen
    self._matrix = np.zero([width, height], dtype=int)
    self._curr_tile = None
    self._score = 0