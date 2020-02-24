import math
import time
import random
import sys
import pygame
from pygame.locals import *

pygame.display.set_icon(pygame.image.load("./sprites/3310icon.png"))
pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 500

Display = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("War.tomation")

pygame.mouse.set_cursor(*pygame.cursors.tri_left)

BigFont = pygame.font.Font("./font/carbon bl.ttf",40)
SmallFont = pygame.font.Font("./font/carbon bl.ttf",25)
SmallerFont = pygame.font.Font("./font/carbon bl.ttf",15)

BUTTONWIDTH = 250
BUTTONHEIGHT = 45

MINIONBOXWIDTH = 50
MINIONBOXHEIGHT = 50

#main
MAINBOXWIDTH = int(math.floor(48*2.5))
MAINBOXHEIGHT = int(math.floor(32*2.5))
MAIN1 = pygame.transform.scale(pygame.image.load("./sprites/maintower/MainTower.png").convert_alpha(),(MAINBOXWIDTH,MAINBOXHEIGHT))
eMAIN1 = pygame.transform.scale(pygame.image.load("./sprites/maintower/MainTower_2.png").convert_alpha(),(MAINBOXWIDTH,MAINBOXHEIGHT))

#tower
TOWERBOXWIDTH = int(math.floor(32*2))
TOWERBOXHEIGHT = int(math.floor(48*2))
TOWERINTERVAL = 20
TOWER1 = pygame.transform.scale(pygame.image.load("./sprites/powertower/powertower-cut/tile000.png").convert_alpha(),(TOWERBOXWIDTH,TOWERBOXHEIGHT))
TOWER2 = pygame.transform.scale(pygame.image.load("./sprites/powertower/powertower-cut/tile001.png").convert_alpha(),(TOWERBOXWIDTH,TOWERBOXHEIGHT))
eTOWER1 = pygame.transform.scale(pygame.image.load("./sprites/powertower/powertower-cut-2/tile000.png").convert_alpha(),(TOWERBOXWIDTH,TOWERBOXHEIGHT))
eTOWER2 = pygame.transform.scale(pygame.image.load("./sprites/powertower/powertower-cut-2/tile001.png").convert_alpha(),(TOWERBOXWIDTH,TOWERBOXHEIGHT))

FPS = 30

LEFT_CLICK = (1,0,0)
RIGHT_CLICK = (0,0,1)

MAXLIFE = 100

GOLDAMOUNT = 25 #1 second, 10 golds

BLACK = (0,0,0)
GREY = (150,150,150)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTRED = (255,0,180)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHTBLUE = (0,180,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)

COLORA = RED
COLORB = LIGHTRED
COLORC = YELLOW
COLORD = LIGHTBLUE
COLORE = BLUE

AGOLD = 50
BGOLD = 100
CGOLD = 150
DGOLD = 200
EGOLD = 250

ASPEED = 4
BSPEED = 4
CSPEED = 3
DSPEED = 2
ESPEED = 2

ALIFE = MAXLIFE * 1 / 100
ADMG = MAXLIFE * 2 / 100

BLIFE = MAXLIFE * 3 / 100
BDMG = MAXLIFE * 5 / 100

CLIFE = MAXLIFE * 6 / 100
CDMG = MAXLIFE * 7 / 100

DLIFE = MAXLIFE * 8 / 100
DDMG = MAXLIFE * 10 / 100

ELIFE = MAXLIFE * 15 / 100
EDMG = MAXLIFE * 15 / 100

#knockback distance
ABACK = 100
BBACK = 80
CBACK = 60
DBACK = 40
EBACK = 20

TOWERDMG = MAXLIFE * 3 / 100

#A (Wonderbot)
AWIDTH = int(math.floor(32*2))
AHEIGHT = int(math.floor(48*2))
SURFA = pygame.Surface((AWIDTH,AHEIGHT))
SURFA.fill(COLORA)
SURFA.set_colorkey(COLORA)
A1 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile000.png").convert_alpha(),(AWIDTH,AHEIGHT))
A2 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile001.png").convert_alpha(),(AWIDTH,AHEIGHT))
A3 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile002.png").convert_alpha(),(AWIDTH,AHEIGHT))
A4 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile003.png").convert_alpha(),(AWIDTH,AHEIGHT))
A5 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile004.png").convert_alpha(),(AWIDTH,AHEIGHT))
A6 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut/tile005.png").convert_alpha(),(AWIDTH,AHEIGHT))

eA1 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile000.png").convert_alpha(),(AWIDTH,AHEIGHT))
eA2 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile001.png").convert_alpha(),(AWIDTH,AHEIGHT))
eA3 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile002.png").convert_alpha(),(AWIDTH,AHEIGHT))
eA4 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile003.png").convert_alpha(),(AWIDTH,AHEIGHT))
eA5 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile004.png").convert_alpha(),(AWIDTH,AHEIGHT))
eA6 = pygame.transform.scale(pygame.image.load("./sprites/wonderbot/wonderbot-cut-2/tile005.png").convert_alpha(),(AWIDTH,AHEIGHT))

#B (Drone)
BWIDTH = int(math.floor(48*2))
BHEIGHT = int(math.floor(32*2))
SURFB = pygame.Surface((BWIDTH,BHEIGHT))
SURFB.fill(COLORB)
SURFB.set_colorkey(COLORB)
B1 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile000.png").convert_alpha(),(BWIDTH,BHEIGHT))
B2 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile001.png").convert_alpha(),(BWIDTH,BHEIGHT))
B3 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile002.png").convert_alpha(),(BWIDTH,BHEIGHT))
B4 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile003.png").convert_alpha(),(BWIDTH,BHEIGHT))
B5 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile004.png").convert_alpha(),(BWIDTH,BHEIGHT))
B6 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile005.png").convert_alpha(),(BWIDTH,BHEIGHT))
B7 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile006.png").convert_alpha(),(BWIDTH,BHEIGHT))
B8 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut/tile007.png").convert_alpha(),(BWIDTH,BHEIGHT))

eB1 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile000.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB2 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile001.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB3 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile002.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB4 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile003.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB5 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile004.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB6 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile005.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB7 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile006.png").convert_alpha(),(BWIDTH,BHEIGHT))
eB8 = pygame.transform.scale(pygame.image.load("./sprites/drone/drone-cut-2/tile007.png").convert_alpha(),(BWIDTH,BHEIGHT))

#C (RobotArm)
CWIDTH = 25*3
CHEIGHT = 25*3
SURFC = pygame.Surface((CWIDTH,CHEIGHT))
SURFC.fill(COLORC)
SURFC.set_colorkey(COLORC)
C1 = pygame.transform.scale(pygame.image.load("./sprites/robotarm/robotarm-cut/tile000.png").convert_alpha(),(CWIDTH,CHEIGHT))
C2 = pygame.transform.scale(pygame.image.load("./sprites/robotarm/robotarm-cut/tile001.png").convert_alpha(),(CWIDTH,CHEIGHT))

eC1 = pygame.transform.scale(pygame.image.load("./sprites/robotarm/robotarm-cut-2/tile000.png").convert_alpha(),(CWIDTH,CHEIGHT))
eC2 = pygame.transform.scale(pygame.image.load("./sprites/robotarm/robotarm-cut-2/tile001.png").convert_alpha(),(CWIDTH,CHEIGHT))

#D (WallE)
DWIDTH = int(math.floor(32*2))
DHEIGHT = int(math.floor(32*2))
SURFD = pygame.Surface((DWIDTH,DHEIGHT))
SURFD.fill(COLORD)
SURFD.set_colorkey(COLORD)
D1 = pygame.transform.scale(pygame.image.load("./sprites/walle/walle-cut/tile000.png").convert_alpha(),(DWIDTH,DHEIGHT))
D2 = pygame.transform.scale(pygame.image.load("./sprites/walle/walle-cut/tile001.png").convert_alpha(),(DWIDTH,DHEIGHT))

eD1 = pygame.transform.scale(pygame.image.load("./sprites/walle/walle-cut-2/tile000.png").convert_alpha(),(DWIDTH,DHEIGHT))
eD2 = pygame.transform.scale(pygame.image.load("./sprites/walle/walle-cut-2/tile001.png").convert_alpha(),(DWIDTH,DHEIGHT))

#E (3310)
EWIDTH = int(math.floor(22*2))
EHEIGHT = int(math.floor(48*2))
SURFE = pygame.Surface((EWIDTH,EHEIGHT))
SURFE.fill(COLORE)
SURFE.set_colorkey(COLORE)
E1 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut/tile000.png").convert_alpha(),(EWIDTH,EHEIGHT))
E2 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut/tile001.png").convert_alpha(),(EWIDTH,EHEIGHT))
E3 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut/tile002.png").convert_alpha(),(EWIDTH,EHEIGHT))
E4 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut/tile003.png").convert_alpha(),(EWIDTH,EHEIGHT))

eE1 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut-2/tile000.png").convert_alpha(),(EWIDTH,EHEIGHT))
eE2 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut-2/tile001.png").convert_alpha(),(EWIDTH,EHEIGHT))
eE3 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut-2/tile002.png").convert_alpha(),(EWIDTH,EHEIGHT))
eE4 = pygame.transform.scale(pygame.image.load("./sprites/3310/3310-cut-2/tile003.png").convert_alpha(),(EWIDTH,EHEIGHT))

