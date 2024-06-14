"""Game module"""

import math
from board import Board

class Game:
    """Game base class"""

    def __init__(self, width, height):
        self.board = Board(width, height)
        # self.snake = Snake()

    def all_choices(self):
        """Returns a list of all choices for the snake"""

        position = list(self.board.snake.position)
        choices = [
            (position[0] + 1, position[1]),
            (position[0] - 1, position[1]),
            (position[0], position[1] + 1),
            (position[0], position[1] - 1)
        ]
        return choices

    def choices(self):
        """Returns a list of possible choices for the snake"""

        choices = []
        free_fields = list(self.board.free_coord)
        apple_position = list(self.board.apple.position)
        for field in self.all_choices():
            if field in apple_position:
                choices = apple_position
                break
            if field in free_fields:
                choices.append(field)
        if choices:
            return self.find_min(choices)
        raise RuntimeError('No choices for the snake')

    def find_min(self, choices):
        """Returns the choice with the shortest distance"""

        if len(choices) == 1:
            return choices

        min_distance = 1000000
        min_choice = None
        apple_position = list(self.board.apple.position)
        for field in choices:
            distance = math.sqrt(pow((apple_position[0][0] - field[0]), 2) + pow((apple_position[0][1] - field[1]), 2))
            if distance < min_distance:
                min_choice = field
        return [min_choice]
