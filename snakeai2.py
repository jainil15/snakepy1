import pygame

from const import WIDTH, HEIGHT
from game import Game


class Hamiltonian_Cycle:
    def __init__(self):
        self.cycle = [[None for i in range(2)] for j in range(4)]
        self.current_dir = 'r'

    def get_dir(self):
        self.cycle[0] = [self.current_dir]
        self.current_dir = self.cycle[1]
        self.cycle[1] = self.cycle[2]
        self.cycle[2] = self.cycle[3]
        self.cycle[3] = self.cycle[0]
        return self.current_dir



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game = Game()
hamiltonian_cycle = Hamiltonian_Cycle()
clock = pygame.time.Clock()
while not game.game_over:
    game.draw_bg(screen)
    game.motion(screen)
    game.eat()
    game.add_food(screen)
    game.get_score(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_UP:
                game.move_up()
            if event.key == pygame.K_DOWN:
                game.move_down()

    pygame.display.update()
    clock.tick(5)

pygame.quit()