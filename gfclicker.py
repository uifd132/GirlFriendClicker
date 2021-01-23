import pygame
import numpy as np
import time
from name_generator import nameGen
from classes import button
from classes import girl
from girl_generator import girlGen

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
gifts = pygame.image.load('images/amazing/multi_button.png')
gifts_sel = pygame.image.load('images/amazing/multi_button_sel.png')
toys = pygame.image.load('images/amazing/bot_button.png')
toys_sel = pygame.image.load('images/amazing/bot_button_sel.png')


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

def drawAmazing(toys_on):
    if not toys_on:
        win.blit(amazingBackground, (0,143))
        win.blit(gifts_sel, (153,174))
        win.blit(toys, (313,174))
    else:
        win.blit(amazingBackground, (0,143))
        win.blit(gifts, (153,174))
        win.blit(toys_sel, (313,174))
    drawBorder()

def drawMessages():
    win.blit(messagesBackground, (0,143))
    drawBorder()

def drawLickr():
    win.blit(lickrBackground, (0,143))
    if not jenniferAndBecky.got:
        jenniferAndBecky.drawGirl(win)
        drawText(win,jenniferAndBecky.name+": "+str(girl_cost),30,300,800,"center")
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
wallpaper = homeScreen
clickCount = 0
girl_cost = 100
girl_bought = 0
time_ch = 0
jenniferAndBecky = girlGen(girl_bought)
gifts_button = button(153,174,157,35)
toys_button = button(313,174,135,35)
amazing_tab = False
drawHomeScreen()
currentScreen = "home"

while running:

    dt = clock.tick(60)


    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Closes game
        if event.type == pygame.QUIT:
            running = False
            
        #Clock update every minute
        time_ch += dt
        
        if time_ch > 1000:
            t = time.localtime()
            currentTime = time.strftime("%I:%M", t)
            drawBorder()
            time_ch = 0

        # Checks for clicks on apps and opens them
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen != "home")):
            if homeButton.isOver(pos):
                clearScreen()
                drawHomeScreen()
                clickCount = 0
                currentScreen = "home"
                amazing_tab = False
                
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if amazing.isOver(pos):
                drawAmazing(amazing_tab)
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
                affection += int(np.floor(affectionMultiplier))
                drawBorder()

        # Buys new girlfriend in Lickr
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "lickr")):
            clickCount +=1
            if (jenniferAndBecky.isOver(pos)) & (clickCount >= 2) & (affection >= girl_cost) & (not (jenniferAndBecky.got)):
                jenniferAndBecky.got = True
                affection -= girl_cost
                girl_cost *= 2.5
                affectionMultiplier = affectionMultiplier*jenniferAndBecky.multiplier
                girl_bought += 1
                drawLickr()
                drawBorder()
                
        # Changes tabs to buy in Amazing app
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "amazing")):
            if amazing_tab & toys_button.isOver(pos):
                drawAmazing(amazing_tab)
                amazing_tab = False
            elif gifts_button.isOver(pos):
                drawAmazing(amazing_tab)
                amazing_tab = True

pygame.quit()
quit()
