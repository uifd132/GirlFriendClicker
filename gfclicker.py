import pygame
import numpy as np
import time
from classes import button
from gameSave import gameState

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
display_amazing = pygame.image.load('images/amazing/display.png')
auto_like_im = pygame.image.load('images/amazing/auto_like.png')
buy = pygame.image.load('images/amazing/buy.png')

game = gameState()

# Draws the screen and objects
def drawBorder():
    win.blit(border, (0,0))
    win.blit(notificationBar, (0,0))
    drawText(win,str(game.affection),23,111,116,"left")
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
    win.blit(amazingBackground, (0,143))
    if (not toys_on):
        win.blit(gifts_sel, (153,174))
        win.blit(toys, (313,174))
    else:
        win.blit(gifts, (153,174))
        win.blit(toys_sel, (313,174))
        win.blit(auto_like_im, (77,260))
        drawText(win,"Like-Bot", 30, 220, 268, "center")
        win.blit(buy, (163,295))
        drawText(win, str(game.auto_like_price[0]), 20, 400, 268, "center")
        drawText(win, str(game.auto_like[0]), 20, 400, 300, "center")
    win.blit(display_amazing, (0,232))
    drawBorder()

def drawMessages():
    win.blit(messagesBackground, (0,143))
    drawBorder()

def drawLickr():
    win.blit(lickrBackground, (0,143))
    if not game.girl_to_buy[0].got:
        game.girl_to_buy[0].drawGirl(win)
        drawText(win,game.girl_to_buy[0].name+": "+str(game.girl_cost),30,300,800,"center")
    drawBorder()

def clearScreen():
    win.blit(wallpaper, (0,0))
    drawBorder()

#buttons
amazing = button(238,157,appWidth,appHeight)
amazing.image = amazingImage
messages = button(55,157,appWidth,appHeight)
messages.image = messagesImage
lickr = button(417,157,appWidth,appHeight)
lickr.image = lickrImage
messagesButton = button(100,211,400,400)
homeButton = button(233,837,127,107)
gifts_button = button(153,174,157,35)
toys_button = button(313,174,135,35)
buy_button = button(163,295,123,38)

#Initialize
wallpaper = homeScreen
currentScreen = "home"
clickCount = 0
time_ch = 0
money_ch = 0
    
drawHomeScreen()

while running:

    dt = clock.tick(60)


    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Closes game
        if event.type == pygame.QUIT:
            running = False
            
        #Clock update every minute
        time_ch += dt
        money_ch += dt
        
        # AutoMoney
        if money_ch >= 1000:
            game.affection += game.auto_like[0]
            money_ch = 0
            drawBorder()
        
        if time_ch > 5000:
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
                game.toy_tab = False
                
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "home")):
            if amazing.isOver(pos):
                drawAmazing(game.toy_tab)
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
                game.affection += int(np.floor(game.affectionMultiplier))
                drawBorder()

        # Buys new girlfriend in Lickr
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "lickr")):
            clickCount +=1
            if (game.girl_to_buy[0].isOver(pos)) & (clickCount >= 2) & (game.affection >= game.girl_cost) & (not (game.girl_to_buy[0].got)):
                game.girl_to_buy[0].got = True
                game.affection -= game.girl_cost
                game.girl_cost *= 2.5
                affectionMultiplier = game.affectionMultiplier*game.girl_to_buy[0].multiplier
                game.girl_bought += 1
                drawLickr()
                drawBorder()
                
        # Changes tabs to buy in Amazing app
        if ((event.type == pygame.MOUSEBUTTONDOWN) & (pygame.mouse.get_pressed()[0]) & (currentScreen == "amazing")):
            if (not game.toy_tab) & toys_button.isOver(pos):
                game.toy_tab = True
                drawAmazing(game.toy_tab)
            elif (game.toy_tab) & gifts_button.isOver(pos):
                game.toy_tab = False
                drawAmazing(game.toy_tab)
            if ((game.toy_tab) & (buy_button.isOver(pos)) & (game.affection >= game.auto_like_price[0])):
                game.auto_like[0] += 1
                game.affection -= game.auto_like_price[0]
                game.auto_like_price[0] = int(np.ceil(1.75*game.auto_like_price[0]))
                drawAmazing(game.toy_tab)
                
pygame.quit()
quit()
