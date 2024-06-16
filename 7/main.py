"""Snake Game"""

from time import sleep
from game import Game

game = Game(7, 7)
print(game.board)

while True:
    try:
        game.render()
        sleep(1)
    except RuntimeError as e:
        print(e)
        break

print('GAME OVER!')
