import pygame
import random


class Pipe:
    def __init__(self, x, gapHeight, gameWidth, gameHeight):
        self.x = x
        self.width = 32
        self.gapHeight = gapHeight
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight

        self.topHeight = random.randint(
            50, 290
        )  # Calculated on the basis of game height, gap height, ground height
        self.bottomHeight = self.topHeight + self.gapHeight

        self.topImage = pygame.image.load("assets/sprites/pipe-top.png")
        self.bottomImage = pygame.image.load("assets/sprites/pipe-bottom.png")

        self.rectTop = pygame.Rect(self.x, 0, 52, self.topHeight)
        self.rectBottom = pygame.Rect(self.x, self.bottomHeight, 52, self.bottomHeight)

    def move(self):
        self.x -= 2.5

        self.rectTop.topleft = (self.x, 0)
        self.rectBottom.topleft = (self.x, self.bottomHeight)

    def draw(self, window):

        window.blit(self.topImage, (self.x, self.topHeight - 320))
        window.blit(self.bottomImage, (self.x, self.bottomHeight))
