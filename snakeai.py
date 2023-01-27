
from const import *


class AI:

    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False

    @staticmethod
    def find_shortest_path(head_pos, food_pos):

        x = head_pos[0] - food_pos[0]
        y = head_pos[1] - food_pos[1]
        return x // SNAKE_BLOCK, y // SNAKE_BLOCK

    @staticmethod
    def ai_move(game):
        x, y = AI.find_shortest_path(game.pos[0], game.food_pos)
        print(game.pos[0], game.food_pos)

        if game.pos[0][0] + SNAKE_BLOCK >= WIDTH:
            game.move_up()

        elif game.pos[0][1] + SNAKE_BLOCK >= HEIGHT:
            game.move_left()

        elif game.pos[0][0] < SNAKE_BLOCK:
            game.move_down()

        elif game.pos[0][1] < SNAKE_BLOCK:
            game.move_left()

        if [game.pos[0][0], game.pos[0][1]] in game.pos[1:]:
            if game.snake_dir == 'u':
                game.move_right()

            elif game.snake_dir == 'l':
                game.move_down()

            elif game.snake_dir == 'd':
                game.move_right()

            elif game.snake_dir == 'r':
                game.move_down()

        if game.snake_dir == 'u':
            if x < -1:
                game.move_right()
                # print('move_right')
            elif x > -1:
                game.move_left()
                # print('move_left')

        elif game.snake_dir == 'l':
            if y > -1:
                game.move_up()
                # print('move_up')
            elif y < -1:
                game.move_down()
                # print('move_down')

        elif game.snake_dir == 'd':
            if x < -1:
                game.move_right()
                # print('move_right')
            elif x > -1:
                game.move_left()
                # print('move_left')

        elif game.snake_dir == 'r':
            if y > -1:
                game.move_up()
                # print('move_up')
            elif y < -1:
                game.move_down()
                # print('move_down')
