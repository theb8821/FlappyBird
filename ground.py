import pygame


class Ground:
    def __init__(self, gameWidth, gameHeight):
        self.x = 0
        self.y = gameHeight - 112
        self.gameWidth = gameWidth
        self.image = pygame.image.load("assets/sprites/base.png")
        self.rect = pygame.Rect(self.x, self.y, self.gameWidth, 112)

    def move(self):
        self.x -= 2.5

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

