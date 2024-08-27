import numpy as np

class Ground:
  def __init__(self, width, height):
    self._width = width
    self._height = height
    self._matrix = np.zeros([width, height], dtype=int)
    self._coordinates = list()
  
  def merge(self, tile):
    coordinates = tile.get_coordinates()
    for position in coordinates:
      if ((self._matrix[position[0], position[1]] != 0) or 
          (position[0] >= self._width) or (position[1] >= self._height)):
        print('Error')
      self._matrix[position[0], position[1]] = tile.get_color()
      self._coordinates.append(position)
  
  def get_matrix(self):
    return self._matrix
  
  def get_coordinates(self):
    return self._coordinates