import pygame
import random

class Pipe:
    def __init__(self, x, gapHeight, gameWidth, gameHeight):
        self.x = x
        self.width = 32
        self.gapHeight = gapHeight
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.topHeight = random.randint(72, 310)
        self.bottomHeight = self.topHeight + self.gapHeight

        self.topImage = pygame.image.load("assets/sprites/pipe-top.png")
        self.bottomImage = pygame.image.load("assets/sprites/pipe-bottom.png")

    def move(self):
        self.x -= 2.5

    def draw(self, window):
        window.blit(self.topImage, (self.x, self.topHeight - 320))
        window.blit(self.bottomImage, (self.x, self.bottomHeight))
