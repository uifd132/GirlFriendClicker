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
bg = pygame.image.load('images/apps/screen.png')
amazingImage = pygame.image.load('images/apps/amazing.png')
messagesImage = pygame.image.load('images/apps/messages.png')
lickrImage = pygame.image.load('images/apps/lickr.png')

class apps(object):
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
