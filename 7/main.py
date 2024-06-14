"""Snake Game"""

from time import sleep
from game import Game

game = Game(15, 15)

while True:
    try:
        game.render()
        sleep(1)
    except RuntimeError as e:
        print(e)
        break

# game.render()
# sleep(2)
# game.render()
# sleep(2)
# game.render()
# sleep(2)
# game.render()
# sleep(2)
print('GAME OVER!')
