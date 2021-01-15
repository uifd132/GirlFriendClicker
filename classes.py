import pygame

# App images loading
amazingImage = pygame.image.load('images/apps/amazing.png')
messagesImage = pygame.image.load('images/apps/messages.png')
lickrImage = pygame.image.load('images/apps/lickr.png')

class apps:
    def __init__(self):
        self.got = True

    def drawAmazing(self,win):
        if self.got:
            win.blit(amazingImage,(238,157))
    def drawMessages(self,win):
        if self.got:
            win.blit(messagesImage,(55,157))
    def drawLickr(self,win):
        if self.got:
            win.blit(lickrImage,(417,157))
