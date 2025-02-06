import pygame
from pygame.locals import *

pygame.init()

#window setup
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout!")
BACKGROUND = (10, 0, 15)

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.width, self.height = 89, 25
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

class Wall():
    def __init__(self):
        super().__init__()
        self.colors = ["red", "orange", "yellow", "green", "blue", "indigo", "cyan"]
        self.y = 100
        self.brick_list = []

    def build(self):
        for i in range(7):
            self.x = 4
            for brick in range(14):
                brick = Brick(self.x, self.y, self.colors[i])
                self.brick_list.append(brick)
                self.x += brick.width + 2
            self.y += brick.height + 2

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #appearance and position
        self.width, self.height = 100, 15
        self.x = WIDTH/2 - self.width/2
        self.y = 600
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vel = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.vel
        self.rect.x = self.x


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width, self.height = 20, 20
        self.x = WIDTH/2 - 50
        self.y = 300
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (10, 10), 10)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vel = 4

    def start(self):
        pass

    def move(self):
        pass

def main():
    FPS = 60
    clock = pygame.time.Clock()

    #create game objects
    paddle = Paddle()
    ball = Ball()
    wall = Wall()
    wall.build()

    #create sprite groups
    paddle_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    sprites_group = pygame.sprite.Group()

    #add sprites to groups
    paddle_group.add(paddle)
    ball_group.add(ball)
    brick_group.add(wall.brick_list)
    sprites_group.add(paddle, ball, wall.brick_list)


    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        #check for paddle movement
        keys = pygame.key.get_pressed()
        paddle.move(keys)

        sprites_group.update()
        
        WINDOW.fill(BACKGROUND)
        sprites_group.draw(WINDOW)
        pygame.display.flip()


main()
