import pygame
from bird import Bird
from pipe import Pipe

class Game:
    def __init__(self):
        self.width = 288
        self.height = 512
        self.score = 0
        self.gapHeight = int(self.height * 0.25)
        self.birdX = int(self.width * 0.1)
        self.birdY = self.height // 2 - 12


        self.bird = Bird(self.birdX, self.birdY)
        self.pipe = Pipe(self.width + 150, self.gapHeight, self.width, self.height)

        pygame.display.set_caption("Flappy Bird")
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font("assets/Roboto-Medium.ttf", 32)

        self.background = pygame.image.load("assets/sprites/background-day.png")

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                    self.bird.flap()

            self.bird.fall()
            self.pipe.move()
            self.draw()

            # set frame rate
            clock.tick(60)

    def draw(self):
        self.window.blit(self.background, (0,0))

        scoreText = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.window.blit(scoreText, (self.width - 100, 20))

        self.pipe.draw(self.window)
        self.bird.draw(self.window)
        pygame.display.update()