#100s set
#ONE = [1,2,1,2,3,3,2,2,2,2]
#TWO = [1,2,1,2,2,2,2,3,2,3]
#THREE = [1,2,2,3,4,3,2,3]
#FOUR = [2,2,4,4,2,2,2,2]
#FIVE = [2,5,5,4,4]
#SIX = [4,4,4,4,4]
#SEVEN = [1,2,4,5,4,4]
#EIGHT = [1,2,3,1,2,3,3,2,3]

ONE = [1,2,3,2,3]
TWO = [2,3,1,3,5]
THREE = [3,2,1,1,3]
FOUR = [2,3,2,1,5]
FIVE = [2,3,1,3,4]
SIX = [1,2,1,4,5]
SEVEN = [1,2,4,3,5]
EIGHT = [3,4,3,1,5]

TheBackground = pygame.transform.scale(pygame.image.load("./sprites/background.png").convert_alpha(),(1000,400))
TheInsScreen = pygame.transform.scale(pygame.image.load("./sprites/theinsscreen.png").convert_alpha(),(SCREENWIDTH,SCREENHEIGHT))

def startscreen():
    running = True
    while running:
        Display.fill(BLACK) #background
        
        #TITLE
        Title = BigFont.render("War.tomation",True,WHITE)
        TitleRect = Title.get_rect()
        TitleRect.center = (SCREENWIDTH/2, TitleRect.height*2)
        Display.blit(Title,TitleRect)

        #ICON
        IconRect = Rect(0,0,E2.get_rect().width,E2.get_rect().height)
        IconRect.right = TitleRect.left-10
        IconRect.centery = TitleRect.centery + 10
        Display.blit(E2,IconRect)

        #Maker
        Maker = SmallFont.render("by JCLOH",True,GREY)
        MakerRect = Maker.get_rect()
        MakerRect.center = (SCREENWIDTH/2, TitleRect.centery + MakerRect.height)
        Display.blit(Maker,MakerRect)

        mousepos = pygame.mouse.get_pos()

        StartButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        StartButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2)

        InsButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        InsButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + BUTTONHEIGHT)

        ExitButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
        ExitButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + 2*BUTTONHEIGHT)

        pygame.draw.rect(Display,GREY,StartButton)
        Start = SmallFont.render("Start",True,WHITE)
        StartRect = Start.get_rect()
        StartRect.center = StartButton.center
        Display.blit(Start,StartRect)

        pygame.draw.rect(Display,WHITE,InsButton)
        Ins = SmallFont.render("Instruction",True,BLACK)
        InsRect = Ins.get_rect()
        InsRect.center = InsButton.center
        Display.blit(Ins,InsRect)

        pygame.draw.rect(Display,GREY,ExitButton)
        Exit = SmallFont.render("Exit",True,WHITE)
        ExitRect = Exit.get_rect()
        ExitRect.center = ExitButton.center
        Display.blit(Exit,ExitRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() == LEFT_CLICK):
                    if (StartButton.collidepoint(mousepos)):
                        #print("Start")
                        running = False

                    elif (InsButton.collidepoint(mousepos)):
                        #print("Instructions")
                        insscreen()

                    elif (ExitButton.collidepoint(mousepos)):
                        #print("Exit")
                        pygame.quit()
                        sys.exit()

                pass


        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def insscreen():
    #print ("InsScreen")
    running = True
    BackButton = Rect(0,0,BUTTONWIDTH,BUTTONHEIGHT)
    BackButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + BackButton.height)
    Back = SmallFont.render("Back to main menu",True,WHITE)
    BackRect = Back.get_rect()
    BackRect.center = BackButton.center

    Title = BigFont.render("How to play?",True,WHITE)
    while running:
        mousepos = pygame.mouse.get_pos()
        Display.fill(GREY)
        Display.blit(TheInsScreen,(0,0))
        pygame.draw.rect(Display,BLACK,BackButton)
        Display.blit(Back,BackRect)
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() == LEFT_CLICK):
                    if (BackButton.collidepoint(mousepos)):
                        running = False

        pygame.display.update()
        pygame.time.Clock().tick(FPS)
    pass

def endscreen(result):
    #print("EndScreen")
    running = True
    ReplayButton = Rect(0,0,BUTTONWIDTH/2,BUTTONHEIGHT)
    ReplayButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + ReplayButton.height)

    ExitButton = Rect(0,0,BUTTONWIDTH/2,BUTTONHEIGHT)
    ExitButton.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + ExitButton.height*2)

    Replay = SmallFont.render("Play Again",True,WHITE)
    ReplayRect = Replay.get_rect()
    ReplayRect.center = ReplayButton.center

    Exit = SmallFont.render("Exit",True,BLACK)
    ExitRect = Exit.get_rect()
    ExitRect.center = ExitButton.center

    if result:
        Result = BigFont.render("Congrats! You win!",True,WHITE)
        ResultRect = Result.get_rect()
        ResultRect.center = (SCREENWIDTH/2,ResultRect.height*2)

    else: #result == False
        Result = BigFont.render("GG! You lose!",True,WHITE)
        ResultRect = Result.get_rect()
        ResultRect.center = (SCREENWIDTH/2,ResultRect.height*2)

    Credit1 = SmallFont.render("Font: Carbon, by Raymond Labarie",True,GREY)
    CreditRect1 = Credit1.get_rect()
    CreditRect1.top = ResultRect.bottom
    CreditRect1.centerx = ResultRect.centerx

    FontSource = SmallerFont.render("https://www.1001fonts.com/carbon-font.html",True,WHITE)
    FontSourceRect = FontSource.get_rect()
    FontSourceRect.top = CreditRect1.bottom
    FontSourceRect.centerx = ResultRect.centerx
    
    Credit = SmallFont.render("BGM from Resistor Anthems, by Eric Skiff",True,GREY)
    CreditRect = Credit.get_rect()
    CreditRect.top = FontSourceRect.bottom
    CreditRect.centerx = ResultRect.centerx
    
    Name1 = SmallerFont.render("Eric Skiff - All of Us - Resistor Anthems - Available at http://EricSkiff.com/music",True,WHITE)
    Name1Rect = Name1.get_rect()
    Name1Rect.top = CreditRect.bottom
    Name1Rect.centerx = ResultRect.centerx
    
    Name2 = SmallerFont.render("Eric Skiff - Come and Find Me - B mix - Resistor Anthems - Available at http://EricSkiff.com/music",True,WHITE)
    Name2Rect = Name2.get_rect()
    Name2Rect.top = Name1Rect.bottom
    Name2Rect.centerx = ResultRect.centerx
    
    Name3 = SmallerFont.render("Eric Skiff - We're the Resistors - Resistor Anthems - Available at http://EricSkiff.com/music",True,WHITE)
    Name3Rect = Name3.get_rect()
    Name3Rect.top = Name2Rect.bottom
    Name3Rect.centerx = ResultRect.centerx

    pygame.mixer.init()
    pygame.mixer.music.load("./music/We're the Resistors.mp3")
    pygame.mixer.music.play(-1,0.0)
    
    while running:
        mousepos = pygame.mouse.get_pos()
        Display.fill(BLACK)
        pygame.draw.rect(Display,GREY,ReplayButton)
        Display.blit(Replay,ReplayRect)
        pygame.draw.rect(Display,WHITE,ExitButton)
        Display.blit(Credit1,CreditRect1)
        Display.blit(FontSource,FontSourceRect)
        Display.blit(Credit,CreditRect)
        Display.blit(Name1,Name1Rect)
        Display.blit(Name2,Name2Rect)
        Display.blit(Name3,Name3Rect)

        Display.blit(Exit,ExitRect)
        Display.blit(Result,ResultRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() == LEFT_CLICK):
                    if (ReplayButton.collidepoint(mousepos)):
                        pygame.mixer.music.stop()
                        return True
                    if (ExitButton.collidepoint(mousepos)):
                        pygame.mixer.music.stop()
                        return False

        pygame.display.update()
        pygame.time.Clock().tick(FPS)
    pass

def background():
    Display.blit(TheBackground,Rect(0,0,1000,400))
    pygame.draw.rect(Display,(212, 209, 104),Rect(0,400,1000,100))

