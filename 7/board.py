"""Board class"""

import random
from apple import Apple
from snake import Snake

class Board:
    """Base class for board"""
    def __init__(self, width:int, height:int, border='*'):
        self._width = width
        self._height = height
        self._boarder = border
        self._board = self.init_board()

    def init_board(self):
        """Initialize board state"""

        limits = set()
        non_limits = set()

        for column in range(self._height):
            for row in range(self._width):
                if column in (0, (self._width - 1)):
                    limits.add((column, row))
                elif row in (0, (self._height - 1)):
                    limits.add((column, row))
                else:
                    non_limits.add((column, row))
        self._limits = limits
        self._non_limits = non_limits
        self._apple = Apple({random.choice(list(self._non_limits))})
        self._snake = Snake({random.choice(list(self.free_coord))})
        return non_limits.union(limits)

    @property
    def all_coordinates(self):
        """Get board coordinates"""
        return self._board

    @property
    def limits_coord(self):
        """Get limits coordinates"""
        return self._limits

    @property
    def non_limits_coord(self):
        """Get non limits coordinates"""
        return self._non_limits

    @property
    def free_coord(self):
        """Get not ocupied (free) coordinates"""
        free_coord = set()
        if hasattr(self, '_snake'):
            free_coord = self._non_limits.difference(self.apple.position, self.snake.position)
        else:
            free_coord = self._non_limits.difference(self.apple.position)
        return free_coord

    @property
    def apple(self):
        """Get apple coordinates"""
        return self._apple

    @property
    def snake(self):
        """Get apple coordinates"""
        return self._snake

    def show(self):
        """Show board"""
        sorted_coordinates = sorted(self._board)
        # print(sorted_coordinates)
        for field in sorted_coordinates:
            if self._width - 1 == field[1]:
                print(self._boarder)
            elif 0 in field:
                print(self._boarder, end = '')
            elif self._height - 1 == field[0]:
                print(self._boarder, end = '')
            elif field in self.apple.position:
                print(self._apple.body, end = '')
            elif field in self.snake.position:
                print(self._snake.body, end = '')
            else:
                print(' ', end = '')
