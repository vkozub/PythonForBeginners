"""Game module"""

import math
import random
from board import Board

class Game:
    """Game base class"""

    def __init__(self, width, height):
        self.board = Board(width, height)
        self.init_game()

    def init_game(self):
        """Initialize game state"""

        self.board.show()

    def all_head_choices(self):
        """Returns a list of all choices for the snake head to move"""

        position = self.board.snake.position[0]
        choices = [
            (position[0] + 1, position[1]),
            (position[0] - 1, position[1]),
            (position[0], position[1] + 1),
            (position[0], position[1] - 1)
        ]
        return choices

    def coordinates_to_move(self):
        """Returns coordinates (tuple) for the snake to move"""

        choices = []
        free_fields = self.board.free_coord
        apple_position = self.board.apple.position
        for field in self.all_head_choices():
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
            return choices[0]

        min_distance = 1000000
        min_choice = None
        apple_position = self.board.apple.position[0]
        for field in choices:
            distance = math.sqrt(pow((apple_position[0] - field[0]), 2) + pow((apple_position[1] - field[1]), 2))
            if distance < min_distance:
                min_distance = distance
                min_choice = field
        return min_choice

    def move(self, coordinates):
        """Move the snake to the coordinates"""

        snake_coordinates = self.board.snake.position
        if coordinates in self.board.apple.position:
            snake_coordinates.insert(0, self.board.apple.position[0])
            self.board.apple.position = [random.choice(self.board.free_coord)]
        else:
            snake_coordinates.pop()
            snake_coordinates.insert(0, coordinates)
        self.board.snake.position = snake_coordinates

    def render(self):
        """Render the game cycle"""

        coordinates = self.coordinates_to_move()
        self.move(coordinates)
        self.board.show()