class Player:
    def __init__(self,maxlife):
        self.main = maxlife
        self.tower1 = maxlife * 30 / 100
        self.tower2 = maxlife * 40 / 100
        self.tower3 = maxlife * 50 / 100

        self.playergold = 0

        #minion boxes
        self.ABox = pygame.Surface((MINIONBOXWIDTH,MINIONBOXHEIGHT))
        self.ABox.fill(WHITE)
        self.ABox.set_alpha(100)
        self.ARect = self.ABox.get_rect()
        self.ARect.center = (MINIONBOXWIDTH, SCREENHEIGHT - MINIONBOXHEIGHT)

        self.BBox = pygame.Surface((MINIONBOXWIDTH,MINIONBOXHEIGHT))
        self.BBox.fill(WHITE)
        self.BBox.set_alpha(100)
        self.BRect = self.ABox.get_rect()
        self.BRect.center = (MINIONBOXWIDTH*3, SCREENHEIGHT - MINIONBOXHEIGHT)

        self.CBox = pygame.Surface((MINIONBOXWIDTH,MINIONBOXHEIGHT))
        self.CBox.fill(WHITE)
        self.CBox.set_alpha(100)
        self.CRect = self.ABox.get_rect()
        self.CRect.center = (MINIONBOXWIDTH*5, SCREENHEIGHT - MINIONBOXHEIGHT)

        self.DBox = pygame.Surface((MINIONBOXWIDTH,MINIONBOXHEIGHT))
        self.DBox.fill(WHITE)
        self.DBox.set_alpha(100)
        self.DRect = self.ABox.get_rect()
        self.DRect.center = (MINIONBOXWIDTH*7, SCREENHEIGHT - MINIONBOXHEIGHT)

        self.EBox = pygame.Surface((MINIONBOXWIDTH,MINIONBOXHEIGHT))
        self.EBox.fill(WHITE)
        self.EBox.set_alpha(100)
        self.ERect = self.ABox.get_rect()
        self.ERect.center = (MINIONBOXWIDTH*9, SCREENHEIGHT - MINIONBOXHEIGHT)

        #main box
        self.mainBox = pygame.Surface((MAINBOXWIDTH,MAINBOXHEIGHT))
        self.mainBox.fill(BLUE)
        self.mainBox.set_colorkey(BLUE)
        self.mainRect = self.mainBox.get_rect()
        self.mainRect.center = (MAINBOXWIDTH/2, SCREENHEIGHT*2/5)

        #towers box
        self.tower1Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower1Box.fill(LIGHTBLUE)
        self.tower1Box.set_colorkey(LIGHTBLUE)
        self.tower1Rect = self.tower1Box.get_rect()
        self.tower1Rect.center = (MAINBOXWIDTH*1.5, self.mainRect.centery - TOWERBOXHEIGHT - TOWERINTERVAL)

        self.tower3Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower3Box.fill(LIGHTBLUE)
        self.tower3Box.set_colorkey(LIGHTBLUE)
        self.tower3Rect = self.tower1Box.get_rect()
        self.tower3Rect.center = (MAINBOXWIDTH*1.5, self.mainRect.centery)

        self.tower2Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower2Box.fill(LIGHTBLUE)
        self.tower2Box.set_colorkey(LIGHTBLUE)
        self.tower2Rect = self.tower1Box.get_rect()
        self.tower2Rect.center = (MAINBOXWIDTH*1.5, self.mainRect.centery + TOWERBOXHEIGHT + TOWERINTERVAL)

        self.FirstDefRect = Rect(0,0,TOWERBOXWIDTH,SCREENHEIGHT-100)
        self.FirstDefRect.centerx = self.tower2Rect.centerx

        self.SecondDefRect = Rect(0,0,MAINBOXWIDTH,SCREENHEIGHT)
        self.SecondDefRect.center = self.mainRect.center

        #minions variables
        self.lenA = 0
        self.lenB = 0
        self.lenC = 0
        self.lenD = 0
        self.lenE = 0

        self.AList = [] #store the rect
        self.BList = []
        self.CList = []
        self.DList = []
        self.EList = []

        self.ALifeList = []
        self.BLifeList = []
        self.CLifeList = []
        self.DLifeList = []
        self.ELifeList = []

        pass

    def AddPlayerGold(self,gold):
        self.playergold += gold

    def MinusPlayerGold(self,gold):
        self.playergold -= gold

    def Available(self,Surf):
        Surf.set_alpha(255)

    def NotAvailable(self,Surf):
        Surf.set_alpha(100)


class Enemy:
    def __init__(self,maxlife):
        self.main = maxlife
        self.tower1 = maxlife * 30 / 100
        self.tower2 = maxlife * 40 / 100
        self.tower3 = maxlife * 50 / 100

        self.enemygold = 0

        self.mainBox = pygame.Surface((MAINBOXWIDTH,MAINBOXHEIGHT))
        self.mainBox.fill(RED)
        self.mainBox.set_colorkey(RED)
        self.mainRect = self.mainBox.get_rect()
        self.mainRect.center = (SCREENWIDTH - MAINBOXWIDTH/2, SCREENHEIGHT*2/5)

        self.tower1Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower1Box.fill(LIGHTRED)
        self.tower1Box.set_colorkey(LIGHTRED)
        self.tower1Rect = self.tower1Box.get_rect()
        self.tower1Rect.center = (SCREENWIDTH - MAINBOXWIDTH*1.5, self.mainRect.centery - TOWERBOXHEIGHT - TOWERINTERVAL)

        self.tower3Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower3Box.fill(LIGHTRED)
        self.tower3Box.set_colorkey(LIGHTRED)
        self.tower3Rect = self.tower1Box.get_rect()
        self.tower3Rect.center = (SCREENWIDTH - MAINBOXWIDTH*1.5, self.mainRect.centery)

        self.tower2Box = pygame.Surface((TOWERBOXWIDTH,TOWERBOXHEIGHT))
        self.tower2Box.fill(LIGHTRED)
        self.tower2Box.set_colorkey(LIGHTRED)
        self.tower2Rect = self.tower1Box.get_rect()
        self.tower2Rect.center = (SCREENWIDTH - MAINBOXWIDTH*1.5, self.mainRect.centery + TOWERBOXHEIGHT + TOWERINTERVAL)

        self.FirstDefRect = Rect(0,0,TOWERBOXWIDTH,SCREENHEIGHT-100)
        self.FirstDefRect.centerx = self.tower2Rect.centerx

        self.SecondDefRect = Rect(0,0,MAINBOXWIDTH,SCREENHEIGHT)
        self.SecondDefRect.center = self.mainRect.center

        #minions variables
        self.lenA = 0
        self.lenB = 0
        self.lenC = 0
        self.lenD = 0
        self.lenE = 0

        self.AList = [] #store the rect
        self.BList = []
        self.CList = []
        self.DList = []
        self.EList = []

        self.ALifeList = []
        self.BLifeList = []
        self.CLifeList = []
        self.DLifeList = []
        self.ELifeList = []

        #which set?
        self.thelist = []
        self.randnum = 0

    def AddEnemyGold(self,gold):
        self.enemygold += gold

    def MinusEnemyGold(self,gold):
        self.enemygold -= gold

    pass

