import pygame

def splashScreen(screen):
    background = pygame.image.load("./assets/sprites/background-day.png")
    start_screen = pygame.transform.scale(pygame.image.load("./assets/sprites/start.png"), (288, 512))

    # Game loop for the start screen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  # Proceed to the game on any key press
                running = False

        screen.blit(background, (0, 0))
        screen.blit(start_screen, (0,0))

        # Update the display
        pygame.display.flip()

def countdown(screen, width, height):
    three_image = pygame.image.load("assets/sprites/3.png")
    two_image = pygame.image.load("assets/sprites/2.png")
    one_image = pygame.image.load("assets/sprites/1.png")

    three_image = pygame.transform.scale(three_image, (50, 50))
    two_image = pygame.transform.scale(two_image, (50, 50))
    one_image = pygame.transform.scale(one_image, (50, 50))

    countdown_images = [three_image, two_image, one_image]

    for image in countdown_images:
        screen.blit(image, (width // 2 - image.get_width() // 2, height // 2 - image.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(1000)  # Wait for 1 second
