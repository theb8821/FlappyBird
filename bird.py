import pygame


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0  # bird at rest at the start
        self.gravity = 0.4
        self.lift = -6.5
        self.imageDownflap = pygame.image.load("assets/sprites/bluebird-downflap.png")
        self.imageUpflap = pygame.image.load("assets/sprites/bluebird-upflap.png")
        self.imageMidflap = pygame.image.load("assets/sprites/bluebird-midflap.png")
        self.rect = pygame.Rect(self.x, self.y, 34, 24)

    def flap(self):
        self.velocity = self.lift

    def fall(self):
        self.velocity += self.gravity
        self.y += self.velocity

        self.rect.topleft = (self.x, self.y)

    def draw(self, window):
        if self.velocity <= 0:
            self.image = self.imageDownflap
        elif self.velocity > 0:
            self.image = self.imageUpflap

        window.blit(self.image, (self.x, self.y))