def main():
    TheTime = 0
    Start = time.time()#start time

    #player
    player = Player(MAXLIFE)

    #enemy
    enemy = Enemy(MAXLIFE)

    #use to check the FPS
    frame = 0;
    realtimeFPS = 0
    previousFrame = 0

    #animations
    towercount = 0
    acount = bcount = ccount = dcount = ecount = 0

    #pause condition
    pause = False
    pausecondition = False

    pygame.mixer.init()
    pygame.mixer.music.load("./music/All of Us.mp3")
    pygame.mixer.music.play(-1,0.0)

    while True:
        background() #background

        #playergold word
        PlayerGoldWord = SmallerFont.render(" Player Power: ",True,WHITE)
        PlayerGoldWordRect = PlayerGoldWord.get_rect()
        Display.blit(PlayerGoldWord, PlayerGoldWordRect)

        PlayerLifeWord = SmallerFont.render("Main Life (%): ",True,WHITE)
        PlayerLifeWordRect = PlayerLifeWord.get_rect()
        PlayerLifeWordRect.top = PlayerGoldWordRect.bottom
        PlayerLifeWordRect.centerx = PlayerGoldWordRect.centerx
        Display.blit(PlayerLifeWord, PlayerLifeWordRect)

        PlayerT1Word = SmallerFont.render("Tower 1 (%): ",True,WHITE)
        PlayerT1WordRect = PlayerT1Word.get_rect()
        PlayerT1WordRect.top = PlayerLifeWordRect.bottom
        PlayerT1WordRect.centerx = PlayerGoldWordRect.centerx
        Display.blit(PlayerT1Word, PlayerT1WordRect)

        PlayerT2Word = SmallerFont.render("Tower 2 (%): ",True,WHITE)
        PlayerT2WordRect = PlayerT2Word.get_rect()
        PlayerT2WordRect.top = PlayerT1WordRect.bottom
        PlayerT2WordRect.centerx = PlayerGoldWordRect.centerx
        Display.blit(PlayerT2Word, PlayerT2WordRect)

        PlayerT3Word = SmallerFont.render("Tower 3 (%): ",True,WHITE)
        PlayerT3WordRect = PlayerT3Word.get_rect()
        PlayerT3WordRect.top = PlayerT2WordRect.bottom
        PlayerT3WordRect.centerx = PlayerGoldWordRect.centerx
        Display.blit(PlayerT3Word, PlayerT3WordRect)

        #enemygold word
        EnemyGoldWord = SmallerFont.render(" :Enemy Power ",True,WHITE)
        EnemyGoldWordRect = EnemyGoldWord.get_rect()
        EnemyGoldWordRect.right = SCREENWIDTH
        Display.blit(EnemyGoldWord, EnemyGoldWordRect)

        EnemyLifeWord = SmallerFont.render(" :(%) Main Life",True,WHITE)
        EnemyLifeWordRect = EnemyLifeWord.get_rect()
        EnemyLifeWordRect.top = EnemyGoldWordRect.bottom
        EnemyLifeWordRect.centerx = EnemyGoldWordRect.centerx
        Display.blit(EnemyLifeWord, EnemyLifeWordRect)

        EnemyT1Word = SmallerFont.render(" :(%) Tower 1",True,WHITE)
        EnemyT1WordRect = EnemyT1Word.get_rect()
        EnemyT1WordRect.top = EnemyLifeWordRect.bottom
        EnemyT1WordRect.centerx = EnemyGoldWordRect.centerx
        Display.blit(EnemyT1Word, EnemyT1WordRect)

        EnemyT2Word = SmallerFont.render(" :(%) Tower 2",True,WHITE)
        EnemyT2WordRect = EnemyT2Word.get_rect()
        EnemyT2WordRect.top = EnemyT1WordRect.bottom
        EnemyT2WordRect.centerx = EnemyGoldWordRect.centerx
        Display.blit(EnemyT2Word, EnemyT2WordRect)

        EnemyT3Word = SmallerFont.render(" :(%) Tower 3",True,WHITE)
        EnemyT3WordRect = EnemyT3Word.get_rect()
        EnemyT3WordRect.top = EnemyT2WordRect.bottom
        EnemyT3WordRect.centerx = EnemyGoldWordRect.centerx
        Display.blit(EnemyT3Word, EnemyT3WordRect)

        End = time.time()#end time

        #for FPS
        frame += 1
        if (int(End) - int(Start) == 1):
                        TheTime += 1
                        Start = time.time()
                        player.AddPlayerGold(GOLDAMOUNT)
                        enemy.AddEnemyGold(GOLDAMOUNT)
                        #print(player.playergold)
                        #print(TheTime)
                        realtimeFPS = (frame - previousFrame)
                        #print("RealTimeFPS:", realtimeFPS,"\n")
                        previousFrame = frame

        mousepos = pygame.mouse.get_pos()

        #ANIMATIONS LOGICS
        towercount += 1
        acount += 1
        bcount += 1
        ccount += 1
        dcount += 1
        ecount += 1
        if (towercount >= 2*(FPS/4)):
            towercount = 0
        if (acount >= 6*(FPS/6)):
            acount = 0
        if (bcount >= 8*(FPS/8)):
            bcount = 0
        if (ccount >= 2*(FPS/8)):
            ccount = 0
        if (dcount >= 2*(FPS/4)):
            dcount = 0
        if (ecount >= 4*(FPS/8)):
            ecount = 0

        #LOGICS
        #availability condition
        if (player.playergold >= AGOLD):
            player.Available(player.ABox)
        else:
            player.NotAvailable(player.ABox)

        if (player.playergold >= BGOLD):
            player.Available(player.BBox)
        else:
            player.NotAvailable(player.BBox)

        if (player.playergold >= CGOLD):
            player.Available(player.CBox)
        else:
            player.NotAvailable(player.CBox)

        if (player.playergold >= DGOLD):
            player.Available(player.DBox)
        else:
            player.NotAvailable(player.DBox)

        if (player.playergold >= EGOLD):
            player.Available(player.EBox)
        else:
            player.NotAvailable(player.EBox)

        #damage system
        #collide with tower (player A)
        for i in range(player.lenA):
            if (player.AList[i].colliderect(enemy.FirstDefRect)): #player collided with enemy towers
                if (enemy.tower1 > 0):
                    enemy.tower1 -= ADMG #A causes damage
                    player.AList[i].centerx -= ABACK
                    player.ALifeList[i] -= TOWERDMG
                elif (enemy.tower2 > 0):
                    enemy.tower2 -= ADMG
                    player.AList[i].centerx -= ABACK
                    player.ALifeList[i] -= TOWERDMG
                    pass
                elif (enemy.tower3 > 0):
                    enemy.tower3 -= ADMG
                    player.AList[i].centerx -= ABACK
                    player.ALifeList[i] -= TOWERDMG
                    pass

        #collide with tower (player B)
        for i in range(player.lenB):
            if (player.BList[i].colliderect(enemy.FirstDefRect)): #player collided with enemy towers
                if (enemy.tower1 > 0):
                    enemy.tower1 -= BDMG #B causes damage
                    player.BList[i].centerx -= BBACK
                    player.BLifeList[i] -= TOWERDMG
                elif (enemy.tower2 > 0):
                    enemy.tower2 -= BDMG
                    player.BList[i].centerx -= BBACK
                    player.BLifeList[i] -= TOWERDMG
                    pass
                elif (enemy.tower3 > 0):
                    enemy.tower3 -= BDMG
                    player.BList[i].centerx -= BBACK
                    player.BLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (player C)
        for i in range(player.lenC):
            if (player.CList[i].colliderect(enemy.FirstDefRect)): #player collided with enemy towers
                if (enemy.tower1 > 0):
                    enemy.tower1 -= MAXLIFE * 5 /100 #C causes damage
                    player.CList[i].centerx -= CBACK
                    player.CLifeList[i] -= TOWERDMG
                elif (enemy.tower2 > 0):
                    enemy.tower2 -= MAXLIFE * 5 /100
                    player.CList[i].centerx -= CBACK
                    player.CLifeList[i] -= TOWERDMG
                    pass
                elif (enemy.tower3 > 0):
                    enemy.tower3 -= MAXLIFE * 5 /100
                    player.CList[i].centerx -= CBACK
                    player.CLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (player D)
        for i in range(player.lenD):
            if (player.DList[i].colliderect(enemy.FirstDefRect)): #player collided with enemy towers
                if (enemy.tower1 > 0):
                    enemy.tower1 -= DDMG #D causes damage
                    player.DList[i].centerx -= DBACK
                    player.DLifeList[i] -= TOWERDMG
                elif (enemy.tower2 > 0):
                    enemy.tower2 -= DDMG
                    player.DList[i].centerx -= DBACK
                    player.DLifeList[i] -= TOWERDMG
                    pass
                elif (enemy.tower3 > 0):
                    enemy.tower3 -= DDMG
                    player.DList[i].centerx -= DBACK
                    player.DLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (player E)
        for i in range(player.lenE):
            if (player.EList[i].colliderect(enemy.FirstDefRect)): #player collided with enemy towers
                if (enemy.tower1 > 0):
                    enemy.tower1 -= EDMG #E causes damage
                    player.EList[i].centerx -= EBACK
                    player.ELifeList[i] -= TOWERDMG
                elif (enemy.tower2 > 0):
                    enemy.tower2 -= EDMG
                    player.EList[i].centerx -= EBACK
                    player.ELifeList[i] -= TOWERDMG
                    pass
                elif (enemy.tower3 > 0):
                    enemy.tower3 -= EDMG
                    player.EList[i].centerx -= EBACK
                    player.ELifeList[i] -= TOWERDMG
                    pass

        #collide main (player hit enemy)
        if (enemy.tower1 <= 0 and enemy.tower2 <= 0 and enemy.tower3 <= 0):
            if (enemy.main > 0):
                for i in range(player.lenA):
                    if (player.AList[i].colliderect(enemy.mainRect)):
                        enemy.main -= ADMG
                        player.AList[i].centerx -= ABACK

                for i in range(player.lenB):
                    if (player.BList[i].colliderect(enemy.mainRect)):
                        enemy.main -= BDMG
                        player.BList[i].centerx -= BBACK

                for i in range(player.lenC):
                    if (player.CList[i].colliderect(enemy.mainRect)):
                        enemy.main -= CDMG
                        player.CList[i].centerx -= CBACK

                for i in range(player.lenD):
                    if (player.DList[i].colliderect(enemy.mainRect)):
                        enemy.main -= DDMG
                        player.DList[i].centerx -= DBACK

                for i in range(player.lenE):
                    if (player.EList[i].colliderect(enemy.mainRect)):
                        enemy.main -= EDMG
                        player.EList[i].centerx -= EBACK

        #collide main (enemy hit player)
        if (player.tower1 <= 0 and player.tower2 <= 0 and player.tower3 <= 0):
            if (player.main > 0):
                for i in range(enemy.lenA):
                    if (enemy.AList[i].colliderect(player.mainRect)):
                        player.main -= ADMG
                        enemy.AList[i].centerx += ABACK

                for i in range(enemy.lenB):
                    if (enemy.BList[i].colliderect(player.mainRect)):
                        player.main -= BDMG
                        enemy.BList[i].centerx += BBACK

                for i in range(enemy.lenC):
                    if (enemy.CList[i].colliderect(player.mainRect)):
                        player.main -= CDMG
                        enemy.CList[i].centerx += CBACK

                for i in range(enemy.lenD):
                    if (enemy.DList[i].colliderect(player.mainRect)):
                        player.main -= DDMG
                        enemy.DList[i].centerx += DBACK

                for i in range(enemy.lenE):
                    if (enemy.EList[i].colliderect(player.mainRect)):
                        player.main -= EDMG
                        enemy.EList[i].centerx += EBACK

        #collide with tower (enemy A)
        for i in range(enemy.lenA):
            if (enemy.AList[i].colliderect(player.FirstDefRect)): #enemy collided with player towers
                if (player.tower1 > 0):
                    player.tower1 -= ADMG #A causes damage
                    enemy.AList[i].centerx += ABACK
                    enemy.ALifeList[i] -= TOWERDMG
                elif (player.tower2 > 0):
                    player.tower2 -= ADMG
                    enemy.AList[i].centerx += ABACK
                    enemy.ALifeList[i] -= TOWERDMG
                    pass
                elif (player.tower3 > 0):
                    player.tower3 -= ADMG
                    enemy.AList[i].centerx += ABACK
                    enemy.ALifeList[i] -= TOWERDMG
                    pass

        #collide with tower (enemy B)
        for i in range(enemy.lenB):
            if (enemy.BList[i].colliderect(player.FirstDefRect)): #enemy collided with player towers
                if (player.tower1 > 0):
                    player.tower1 -= BDMG #B causes damage
                    enemy.BList[i].centerx += BBACK
                    enemy.BLifeList[i] -= TOWERDMG
                elif (player.tower2 > 0):
                    player.tower2 -= BDMG
                    enemy.BList[i].centerx += BBACK
                    enemy.BLifeList[i] -= TOWERDMG
                    pass
                elif (player.tower3 > 0):
                    player.tower3 -= BDMG
                    enemy.BList[i].centerx += BBACK
                    enemy.BLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (enemy C)
        for i in range(enemy.lenC):
            if (enemy.CList[i].colliderect(player.FirstDefRect)): #enemy collided with player towers
                if (player.tower1 > 0):
                    player.tower1 -= CDMG #C causes damage
                    enemy.CList[i].centerx += CBACK
                    enemy.CLifeList[i] -= TOWERDMG
                elif (player.tower2 > 0):
                    player.tower2 -= CDMG
                    enemy.CList[i].centerx += CBACK
                    enemy.CLifeList[i] -= TOWERDMG
                    pass
                elif (player.tower3 > 0):
                    player.tower3 -= CDMG
                    enemy.CList[i].centerx += CBACK
                    enemy.CLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (enemy D)
        for i in range(enemy.lenD):
            if (enemy.DList[i].colliderect(player.FirstDefRect)): #enemy collided with player towers
                if (player.tower1 > 0):
                    player.tower1 -= DDMG #D causes damage
                    enemy.DList[i].centerx += DBACK
                    enemy.DLifeList[i] -= TOWERDMG
                elif (player.tower2 > 0):
                    player.tower2 -= DDMG
                    enemy.DList[i].centerx += DBACK
                    enemy.DLifeList[i] -= TOWERDMG
                    pass
                elif (player.tower3 > 0):
                    player.tower3 -= DDMG
                    enemy.DList[i].centerx += DBACK
                    enemy.DLifeList[i] -= TOWERDMG
                    pass

        #collide with tower (enemy E)
        for i in range(enemy.lenE):
            if (enemy.EList[i].colliderect(player.FirstDefRect)): #enemy collided with player towers
                if (player.tower1 > 0):
                    player.tower1 -= EDMG #E causes damage
                    enemy.EList[i].centerx += EBACK
                    enemy.ELifeList[i] -= TOWERDMG
                elif (player.tower2 > 0):
                    player.tower2 -= EDMG
                    enemy.EList[i].centerx += EBACK
                    enemy.ELifeList[i] -= TOWERDMG
                    pass
                elif (player.tower3 > 0):
                    player.tower3 -= EDMG
                    enemy.EList[i].centerx += EBACK
                    enemy.ELifeList[i] -= TOWERDMG
                    pass

        #collided with enemy minions (player A)
        for i in range(player.lenA):
            for j in range(enemy.lenA):#PA hit EA
                if (player.AList[i].colliderect(enemy.AList[j])):
                    player.ALifeList[i] -= ADMG #EA causes damage
                    enemy.ALifeList[j] -= ADMG #PA causes damage
                    player.AList[i].centerx -= ABACK
                    enemy.AList[j].centerx += ABACK

            for j in range(enemy.lenB):#PA hit EB
                if (player.AList[i].colliderect(enemy.BList[j])):
                    player.ALifeList[i] -= BDMG #EB causes damage
                    enemy.BLifeList[j] -=  ADMG #PA causes damage
                    player.AList[i].centerx -= ABACK
                    enemy.BList[j].centerx += BBACK

            for j in range(enemy.lenC):#PA hit EC
                if (player.AList[i].colliderect(enemy.CList[j])):
                    player.ALifeList[i] -= CDMG #EC causes damage
                    enemy.CLifeList[j] -= ADMG #PA causes damage
                    player.AList[i].centerx -= ABACK
                    enemy.CList[j].centerx += BBACK

            for j in range(enemy.lenD):#PA hit ED
                if (player.AList[i].colliderect(enemy.DList[j])):
                    player.ALifeList[i] -= DDMG #ED causes damage
                    enemy.DLifeList[j] -= ADMG #PA causes damage
                    player.AList[i].centerx -= ABACK
                    enemy.DList[j].centerx += BBACK

            for j in range(enemy.lenE):#PA hit EE
                if (player.AList[i].colliderect(enemy.EList[j])):
                    player.ALifeList[i] -= EDMG #EE causes damage
                    enemy.ELifeList[j] -= ADMG #PA causes damage
                    player.AList[i].centerx -= ABACK
                    enemy.EList[j].centerx += BBACK

        #collided with enemy minions (player B)
        for i in range(player.lenB):
            for j in range(enemy.lenA):#PB hit EA
                if (player.BList[i].colliderect(enemy.AList[j])):
                    player.BLifeList[i] -= ADMG #EA causes damage
                    enemy.ALifeList[j] -= BDMG #PB causes damage
                    player.BList[i].centerx -= BBACK
                    enemy.AList[j].centerx += ABACK

            for j in range(enemy.lenB):#PB hit EB
                if (player.BList[i].colliderect(enemy.BList[j])):
                    player.BLifeList[i] -= BDMG #EB causes damage
                    enemy.BLifeList[j] -= BDMG #PB causes damage
                    player.BList[i].centerx -= BBACK
                    enemy.BList[j].centerx += BBACK

            for j in range(enemy.lenC):#PB hit EC
                if (player.BList[i].colliderect(enemy.CList[j])):
                    player.BLifeList[i] -= CDMG#EC causes damage
                    enemy.CLifeList[j] -= BDMG #PB causes damage
                    player.BList[i].centerx -= BBACK
                    enemy.CList[j].centerx += CBACK

            for j in range(enemy.lenD):#PB hit ED
                if (player.BList[i].colliderect(enemy.DList[j])):
                    player.BLifeList[i] -= DDMG #ED causes damage
                    enemy.DLifeList[j] -= BDMG #PB causes damage
                    player.BList[i].centerx -= BBACK
                    enemy.DList[j].centerx += DBACK

            for j in range(enemy.lenE):#PB hit EE
                if (player.BList[i].colliderect(enemy.EList[j])):
                    player.BLifeList[i] -= EDMG #EE causes damage
                    enemy.ELifeList[j] -= BDMG #PB causes damage
                    player.BList[i].centerx -= BBACK
                    enemy.EList[j].centerx += EBACK

        #collided with enemy minions (player C)
        for i in range(player.lenC):
            for j in range(enemy.lenA):#PC hit EA
                if (player.CList[i].colliderect(enemy.AList[j])):
                    player.CLifeList[i] -= ADMG #EA causes damage
                    enemy.ALifeList[j] -= CDMG #PC causes damage
                    player.CList[i].centerx -= CBACK
                    enemy.AList[j].centerx += ABACK

            for j in range(enemy.lenB):#PC hit EB
                if (player.CList[i].colliderect(enemy.BList[j])):
                    player.CLifeList[i] -= BDMG #EB causes damage
                    enemy.BLifeList[j] -= CDMG #PC causes damage
                    player.CList[i].centerx -= CBACK
                    enemy.BList[j].centerx += BBACK

            for j in range(enemy.lenC):#PC hit EC
                if (player.CList[i].colliderect(enemy.CList[j])):
                    player.CLifeList[i] -= CDMG#EC causes damage
                    enemy.CLifeList[j] -= CDMG #PC causes damage
                    player.CList[i].centerx -= CBACK
                    enemy.CList[j].centerx += CBACK

            for j in range(enemy.lenD):#PC hit ED
                if (player.CList[i].colliderect(enemy.DList[j])):
                    player.CLifeList[i] -= DDMG #ED causes damage
                    enemy.DLifeList[j] -= CDMG #PC causes damage
                    player.CList[i].centerx -= CBACK
                    enemy.DList[j].centerx += DBACK

            for j in range(enemy.lenE):#PC hit EE
                if (player.CList[i].colliderect(enemy.EList[j])):
                    player.CLifeList[i] -= EDMG #EE causes damage
                    enemy.ELifeList[j] -= CDMG #PC causes damage
                    player.CList[i].centerx -= CBACK
                    enemy.EList[j].centerx += EBACK

        #collided with enemy minions (player D)
        for i in range(player.lenD):
            for j in range(enemy.lenA):#PD hit EA
                if (player.DList[i].colliderect(enemy.AList[j])):
                    player.DLifeList[i] -= ADMG #EA causes damage
                    enemy.ALifeList[j] -= DDMG #PD causes damage
                    player.DList[i].centerx -= DBACK
                    enemy.AList[j].centerx += ABACK

            for j in range(enemy.lenB):#PD hit EB
                if (player.DList[i].colliderect(enemy.BList[j])):
                    player.DLifeList[i] -= BDMG #EB causes damage
                    enemy.BLifeList[j] -= DDMG #PD causes damage
                    player.DList[i].centerx -= DBACK
                    enemy.BList[j].centerx += BBACK

            for j in range(enemy.lenC):#PD hit EC
                if (player.DList[i].colliderect(enemy.CList[j])):
                    player.DLifeList[i] -= CDMG#EC causes damage
                    enemy.CLifeList[j] -= DDMG #PD causes damage
                    player.DList[i].centerx -= DBACK
                    enemy.CList[j].centerx += CBACK

            for j in range(enemy.lenD):#PD hit ED
                if (player.DList[i].colliderect(enemy.DList[j])):
                    player.DLifeList[i] -= DDMG #ED causes damage
                    enemy.DLifeList[j] -= DDMG #PD causes damage
                    player.DList[i].centerx -= DBACK
                    enemy.DList[j].centerx += DBACK

            for j in range(enemy.lenE):#PD hit EE
                if (player.DList[i].colliderect(enemy.EList[j])):
                    player.DLifeList[i] -= EDMG #EE causes damage
                    enemy.ELifeList[j] -= DDMG #PD causes damage
                    player.DList[i].centerx -= DBACK
                    enemy.EList[j].centerx += EBACK

        #collided with enemy minions (player E)
        for i in range(player.lenE):
            for j in range(enemy.lenA):#PE hit EA
                if (player.EList[i].colliderect(enemy.AList[j])):
                    player.ELifeList[i] -= ADMG #EA causes damage
                    enemy.ALifeList[j] -= EDMG #PE causes damage
                    player.EList[i].centerx -= EBACK
                    enemy.AList[j].centerx += ABACK

            for j in range(enemy.lenB):#PE hit EB
                if (player.EList[i].colliderect(enemy.BList[j])):
                    player.ELifeList[i] -= BDMG #EB causes damage
                    enemy.BLifeList[j] -= EDMG #PE causes damage
                    player.EList[i].centerx -= EBACK
                    enemy.BList[j].centerx += BBACK

            for j in range(enemy.lenC):#PE hit EC
                if (player.EList[i].colliderect(enemy.CList[j])):
                    player.ELifeList[i] -= CDMG#EC causes damage
                    enemy.CLifeList[j] -= EDMG #PE causes damage
                    player.EList[i].centerx -= EBACK
                    enemy.CList[j].centerx += CBACK

            for j in range(enemy.lenD):#PE hit ED
                if (player.EList[i].colliderect(enemy.DList[j])):
                    player.ELifeList[i] -= DDMG #ED causes damage
                    enemy.DLifeList[j] -= EDMG #PE causes damage
                    player.EList[i].centerx -= EBACK
                    enemy.DList[j].centerx += DBACK

            for j in range(enemy.lenE):#PD hit EE
                if (player.EList[i].colliderect(enemy.EList[j])):
                    player.ELifeList[i] -= EDMG #EE causes damage
                    enemy.ELifeList[j] -= EDMG #PE causes damage
                    player.EList[i].centerx -= EBACK
                    enemy.EList[j].centerx += EBACK

        pass

        #walking system (player A)
        if (player.lenA != 0):
            for i in range(player.lenA):
                player.AList[i].centerx += ASPEED

        #walking system (player B)
        if (player.lenB != 0):
            for i in range(player.lenB):
                player.BList[i].centerx += BSPEED

        #walking system (player C)
        if (player.lenC != 0):
            for i in range(player.lenC):
                player.CList[i].centerx += CSPEED

        #walking system (player D)
        if (player.lenD != 0):
            for i in range(player.lenD):
                player.DList[i].centerx += DSPEED

        #walking system (player E)
        if (player.lenE != 0):
            for i in range(player.lenE):
                player.EList[i].centerx += ESPEED

        #minion life system (player A)
        for i in range(player.lenA):
            if (player.ALifeList[i] <= 0):
                player.ALifeList.remove(player.ALifeList[i])
                player.AList.remove(player.AList[i])
                player.lenA -= 1
                break

        #minion life system (player B)
        for i in range(player.lenB):
            if (player.BLifeList[i] <= 0):
                player.BLifeList.remove(player.BLifeList[i])
                player.BList.remove(player.BList[i])
                player.lenB -= 1
                break
        #minion life system (player C)
        for i in range(player.lenC):
            if (player.CLifeList[i] <= 0):
                player.CLifeList.remove(player.CLifeList[i])
                player.CList.remove(player.CList[i])
                player.lenC -= 1
                break
        #minion life system (player D)
        for i in range(player.lenD):
            if (player.DLifeList[i] <= 0):
                player.DLifeList.remove(player.DLifeList[i])
                player.DList.remove(player.DList[i])
                player.lenD -= 1
                break
        #minion life system (player E)
        for i in range(player.lenE):
            if (player.ELifeList[i] <= 0):
                player.ELifeList.remove(player.ELifeList[i])
                player.EList.remove(player.EList[i])
                player.lenE -= 1
                break

        #minion life system (enemy A)
        for i in range(enemy.lenA):
            if (enemy.ALifeList[i] <= 0):
                enemy.ALifeList.remove(enemy.ALifeList[i])
                enemy.AList.remove(enemy.AList[i])
                enemy.lenA -= 1
                break

        #minion life system (enemy B)
        for i in range(enemy.lenB):
            if (enemy.BLifeList[i] <= 0):
                enemy.BLifeList.remove(enemy.BLifeList[i])
                enemy.BList.remove(enemy.BList[i])
                enemy.lenB -= 1
                break
        #minion life system (enemy C)
        for i in range(enemy.lenC):
            if (enemy.CLifeList[i] <= 0):
                enemy.CLifeList.remove(enemy.CLifeList[i])
                enemy.CList.remove(enemy.CList[i])
                enemy.lenC -= 1
                break
        #minion life system (enemy D)
        for i in range(enemy.lenD):
            if (enemy.DLifeList[i] <= 0):
                enemy.DLifeList.remove(enemy.DLifeList[i])
                enemy.DList.remove(enemy.DList[i])
                enemy.lenD -= 1
                break
        #minion life system (enemy E)
        for i in range(enemy.lenE):
            if (enemy.ELifeList[i] <= 0):
                enemy.ELifeList.remove(enemy.ELifeList[i])
                enemy.EList.remove(enemy.EList[i])
                enemy.lenE -= 1
                break

        #tower life system (player)
        if (player.tower1 <= 0):
            player.tower1Box.set_alpha(0)
        if (player.tower2 <= 0):
            player.tower2Box.set_alpha(0)
        if (player.tower3 <= 0):
            player.tower3Box.set_alpha(0)

        #tower life system (enemy)
        if (enemy.tower1 <= 0):
            enemy.tower1Box.set_alpha(0)
        if (enemy.tower2 <= 0):
            enemy.tower2Box.set_alpha(0)
        if (enemy.tower3 <= 0):
            enemy.tower3Box.set_alpha(0)

        #main life system (player)
        if (player.main <= 0):
            player.mainBox.set_alpha(0)


        #enemy spawn minion (choose which 100s set?)
        if (len(enemy.thelist) == 0):
            enemy.randnum = random.randint(1,8) #from 1 to 8
            #print("Set: ",enemy.randnum)
            if (enemy.randnum == 1):
                enemy.thelist += ONE
            if (enemy.randnum == 2):
                enemy.thelist += TWO
            if (enemy.randnum == 3):
                enemy.thelist += THREE
            if (enemy.randnum == 4):
                enemy.thelist += FOUR
            if (enemy.randnum == 5):
                enemy.thelist += FIVE
            if (enemy.randnum == 6):
                enemy.thelist += SIX
            if (enemy.randnum == 7):
                enemy.thelist += SEVEN
            if (enemy.randnum == 8):
                enemy.thelist += EIGHT
        #print("The List: ", enemy.thelist)

        #enemy spawn minion (enemy A)
        if (len(enemy.thelist) != 0):
            if (enemy.thelist[0] == 1):
                if (enemy.enemygold >= AGOLD+GOLDAMOUNT): 
                    enemy.MinusEnemyGold(AGOLD)
                    enemy.lenA += 1
                    RectA = SURFA.get_rect()
                    RectA.center = (enemy.mainRect.centerx,enemy.mainRect.centery)
                    enemy.AList.append(RectA)
                    enemy.ALifeList.append(ALIFE)
                    enemy.thelist.remove(enemy.thelist[0])

        #enemy spawn minion (enemy B)
        if (len(enemy.thelist) != 0):
            if (enemy.thelist[0] == 2):
                if (enemy.enemygold >= BGOLD+GOLDAMOUNT):
                    enemy.MinusEnemyGold(BGOLD)
                    enemy.lenB += 1
                    RectB = SURFB.get_rect()
                    RectB.center = (enemy.mainRect.centerx,enemy.mainRect.centery)
                    enemy.BList.append(RectB)
                    enemy.BLifeList.append(BLIFE)
                    enemy.thelist.remove(enemy.thelist[0])

        #enemy spawn minion (enemy C)
        if (len(enemy.thelist) != 0):
            if (enemy.thelist[0] == 3):
                if (enemy.enemygold >= CGOLD+GOLDAMOUNT):
                    enemy.MinusEnemyGold(CGOLD)
                    enemy.lenC += 1
                    RectC = SURFC.get_rect()
                    RectC.center = (enemy.mainRect.centerx,enemy.mainRect.centery)
                    enemy.CList.append(RectC)
                    enemy.CLifeList.append(CLIFE)
                    enemy.thelist.remove(enemy.thelist[0])

        #enemy spawn minion (enemy D)
        if (len(enemy.thelist) != 0):
            if (enemy.thelist[0] == 4):
                if (enemy.enemygold >= DGOLD+GOLDAMOUNT):
                    enemy.MinusEnemyGold(DGOLD)
                    enemy.lenD += 1
                    RectD = SURFD.get_rect()
                    RectD.center = (enemy.mainRect.centerx,enemy.mainRect.centery)
                    enemy.DList.append(RectD)
                    enemy.DLifeList.append(DLIFE)
                    enemy.thelist.remove(enemy.thelist[0])

        #enemy spawn minion (enemy E)
        if (len(enemy.thelist) != 0):
            if (enemy.thelist[0] == 5):
                if (enemy.enemygold >= EGOLD+GOLDAMOUNT):
                    enemy.MinusEnemyGold(EGOLD)
                    enemy.lenE += 1
                    RectE = SURFE.get_rect()
                    RectE.center = (enemy.mainRect.centerx,enemy.mainRect.centery)
                    enemy.EList.append(RectE)
                    enemy.ELifeList.append(ELIFE)
                    enemy.thelist.remove(enemy.thelist[0])


        #walking system (enemy A)
        if (enemy.lenA != 0):
            for i in range(enemy.lenA):
                enemy.AList[i].centerx -= ASPEED

        #walking system (enemy B)
        if (enemy.lenB != 0):
            for i in range(enemy.lenB):
                enemy.BList[i].centerx -= BSPEED

        #walking system (enemy C)
        if (enemy.lenC != 0):
            for i in range(enemy.lenC):
                enemy.CList[i].centerx -= CSPEED

        #walking system (enemy D)
        if (enemy.lenD != 0):
            for i in range(enemy.lenD):
                enemy.DList[i].centerx -= DSPEED

        #walking system (enemy E)
        if (enemy.lenE != 0):
            for i in range(enemy.lenE):
                enemy.EList[i].centerx -= ESPEED

        #end game
        if (player.main <= 0):
            return False #Lose

        if (enemy.main <= 0):
            return True #Win

        #tower life become 0
        if (player.tower1<= 0):
            player.tower1 = 0
        if (player.tower2<= 0):
            player.tower2 = 0
        if (player.tower3<= 0):
            player.tower3 = 0
        if (player.main <=0):
            player.main = 0

        if (enemy.tower1<= 0):
            enemy.tower1 = 0
        if (enemy.tower2<= 0):
            enemy.tower2 = 0
        if (enemy.tower3<= 0):
            enemy.tower3 = 0
        if (enemy.main<=0):
            enemy.main = 0

        #pause button
        PauseButton = Rect(SCREENWIDTH/2 - BUTTONWIDTH/2, 0 , BUTTONWIDTH, BUTTONHEIGHT)
        pygame.draw.rect(Display,RED,PauseButton)
        
        if (player.tower1<= 0):
            player.tower1 = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() == LEFT_CLICK):
                    if (player.playergold > 0):
                        if (player.ABox.get_alpha() == 255):
                            if (player.ARect.collidepoint(mousepos)):
                                player.MinusPlayerGold(AGOLD)
                                player.lenA += 1
                                RectA = SURFA.get_rect()
                                RectA.center = (player.mainRect.centerx,player.mainRect.centery)
                                player.AList.append(RectA)
                                player.ALifeList.append(ALIFE)

                        if (player.BBox.get_alpha() == 255):
                            if (player.BRect.collidepoint(mousepos)):
                                player.MinusPlayerGold(BGOLD)
                                player.lenB += 1
                                RectB = SURFB.get_rect()
                                RectB.center = (player.mainRect.centerx,player.mainRect.centery)
                                player.BList.append(RectB)
                                player.BLifeList.append(BLIFE)

                        if (player.CBox.get_alpha() == 255):
                            if (player.CRect.collidepoint(mousepos)):
                                player.MinusPlayerGold(CGOLD)
                                player.lenC += 1
                                RectC = SURFC.get_rect()
                                RectC.center = (player.mainRect.centerx,player.mainRect.centery)
                                player.CList.append(RectC)
                                player.CLifeList.append(CLIFE)

                        if (player.DBox.get_alpha() == 255):
                            if (player.DRect.collidepoint(mousepos)):
                                player.MinusPlayerGold(DGOLD)
                                player.lenD += 1
                                RectD = SURFD.get_rect()
                                RectD.center = (player.mainRect.centerx,player.mainRect.centery)
                                player.DList.append(RectD)
                                player.DLifeList.append(DLIFE)

                        if (player.EBox.get_alpha() == 255):
                            if (player.ERect.collidepoint(mousepos)):
                                player.MinusPlayerGold(EGOLD)
                                player.lenE += 1
                                RectE = SURFE.get_rect()
                                RectE.center = (player.mainRect.centerx,player.mainRect.centery)
                                player.EList.append(RectE)
                                player.ELifeList.append(ELIFE)

                    else: #player.playergold <= 0
                        player.playergold = 0

                    if (PauseButton.collidepoint(mousepos)):
                        if pause == False:
                            pause = True
                            pausecondition = True
                            PauseWord = SmallFont.render("Click to continue", True,WHITE)
                            PauseWordRect = PauseWord.get_rect()
                            PauseWordRect.center = PauseButton.center
                            Display.blit(PauseWord, PauseWordRect)
                            pygame.mixer.music.pause()
                            
                        else:
                            pause = False
                            pausecondition = False
                            pygame.mixer.music.unpause()

                pass

                
        #DRAW
        #show the golds
        PlayerGold = SmallerFont.render(str(player.playergold),True,WHITE)
        PlayerGoldRect = PlayerGold.get_rect()
        PlayerGoldRect.left = PlayerGoldWordRect.right
        PlayerGoldRect.centery = PlayerGoldWordRect.centery
        Display.blit(PlayerGold, PlayerGoldRect)

        EnemyGold = SmallerFont.render(str(enemy.enemygold),True,WHITE)
        EnemyGoldRect = EnemyGold.get_rect()
        EnemyGoldRect.right = EnemyGoldWordRect.left
        EnemyGoldRect.centery = EnemyGoldWordRect.centery
        Display.blit(EnemyGold, EnemyGoldRect)

        #lifes
        PlayerLife = SmallerFont.render(str(player.main*100/MAXLIFE),True,WHITE)
        PlayerLifeRect = PlayerLife.get_rect()
        PlayerLifeRect.left = PlayerLifeWordRect.right
        PlayerLifeRect.centery = PlayerLifeWordRect.centery
        Display.blit(PlayerLife, PlayerLifeRect)

        T1 = SmallerFont.render(str("{0:.2f}".format(player.tower1*100/(MAXLIFE*30/100))),True,WHITE)
        T2 = SmallerFont.render(str("{0:.2f}".format(player.tower2*100/(MAXLIFE*40/100))),True,WHITE)
        T3 = SmallerFont.render(str("{0:.2f}".format(player.tower3*100/(MAXLIFE*50/100))),True,WHITE)

        T1Rect = T1.get_rect()
        T1Rect.left = PlayerT1WordRect.right
        T1Rect.centery = PlayerT1WordRect.centery
        Display.blit(T1,T1Rect)

        T2Rect = T2.get_rect()
        T2Rect.left = PlayerT2WordRect.right
        T2Rect.centery = PlayerT2WordRect.centery
        Display.blit(T2,T2Rect)

        T3Rect = T3.get_rect()
        T3Rect.left = PlayerT3WordRect.right
        T3Rect.centery = PlayerT3WordRect.centery
        Display.blit(T3,T3Rect)

        EnemyLife = SmallerFont.render(str(enemy.main*100/MAXLIFE),True,WHITE)
        EnemyLifeRect = EnemyLife.get_rect()
        EnemyLifeRect.right = EnemyLifeWordRect.left
        EnemyLifeRect.centery = EnemyLifeWordRect.centery
        Display.blit(EnemyLife, EnemyLifeRect)

        eT1 = SmallerFont.render(str("{0:.2f}".format(enemy.tower1*100/(MAXLIFE*30/100))),True,WHITE)
        eT2 = SmallerFont.render(str("{0:.2f}".format(enemy.tower2*100/(MAXLIFE*40/100))),True,WHITE)
        eT3 = SmallerFont.render(str("{0:.2f}".format(enemy.tower3*100/(MAXLIFE*50/100))),True,WHITE)

        eT1Rect = eT1.get_rect()
        eT1Rect.right = EnemyT1WordRect.left
        eT1Rect.centery = EnemyT1WordRect.centery
        Display.blit(eT1,eT1Rect)

        eT2Rect = eT2.get_rect()
        eT2Rect.right = EnemyT2WordRect.left
        eT2Rect.centery = EnemyT2WordRect.centery
        Display.blit(eT2,eT2Rect)

        eT3Rect = eT3.get_rect()
        eT3Rect.right = EnemyT3WordRect.left
        eT3Rect.centery = EnemyT3WordRect.centery
        Display.blit(eT3,eT3Rect)

        #Player
        #pygame.draw.rect(Display,BLUE,player.FirstDefRect) #1st defence rect
        #pygame.draw.rect(Display,LIGHTBLUE,player.SecondDefRect) #2nd defence rect
        Display.blit(player.mainBox,player.mainRect)
        player.mainBox.blit(pygame.transform.flip(MAIN1,True,False),MAIN1.get_rect())

        #tower 1 animation (player)
        Display.blit(player.tower1Box,player.tower1Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(player.tower1Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower1Box.blit(TOWER1,TOWER1.get_rect())
        else:
            pygame.draw.rect(player.tower1Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower1Box.blit(TOWER2,TOWER2.get_rect())

        #tower 2 animation (player)
        Display.blit(player.tower2Box,player.tower2Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(player.tower2Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower2Box.blit(TOWER1,TOWER1.get_rect())
        else:
            pygame.draw.rect(player.tower2Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower2Box.blit(TOWER2,TOWER2.get_rect())

        #tower 3 animation (player)
        Display.blit(player.tower3Box,player.tower3Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(player.tower3Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower3Box.blit(TOWER1,TOWER1.get_rect())
        else:
            pygame.draw.rect(player.tower3Box,LIGHTBLUE,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            player.tower3Box.blit(TOWER2,TOWER2.get_rect())

        #player minions spawn
        #E animation
        for i in range(player.lenE):
            Display.blit(SURFE,player.EList[i])
            if ecount <= 1*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(E1,player.EList[i])
            elif ecount <= 2*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(E2,player.EList[i])
            elif ecount <= 3*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(E3,player.EList[i])
            else:
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(E4,player.EList[i])
        #D animation
        for i in range(player.lenD):
            Display.blit(SURFD,player.DList[i])
            if dcount <= 1*(FPS/4):
                pygame.draw.rect(SURFD,COLORD,Rect(0,0,DWIDTH,DHEIGHT))
                Display.blit(D1,player.DList[i])
            else:
                pygame.draw.rect(SURFD,COLORD,Rect(0,0,DWIDTH,DHEIGHT))
                Display.blit(D2,player.DList[i])

        #C animation
        for i in range(player.lenC):
            Display.blit(SURFC,player.CList[i])
            if ccount <= 1*(FPS/8):
                pygame.draw.rect(SURFC,COLORC,Rect(0,0,CWIDTH,CHEIGHT))
                Display.blit(C1,player.CList[i])
            else:
                pygame.draw.rect(SURFC,COLORC,Rect(0,0,CWIDTH,CHEIGHT))
                Display.blit(C2,player.CList[i])

        #B animation
        for i in range(player.lenB):
            Display.blit(SURFB,player.BList[i])
            if bcount <= 1*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B1,player.BList[i])
            elif bcount <= 2*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B2,player.BList[i])
            elif bcount <= 3*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B3,player.BList[i])
            elif bcount <= 4*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B4,player.BList[i])
            elif bcount <= 5*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(pygame.transform.flip(B5,True,False),player.BList[i])
            elif bcount <= 6*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B6,player.BList[i])
            elif bcount <= 7*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B7,player.BList[i])
            else:
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(B8,player.BList[i])

        #A animation
        for i in range(player.lenA):
            Display.blit(SURFA,player.AList[i])
            if acount <= 1*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A1,True,False),player.AList[i])
            elif acount <= 2*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A2,True,False),player.AList[i])
            elif acount <= 3*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A3,True,False),player.AList[i])
            elif acount <= 4*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A4,True,False),player.AList[i])
            elif acount <= 5*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A5,True,False),player.AList[i])
            else:
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(pygame.transform.flip(A6,True,False),player.AList[i])

        #Enemy
        #pygame.draw.rect(Display,RED,enemy.FirstDefRect) #1st defence rect
        #pygame.draw.rect(Display,LIGHTRED,enemy.SecondDefRect) #2nd defence rect
        Display.blit(enemy.mainBox,enemy.mainRect)
        enemy.mainBox.blit(eMAIN1,eMAIN1.get_rect())

        #tower 1 animation (enemy)
        Display.blit(enemy.tower1Box,enemy.tower1Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(enemy.tower1Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower1Box.blit(eTOWER1,eTOWER1.get_rect())
        else:
            pygame.draw.rect(enemy.tower1Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower1Box.blit(eTOWER2,eTOWER2.get_rect())

        #tower 2 animation (enemy)
        Display.blit(enemy.tower2Box,enemy.tower2Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(enemy.tower2Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower2Box.blit(eTOWER1,eTOWER1.get_rect())
        else:
            pygame.draw.rect(enemy.tower2Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower2Box.blit(eTOWER2,eTOWER2.get_rect())

        #tower 3 animation (enemy)
        Display.blit(enemy.tower3Box,enemy.tower3Rect)
        if towercount <= 1*(FPS/4):
            pygame.draw.rect(enemy.tower3Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower3Box.blit(eTOWER1,eTOWER1.get_rect())
        else:
            pygame.draw.rect(enemy.tower3Box,LIGHTRED,Rect(0,0,TOWERBOXWIDTH,TOWERBOXHEIGHT))
            enemy.tower3Box.blit(eTOWER2,eTOWER2.get_rect())

        #enemy minions spawn
        #E animation
        for i in range(enemy.lenE):
            Display.blit(SURFE,enemy.EList[i])
            if ecount <= 1*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(eE1,enemy.EList[i])
            elif ecount <= 2*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(eE2,enemy.EList[i])
            elif ecount <= 3*(FPS/8):
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(eE3,enemy.EList[i])
            else:
                pygame.draw.rect(SURFE,COLORE,Rect(0,0,EWIDTH,EHEIGHT))
                Display.blit(eE4,enemy.EList[i])
                
        #D animation
        for i in range(enemy.lenD):
            Display.blit(SURFD,enemy.DList[i])
            if dcount <= 1*(FPS/4):
                pygame.draw.rect(SURFD,COLORD,Rect(0,0,DWIDTH,DHEIGHT))
                Display.blit(eD1,enemy.DList[i])
            else:
                pygame.draw.rect(SURFD,COLORD,Rect(0,0,DWIDTH,DHEIGHT))
                Display.blit(eD2,enemy.DList[i])

        #C animation
        for i in range(enemy.lenC):
            Display.blit(SURFC,enemy.CList[i])
            if ccount <= 1*(FPS/8):
                pygame.draw.rect(SURFC,COLORC,Rect(0,0,CWIDTH,CHEIGHT))
                Display.blit(pygame.transform.flip(eC1,True,False),enemy.CList[i])
            else:
                pygame.draw.rect(SURFC,COLORC,Rect(0,0,CWIDTH,CHEIGHT))
                Display.blit(pygame.transform.flip(eC2,True,False),enemy.CList[i])
            
        #B animation
        for i in range(enemy.lenB):
            Display.blit(SURFB,enemy.BList[i])
            if bcount <= 1*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB1,enemy.BList[i])
            elif bcount <= 2*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB2,enemy.BList[i])
            elif bcount <= 3*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB3,enemy.BList[i])
            elif bcount <= 4*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB4,enemy.BList[i])
            elif bcount <= 5*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB5,enemy.BList[i])
            elif bcount <= 6*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB6,enemy.BList[i])
            elif bcount <= 7*(FPS/8):
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB7,enemy.BList[i])
            else:
                pygame.draw.rect(SURFB,COLORB,Rect(0,0,BWIDTH,BHEIGHT))
                Display.blit(eB8,enemy.BList[i])

        #A animation
        for i in range(enemy.lenA):
            Display.blit(SURFA,enemy.AList[i])
            if acount <= 1*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA1,enemy.AList[i])
            elif acount <= 2*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA2,enemy.AList[i])
            elif acount <= 3*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA3,enemy.AList[i])
            elif acount <= 4*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA4,enemy.AList[i])
            elif acount <= 5*(FPS/6):
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA5,enemy.AList[i])
            else:
                pygame.draw.rect(SURFA,COLORA,Rect(0,0,AWIDTH,AHEIGHT))
                Display.blit(eA6,enemy.AList[i])
        

        #Choose Minions Box
        Display.blit(player.ABox,player.ARect)
        player.ABox.blit(pygame.transform.scale(pygame.transform.flip(A6,True,False),(MINIONBOXWIDTH-10,MINIONBOXHEIGHT)),Rect(5,0,MINIONBOXWIDTH,MINIONBOXHEIGHT))
        Display.blit(player.BBox,player.BRect)
        player.BBox.blit(pygame.transform.scale(B3,(MINIONBOXWIDTH,MINIONBOXHEIGHT)),Rect(0,0,MINIONBOXWIDTH,MINIONBOXHEIGHT))
        Display.blit(player.CBox,player.CRect)
        player.CBox.blit(pygame.transform.scale(C1,(MINIONBOXWIDTH,MINIONBOXHEIGHT)),Rect(0,0,MINIONBOXWIDTH,MINIONBOXHEIGHT))
        Display.blit(player.DBox,player.DRect)
        player.DBox.blit(pygame.transform.scale(D1,(MINIONBOXWIDTH,MINIONBOXHEIGHT)),Rect(0,0,MINIONBOXWIDTH,MINIONBOXHEIGHT))
        Display.blit(player.EBox,player.ERect)
        player.EBox.blit(pygame.transform.scale(E2,(MINIONBOXWIDTH-20,MINIONBOXHEIGHT)),Rect(10,0,MINIONBOXWIDTH,MINIONBOXHEIGHT))

        #Time
        Time = SmallFont.render(str("Time: "+str(TheTime)+" s"),True,WHITE)
        TimeRect = Time.get_rect()
        TimeRect.centerx = SCREENWIDTH/2
        TimeRect.top = PauseButton.bottom
        Display.blit(Time,TimeRect)

        #Display paused word
        if pause:
            while pausecondition:
                Start = time.time()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_BACKSPACE:
                            pygame.quit()
                            sys.exit()
                    elif event.type == MOUSEBUTTONDOWN:
                        if (pygame.mouse.get_pressed() == LEFT_CLICK):
                            if (PauseButton.collidepoint(mousepos)):
                                pause = False
                                pausecondition = False
                                pygame.mixer.music.unpause()
                pygame.display.update()
        else:
            PauseWord = SmallFont.render("Click to pause", True,WHITE)
            PauseWordRect = PauseWord.get_rect()
            PauseWordRect.center = PauseButton.center
            Display.blit(PauseWord, PauseWordRect)

                
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def Game():
    pygame.mixer.init()
    pygame.mixer.music.load("./music/Come and Find Me - B mix.mp3")
    pygame.mixer.music.play(-1,0.0)
    startscreen()
    pygame.mixer.music.stop()
    if(endscreen(main())):
        return Game()
    else:
        pygame.quit()
        sys.exit()


Game()
