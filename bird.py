import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0 # bird at rest at the start
        self.gravity = 0.25
        self.lift = -7.5
        self.imageDownflap = pygame.image.load("assets/sprites/bluebird-downflap.png")
        self.imageUpflap = pygame.image.load("assets/sprites/bluebird-upflap.png")
        self.imageMidflap = pygame.image.load("assets/sprites/bluebird-midflap.png")

    def flap(self):
        self.velocity = self.lift

    def fall(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, window):
        if self.velocity < 0:
                self.image = self.imageDownflap
        elif self.velocity > 0:
                self.image = self.imageUpflap
        
        window.blit(self.image, (self.x, self.y))

