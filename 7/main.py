"""Snake Game"""

from board import Board

board = Board(5, 5)

print(board.all_coordinates)
print(board.limits_coord)
print(board.non_limits_coord)
print(board.show())
