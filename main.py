import sys

import pygame
from const import *
from game import Game
from snakeai import AI


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.ai = AI()
        
        
    def main_loop(self):
        screen = self.screen
        game = self.game
        clock = self.clock
        ai = self.ai
        while True:
            game.f_game_over()
            game.draw_bg(screen)
            game.add_food(screen)
            game.motion(screen)
            game.eat()
            game.get_score(screen)

            clock.tick(17)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                if event.type == pygame.KEYDOWN:
                    if not game.game_over:
                        if event.key == pygame.K_d:
                            game.move_right()
                        elif event.key == pygame.K_a:
                            game.move_left()
                        elif event.key == pygame.K_w:
                            game.move_up()
                        elif event.key == pygame.K_s:
                            game.move_down()


                    if event.key == pygame.K_r:
                        game.__init__()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            AI.ai_move(game)

if __name__ == "__main__":
    main = Main()
    main.main_loop()
