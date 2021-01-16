import pygame

girlWidth = 500
girlHeight = 500

# Creates, draws, and determines if the cursor is over app
class button:
    def __init__(self,x,y,width,height):
        self.got = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = 0

    def drawButton(self,win):
        if self.got:
            win.blit(self.image,(self.x,self.y))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class girl:
    def __init__(self,name,image,multiplier):
        self.got = False
        self.name = name
        self.image = image
        self.multiplier = multiplier
        self.description = ""

    def drawGirl(self,win):
        if not self.got:
            win.blit(self.image,(50,225))

    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
