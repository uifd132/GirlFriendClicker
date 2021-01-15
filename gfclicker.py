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
border = pygame.image.load('images/apps/screen.png')
homeScreen = pygame.image.load('images/apps/bg.png')


# Draws the screen and objects

def drawBorder():
    win.blit(border, (0,0))
    pygame.display.update()
    
def drawHomeScreen():
    win.blit(wallpaper, (0,0))
    amazing.drawAmazing(win)
    messages.drawMessages(win)
    lickr.drawLickr(win)
    drawBorder()
    
def clearScreen():
    win.blit(wallpaper, (0,0))
    drawBorder()

amazing = apps()
messages = apps()
lickr = apps()
wallpaper = homeScreen

drawHomeScreen()

while running:

    clock.tick(30)

    #closses game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
quit()
