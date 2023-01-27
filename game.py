import math
import pygame
from const import *
import numpy as np
from snakeai import AI


class Game:
    def __init__(self):
        self.game_over = False  # game over state
        self.length = 3
        self.pos = [[WIDTH // 100 * SNAKE_BLOCK for i in range(2)] for j in range(self.length)]
        self.speed = SNAKE_BLOCK
        self.snake_dir = 'r'
        self.has_food = False
        self.food_pos = []
        self.ate_food = False
        self.score = 0

    def draw_bg(self, screen):
        rect = (0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(screen, 'black', rect)
        for i in range(WIDTH // SNAKE_BLOCK):
            for j in range(HEIGHT // SNAKE_BLOCK):
                rect = (i*SNAKE_BLOCK, j*SNAKE_BLOCK, WIDTH, HEIGHT)
                pygame.draw.rect(screen, '#202124', rect, width = 1)

    def draw_snake(self, screen):
        for i in range(self.length):
            rect = (self.pos[i][0]+0.5, self.pos[i][1]+0.5, SNAKE_BLOCK - 1, SNAKE_BLOCK - 1)
            pygame.draw.rect(screen, '#9CFF2E', rect)



    # draw food
    def add_food(self, screen):
        if not self.has_food:

            x, y = self.random_num_generator()
            pygame.draw.circle(screen, '#E0144C', (x, y), SNAKE_BLOCK // 2 - 3)
            self.food_pos = [x, y]
            self.has_food = True
        else:
            pygame.draw.circle(screen, '#E0144C', self.food_pos, SNAKE_BLOCK // 2 - 3)

    # for another class---------------------------
    # moves
    def move_right(self):
        if self.snake_dir != 'l':
            self.snake_dir = 'r'

    def move_left(self):
        if self.snake_dir != 'r':
            self.snake_dir = 'l'

    def move_up(self):
        if self.snake_dir != 'd':
            self.snake_dir = 'u'

    def move_down(self):
        if self.snake_dir != 'u':
            self.snake_dir = 'd'

    def motion(self, screen):
        self.f_game_over()
        if not self.game_over:
            for i in range(self.length - 1, 0, -1):
                self.pos[i][0] = self.pos[i - 1][0]
                self.pos[i][1] = self.pos[i - 1][1]

            if self.snake_dir == 'r':
                self.pos[0][0] += self.speed
            elif self.snake_dir == 'l':
                self.pos[0][0] -= self.speed
            elif self.snake_dir == 'u':
                self.pos[0][1] -= self.speed
            elif self.snake_dir == 'd':
                self.pos[0][1] += self.speed

        self.draw_snake(screen)
        if self.game_over:
            rect = (WIDTH // 2, HEIGHT // 2, 100, 50)
            font = pygame.font.SysFont('robotomono', 50)
            img = font.render(f'GAME OVER', True, 'white')
            screen.blit(img, (WIDTH // 2 - 100, HEIGHT // 2 - 35))
            img = font.render(f'score = {self.score}', True, 'white')
            screen.blit(img, (WIDTH // 2 - 80, HEIGHT // 2))

    def eat(self):
        if [self.food_pos[0] - SNAKE_BLOCK // 2, self.food_pos[1] - SNAKE_BLOCK // 2] == self.pos[0]:
            self.length += 1
            self.pos.append(self.food_pos)
            self.has_food = False
            self.ate_food = True


    def f_game_over(self):
        if self.pos[0][0] >= WIDTH or self.pos[0][1] >= HEIGHT or self.pos[0][0] < 0 or self.pos[0][1] < 0:
            self.game_over = True
        elif self.pos[0] in self.pos[1:] and self.length > 3:
            self.game_over = True

    # random number generator
    def random_num_generator(self):
        x, y = self.pos[0]
        while [x, y] in self.pos:
            x = np.random.randint(0,
                                  WIDTH) // \
                SNAKE_BLOCK * SNAKE_BLOCK + SNAKE_BLOCK // 2 - SNAKE_BLOCK // 2
            y = np.random.randint(0,
                                  HEIGHT) // \
                SNAKE_BLOCK * SNAKE_BLOCK + SNAKE_BLOCK // 2 - SNAKE_BLOCK // 2
        return x + SNAKE_BLOCK // 2, y + SNAKE_BLOCK // 2

    def get_score(self, screen):
        if self.ate_food:
            self.score += 1
            self.ate_food = False

        font = pygame.font.SysFont('robotomono', 24, True)
        img = font.render(f'score = {self.score}', True, 'white')
        screen.blit(img, (WIDTH - 110, 10))
