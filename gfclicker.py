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
bg = pygame.image.load('images/screen.png')
amazingImage = pygame.image.load('images/amazing.png')

class apps(object):
    def __init__(self):
        self.got = True

    def drawAmazing(self,win):
        if self.got:
            win.blit(amazingImage,(55,157))


def drawStuff():
    win.blit(bg, (0,0))
    amazing.drawAmazing(win)
    pygame.display.update()


amazing = apps()

while running:

    clock.tick(30)

    #closes game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawStuff()

pygame.quit
