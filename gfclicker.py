import pygame
import numpy as np
import pygame.freetype
from name_generator import gen_name
from classes import button
pygame.init()
print("Game loading lol if u see this ur gay lol omg lolololol terminal user lol")

# Important variables
screenWidth = 600
screenHeight = 950
appWidth = 124
appHeight = 124
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
amazingBackground = pygame.image.load('images/amazing/background.png')
messagesBackground = pygame.image.load('images/messages/background.png')
messagesButtonHit = pygame.image.load('images/messages/messagesButton.png')

# Creates the int for the score and the scorecard to blit
affection = 0

# Draws the screen and objects
def drawBorder():
    win.blit(border, (0,0))
    win.blit(notificationBar, (0,0))
    drawScoreCard(win,str(affection),24,116,116)
    pygame.display.update()

def drawScoreCard(win, text, size, x, y):
    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    win.blit(text_surface, text_rect)
    pygame.display.update()

def drawHomeScreen():
    win.blit(wallpaper, (0,0))
    amazing.drawButton(win)
    messages.drawButton(win)
    lickr.drawButton(win)
    messagesButton.drawButton(win)
    drawBorder()

def drawAmazing():
    win.blit(amazingBackground, (0,143))
    drawBorder()

def drawMessages():
    win.blit(messagesBackground, (0,143))

def clearScreen():
    win.blit(wallpaper, (0,0))
    drawBorder()

amazing = button(238,157,appWidth,appHeight,amazingImage)
messages = button(55,157,appWidth,appHeight,messagesImage)
lickr = button(417,157,appWidth,appHeight,lickrImage)
messagesButton = button(100,211,400,400,messagesButtonHit)
wallpaper = homeScreen
drawHomeScreen()
currentScreen = "home"

while running:

    clock.tick(60)


    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Closes game
        if event.type == pygame.QUIT:
            running = False

        #Checks for click amazing
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if amazing.isOver(pos):
                drawAmazing()
                currentScreen = "amazing"

        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if messages.isOver(pos):
                drawMessages()
                currentScreen = "messages"

        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "messages")):
            if messagesButton.isOver(pos):
                affection += 1
                drawBorder()


pygame.quit()
quit()
