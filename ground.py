import pygame

class Ground:
    def __init__(self, gameHeight):
        self.x = 0
        self.y = gameHeight - 112

        self.image = pygame.image.load("assets/sprites/base.png")

    def move(self):
        self.x -= 2.5

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

