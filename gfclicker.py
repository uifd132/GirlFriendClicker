import pygame
pygame.init()
print("Game loading lol if u see this ur gay lol omg lolololol terminal user lol")

screenWidth = 600
screenHeight = 950
running = True

clock = pygame.time.Clock()
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Girlfriend Clicker: The Game")

#Images load here



while running:

    clock.tick(30)

    #closes game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
