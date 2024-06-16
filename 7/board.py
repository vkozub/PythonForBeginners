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

        limits = []
        non_limits = []

        for column in range(self._height):
            for row in range(self._width):
                if column in (0, (self._width - 1)):
                    limits.append((column, row))
                elif row in (0, (self._height - 1)):
                    limits.append((column, row))
                else:
                    non_limits.append((column, row))
        self._limits = limits
        self._non_limits = non_limits
        self._apple = Apple([random.choice(non_limits)])
        self._snake = Snake([random.choice(self.free_coord)])
        return list(set(non_limits) | set(limits))

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
            free_coord = list(set(self._non_limits) - set(self.apple.position) - set(self.snake.position))
        else:
            free_coord = list(set(self._non_limits) - set(self.apple.position))
        return free_coord

    @property
    def apple(self):
        """Get apple coordinates"""
        return self._apple

    @property
    def snake(self):
        """Get snake coordinates"""
        return self._snake

    def show(self):
        """Show board"""
        sorted_coordinates = sorted(self._board)
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

    def __str__(self) -> str:
        return f'Non limits fields: {self._non_limits}\n' \
                f'Limits fields: {self._limits}\n' \
                f'Apple position: {self.apple.position}\n' \
                f'Snake position: {self.snake.position}'
