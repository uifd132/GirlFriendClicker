import pygame
import numpy as np
import time
from name_generator import nameGen
from classes import button
from classes import girl

pygame.init()
print("Game loading lol if u see this ur a gay terminal user lol")

# Important variables
screenWidth = 600
screenHeight = 950
appWidth = 124
appHeight = 124
running = True
clock = pygame.time.Clock()
t = time.localtime()
currentTime = time.strftime("%I:%M", t)
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Girlfriend Clicker: The Game")

#(this bit is for the font/scorecard)
black = (0,0,0)

# Creates the int for the score and the gf multiplier
affectionMultiplier = 1
affection = 0

# Images load here
border = pygame.image.load('images/apps/screen.png')
notificationBar = pygame.image.load('images/apps/notificationBar.png')
homeScreen = pygame.image.load('images/apps/bg.png')
amazingImage = pygame.image.load('images/apps/amazing.png')
messagesImage = pygame.image.load('images/apps/messages.png')
lickrImage = pygame.image.load('images/apps/lickr.png')
amazingBackground = pygame.image.load('images/amazing/background.png')
messagesBackground = pygame.image.load('images/messages/background.png')
lickrBackground = pygame.image.load('images/lickr/background.png')
jenniferAndBeckyImage = pygame.image.load('images/girls/JenniferAndBecky.png')


# Draws the screen and objects
def drawBorder():
    win.blit(border, (0,0))
    win.blit(notificationBar, (0,0))
    drawText(win,str(affection),23,111,116,"left")
    drawText(win,currentTime,23,41,116,"center")
    pygame.display.update()

def drawText(win, text, size, x, y, align):
    font = pygame.font.Font('fonts/OpenSans-Regular.ttf', size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    if align == "left":
        text_rect.midleft = (x,y)
    elif align == "center":
        text_rect.center = (x,y)
    win.blit(text_surface, text_rect)
    pygame.display.update()

def drawHomeScreen():
    win.blit(wallpaper, (0,0))
    amazing.drawButton(win)
    messages.drawButton(win)
    lickr.drawButton(win)
    drawBorder()

def drawAmazing():
    win.blit(amazingBackground, (0,143))
    drawBorder()

def drawMessages():
    win.blit(messagesBackground, (0,143))
    drawBorder()

def drawLickr():
    win.blit(lickrBackground, (0,143))
    jenniferAndBecky.drawGirl(win)
    drawText(win,jenniferAndBecky.name,30,300,800,"center")
    drawBorder()

def clearScreen():
    win.blit(wallpaper, (0,0))
    drawBorder()

amazing = button(238,157,appWidth,appHeight)
amazing.image = amazingImage
messages = button(55,157,appWidth,appHeight)
messages.image = messagesImage
lickr = button(417,157,appWidth,appHeight)
lickr.image = lickrImage
messagesButton = button(100,211,400,400)
homeButton = button(233,837,127,107)
jenniferAndBecky = girl(nameGen(),jenniferAndBeckyImage,2)
wallpaper = homeScreen
clickCount = 0

drawHomeScreen()
currentScreen = "home"

while running:

    clock.tick(60)


    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Closes game
        if event.type == pygame.QUIT:
            running = False

        # Checks for clicks on apps and opens them
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen != "home")):
            if homeButton.isOver(pos):
                clearScreen()
                drawHomeScreen()
                clickCount = 0
                currentScreen = "home"

        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if amazing.isOver(pos):
                drawAmazing()
                currentScreen = "amazing"

        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if messages.isOver(pos):
                drawMessages()
                currentScreen = "messages"

        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if lickr.isOver(pos):
                drawLickr()
                currentScreen = "lickr"

        # Main clicking function of button in messages
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "messages")):
            clickCount +=1
            if messagesButton.isOver(pos) & (clickCount >= 2):
                affection += affectionMultiplier
                drawBorder()

        # Buys new girlfriend in Lickr
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "lickr")):
            clickCount +=1
            if jenniferAndBecky.isOver(pos) & (clickCount >= 2) & (affection >= 10) and not (jenniferAndBecky.got):
                jenniferAndBecky.got = True
                affection -= 10
                drawLickr()
                drawBorder()


pygame.quit()
quit()
