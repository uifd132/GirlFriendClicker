import pygame
import numpy as np
from name_generator import gen_name
from classes import apps
pygame.init()
print("Game loading lol if u see this ur gay lol omg lolololol terminal user lol")

# Important variables
screenWidth = 600
screenHeight = 950
running = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Girlfriend Clicker: The Game")

# Images load here
bg = pygame.image.load('images/apps/screen.png')


# Draws the screen and objects
def drawStuff():
    win.blit(bg, (0,0))
    amazing.drawAmazing(win)
    messages.drawMessages(win)
    lickr.drawLickr(win)
    pygame.display.update()


amazing = apps()
messages = apps()
lickr = apps()

while running:

    clock.tick(30)

    #closes game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawStuff()

pygame.quit
