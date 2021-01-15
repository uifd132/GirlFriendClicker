import pygame
import numpy as np
import pygame.freetype
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

#(this bit is for the font/scorecard)
black = (0,0,0)
font = pygame.freetype.Font('text/COMIC.TTF', 24)

# Images load here
border = pygame.image.load('images/apps/screen.png')
notificationBar = pygame.image.load('images/apps/notificationBar.png')
homeScreen = pygame.image.load('images/apps/bg.png')
amazingImage = pygame.image.load('images/apps/amazing.png')
messagesImage = pygame.image.load('images/apps/messages.png')
lickrImage = pygame.image.load('images/apps/lickr.png')

# Creates the int for the score and the scorecard to blit
affection = 0

# Draws the screen and objects
def drawBorder():
    win.blit(border, (0,0))
    win.blit(notificationBar, (0,0))
    drawScoreCard()
    pygame.display.update()

def drawScoreCard():
    textSurface, rect = font.render(str(affection), (0,0,0))
    win.blit(textSurface, (110,109))
    print("REFRESHING SCORECARD")
    pygame.display.update()
    
def drawHomeScreen():
    win.blit(wallpaper, (0,0))
    amazing.drawApps(win)
    messages.drawApps(win)
    lickr.drawApps(win)
    drawBorder()

def clearScreen():
    win.blit(wallpaper, (0,0))
    drawBorder()

amazing = apps(238,157,amazingImage)
messages = apps(55,157,messagesImage)
lickr = apps(417,157,lickrImage)
wallpaper = homeScreen
drawHomeScreen()

while running:

    clock.tick(1)
    
    #attempt to update scorecard
    affection += 1
    print(str(affection))
    drawScoreCard()
    
    
        
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Closes game
        if event.type == pygame.QUIT:
            running = False
        
        #Checks for clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if amazing.isOver(pos):
                clearScreen()
            


pygame.quit()
quit()
