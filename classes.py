import pygame

# App images loading
amazingImage = pygame.image.load('images/apps/amazing.png')
messagesImage = pygame.image.load('images/apps/messages.png')
lickrImage = pygame.image.load('images/apps/lickr.png')

appWidth = 124
appHeight = 124

# Creates, draws, and determines if the cursor is over app
class button:
    def __init__(self,x,y,width,height,image):
        self.got = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def drawButton(self,win):
        if self.got:
            win.blit(self.image,(self.x,self.y))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
