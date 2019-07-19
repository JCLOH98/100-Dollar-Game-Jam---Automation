import sys
import pygame
from pygame.locals import *
import time

SCREENWIDTH = 1000
SCREENHEIGHT = 500

BUTTONWIDTH = 100
BUTTONHEIGHT = 45

FPS = 30

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)

pygame.init()
Display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Automation")

def startscreen():
    running = True
    while running:
        Display.fill(AQUA) #background

        mousepos = pygame.mouse.get_pos()

        StartButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        StartButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2)
        
        InsButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        InsButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + BUTTONHEIGHT)
        
        ExitButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        ExitButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + 2*BUTTONHEIGHT)

        pygame.draw.rect(Display,RED,StartButton)
        pygame.draw.rect(Display,GREEN,InsButton)
        pygame.draw.rect(Display,BLUE,ExitButton)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (StartButton.collidepoint(mousepos)):
                    print("Start")
                    running = False

                elif (InsButton.collidepoint(mousepos)):
                    print("Instructions")
                    insscreen()

                elif (ExitButton.collidepoint(mousepos)):
                    print("Exit")
                    pygame.quit()
                    sys.exit()
                    
                pass
                

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def insscreen():
    print ("InsScreen")
    pass

def endscreen():
    pass
    
def background():
    Display.fill(GREY)

class Player:
    def __init__(self,maxlife):
        self.main = maxlife
        self.tower1 = maxlife * 10 / 100
        self.tower2 = maxlife * 15 / 100
        self.tower3 = maxlife * 20 / 100
        pass

class Enemy:
    def __init__(self,maxlife,time):
        elf.main = maxlife
        self.tower1 = maxlife * 11 / 100
        self.tower2 = maxlife * 13 / 100
        self.tower3 = maxlife * 15 / 100
        pass

def main():
    TheTime = 0
    Start = time.time()#start time
    
    while True:
        background() #background
        End = time.time()#end time
        if (int(End) - int(Start) == 1):
                        TheTime += 1
                        Start = time.time()
                        #print(TheTime)
                        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

startscreen()
main()
