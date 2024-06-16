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

        position = list(self.board.snake.head)
        choices = [
            (position[0][0] + 1, position[0][1]),
            (position[0][0] - 1, position[0][1]),
            (position[0][0], position[0][1] + 1),
            (position[0][0], position[0][1] - 1)
        ]
        return choices

    def head_choices(self):
        """Returns a list of possible choices for the snake to move"""

        choices = []
        free_fields = list(self.board.free_coord)
        apple_position = list(self.board.apple.position)
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
            return choices

        min_distance = 1000000
        min_choice = None
        apple_position = list(self.board.apple.position)
        for field in choices:
            distance = math.sqrt(pow((apple_position[0][0] - field[0]), 2) + pow((apple_position[0][1] - field[1]), 2))
            if distance < min_distance:
                min_distance = distance
                min_choice = field
        return [min_choice]

    def next_tail(self):
        """Returns the next tail of the sanke to set up"""

        position = list(self.board.snake.tail)
        free_fields = list(self.board.free_coord)
        limits_fields = list(self.board.limits_coord)
        choices = [
            (position[0][0] + 1, position[0][1]),
            (position[0][0] - 1, position[0][1]),
            (position[0][0], position[0][1] + 1),
            (position[0][0], position[0][1] - 1)
        ]
        next_tail = []
        for field in choices:
            if  field not in free_fields and field not in limits_fields:
                next_tail.append(field)
        return next_tail

    def move(self, coordinates):
        """Move the snake"""

        snake_coordinates = list(self.board.snake.position)
        if coordinates[0] in list(self.board.apple.position):
            snake_coordinates.append(list(self.board.apple.position)[0])
            self.board.apple.position = {random.choice(list(self.board.free_coord))}
        else:
            snake_coordinates.remove(list(self.board.snake.tail)[0])
            snake_coordinates.append(coordinates[0])
            if len(snake_coordinates) > 1:
                self.board.snake.tail = set(self.next_tail())
            else:
                self.board.snake.tail = set(coordinates)
        self.board.snake.position = set(snake_coordinates)
        self.board.snake.head = set(coordinates)

    def render(self):
        """Render the game cycle"""

        coordinates = self.head_choices()
        self.move(coordinates)
        self.board.show()
