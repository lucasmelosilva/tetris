import numpy as np
from collision_detector import CollisionDetector
from shape import Shape
class Tile:
  def __init__(self, shape: Shape, collision_detector: CollisionDetector, color: int, pos_x=5, pos_y=0, rotation=0):
    self._shape = shape
    self._rotation = rotation
    self._color = color
    self._collision_detector = collision_detector
    self._position = np.array([pos_x, pos_y])
    self._is_locked = False
    
  def render(self, board):
    matrix = self.get_coordinates()
    board.draw_tile(matrix, self._color)
    
  def get_coordinates(self):
    return self._shape.get_matrix_with_offset(self._rotation, self._position)
  
  def get_color(self):
    return self._color
  
  def rotate(self, direction):
    new_rotation = np.abs(np.mod(self._rotation + direction, self._shape._rotations_count))
    new_matrix = self._shape.get_matrix_with_offset(new_rotation, self._position)
    self._rotation = new_rotation
    collision = self._collision_detector.check(new_matrix, 0, 0)
    if collision is collision.BOTTOM:
      self._is_locked = True
    if collision is collision.NONE:
      self._rotation = new_rotation
    return new_matrix
  
  def move(self, dx, dy):
    next_pos = self._position + np.array([dx, dy]) 
    new_matrix = self._shape.get_matrix_with_offset(self._rotation, next_pos)
    collision = self._collision_detector.check(new_matrix, dx, dy)
    if collision is collision.BOTTOM:
      self._is_locked = True
    if collision is collision.NONE:
      self._position = next_pos
    return self._is_locked