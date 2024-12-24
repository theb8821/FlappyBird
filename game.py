import pygame, time, sys
from bird import Bird
from pipe import Pipe
from ground import Ground


class Game:
    def __init__(self):
        self.width = 288
        self.height = 512
        self.score = 0
        self.gapHeight = 100
        self.birdX = int(self.width * 0.1)
        self.birdY = self.height // 2 - 12

        self.bird = Bird(self.birdX, self.birdY)
        self.pipes = []
        self.ground = Ground(self.width, self.height)

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

            self.draw()

            self.bird.fall()
            self.createPipes()
            self.pipeController()

            if self.checkCollision():
                running = False

            # set frame rate
            clock.tick(60)

    def createPipes(self):
        for _ in range(3):
            self.pipes.append(
                Pipe(self.width + 150, self.gapHeight, self.width, self.height)
            )

    def pipeController(self):
        self.pipes[0].move()

        for i in range(3):
            if self.pipes[i].x <= -60:
                self.pipes.remove(self.pipes[i])

            if self.pipes[i].x <= self.width:
                self.pipes[i + 1].move()

    def checkCollision(self):
        for pipe in self.pipes:
            if pygame.Rect.colliderect(
                pipe.rectTop, self.bird.rect
            ) or pygame.Rect.colliderect(pipe.rectBottom, self.bird.rect):
                return True

        if self.bird.rect.bottom >= 400:
            return True

        return False

    def draw(self):
        self.window.blit(self.background, (0, 0))

        for pipe in self.pipes:
            pipe.draw(self.window)

        scoreText = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(scoreText, (0, 20))

        self.ground.draw(self.window)
        self.bird.draw(self.window)

        pygame.display.update()
