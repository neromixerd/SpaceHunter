import pygame
import sys
import random
import string
from threading import Timer
from operator import attrgetter

import Objects

FPS = 60
i = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKBLUE = (0, 0, 139)
DARKRED = (176, 16, 48)
myshoot_flag = 0
Enemy1_come = [-1, -160, -400]
Enemy1_reload = [-1, -1, -1]
My_Score = 0
enemy1_shootdelay = 40
enemy1_comedelay = 300
meteor_flag = -1
meteor_comedelay = 120
GO_time = -160
My_Hitpoints = 300
Enemy_Hitpoints = 100
Start_flag = 0
Write_flag = 0
Print_flag = 0
Rating_flag = 0
RatingSpace = [0, 0, 0, 0, 0, 0, 0, 0]
Rait = [0, 0, 0, 0, 0, 0, 0, 0]
My_Name = 'Player_1'


def comedelay(time, delay):
    timer = time
    if timer == -1:
        timer += 1
        return timer
    elif timer < delay:
        timer += 1
        return timer
    elif timer >= delay:
        timer = -1
        return timer


def rand():
    x = random.randint(30, 370)
    y = random.randint(60, 200)
    return x, y


def score_update(enemy1, enemy2, enemy3, score):
    score += enemy1
    score += enemy2
    score += enemy3
    return score


def retry():
    fenemy.rect.x = -50; fenemy.rect.y = -50; fenemy.status = 0
    senemy.rect.x = -50; senemy.rect.y = -50; senemy.status = 0
    thenemy.rect.x = -50; thenemy.rect.y = -50; thenemy.status = 0
    fenemy.hitpoints = Enemy_Hitpoints; senemy.hitpoints = Enemy_Hitpoints
    thenemy.hitpoints = Enemy_Hitpoints
    myShip.rect.x = 200; myShip.rect.y = 450
    myShip.old_rect[0] = 0; myShip.old_rect[1] = 0
    myShip.hitpoints = My_Hitpoints; myShip.count = -1; myShip.Bcount = -1
    meteors.empty()
    MyShoots.empty()
    EnemyShoots.empty()
    Score = 0
    return Score


pygame.init()
pygame.display.set_caption("Space Hunter")

table = pygame.display.set_mode((400, 600))
table_rect = table.get_rect()
movespace = pygame.Surface((400, 600))
scorespace = pygame.Surface((400, 74))
overspace = pygame.Surface((315, 156))
button_retry = pygame.Surface((216, 65))
retry_rect = button_retry.get_rect()

Scorespace = pygame.image.load(r"Images\Scorespace.png")
scorespace.blit(Scorespace, (0, 0))
Movespace = pygame.image.load(r"Images\Movespace.png")
movespace.blit(Movespace, (0, 0))
Overspace = pygame.image.load(r"Images\RetrySpace1.jpg")
overspace.blit(Overspace, (0, 0))
RetryButton = pygame.image.load(r"Images\RetryButton.png")
button_retry.blit(RetryButton, (0, 0))
Menu = pygame.image.load(r"Images\MenuSpace.png")

movespace.set_alpha(120)
scorespace.set_alpha(120)
overspace.set_alpha(250)

meteors = pygame.sprite.Group()
MyShoots = pygame.sprite.Group()
myShips = pygame.sprite.Group()
EnemyShoots = pygame.sprite.Group()
Enemies01 = pygame.sprite.Group()
Enemies02 = pygame.sprite.Group()
Enemies03 = pygame.sprite.Group()

myShip = Objects.MyShip(table, 200, 450, myShips, My_Hitpoints)
fenemy = Objects.Enemy1(table, -50, -50, Enemy_Hitpoints, Enemies01, 0)
senemy = Objects.Enemy1(table, -50, -50, Enemy_Hitpoints, Enemies02, 0)
thenemy = Objects.Enemy1(table, -50, -50, Enemy_Hitpoints, Enemies03, 0)

Fount1 = pygame.font.SysFont('verdana', 35)
Fount2 = pygame.font.SysFont('verdana', 20)
NameText = pygame.font.SysFont('verdana', 25)
RatingFount = pygame.font.SysFont('verdana', 18)
Over = Fount1.render('Game Over', 1, DARKRED)
Retry = Fount2.render('Retry?', 1, DARKRED)
Back_menu = Fount1.render('Menu', 1, DARKRED)
Back_rect = Back_menu.get_rect()
Back_rect.x = 290; Back_rect.y = 18

Game_over = pygame.USEREVENT + 1
Game_start = pygame.USEREVENT + 2
Event_GO = pygame.event.Event(Game_over)
Event_GS = pygame.event.Event(Game_start)

table.blit(movespace, (0, 0))
clock = pygame.time.Clock()
pygame.display.update()
print(pygame.font.get_fonts())

while 1:
    clock.tick(FPS)
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    while Start_flag == 0:
        #clock.tick(FPS)
        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        events = pygame.event.get()

        MenuButton1 = Objects.Menu_Button(table, (250, 100))
        Start = Fount1.render("Start", 1, BLACK)
        MenuButton1.iso.blit(Start, (40, 8))

        MenuButton2 = Objects.Menu_Button(table, (220, 200))
        Results = Fount1.render("Rating", 1, BLACK)
        MenuButton2.iso.blit(Results, (40, 8))

        MenuButton3 = Objects.Menu_Button(table, (280, 350))
        Exit = Fount1.render("Exit", 1, BLACK)
        MenuButton3.iso.blit(Exit, (40, 8))

        Name = pygame.image.load(r"Images\Name.png")
        Name_rect = Name.get_rect()
        Name_rect.x = 20; Name_rect.y = 20
        Name_tex = NameText.render(My_Name, 1, DARKRED)
        Name.blit(Name_tex, (15, 15))

        if pressed[0] and MenuButton1.rect.collidepoint(pos):
            Start_flag = 1
        elif pressed[0] and MenuButton2.rect.collidepoint(pos):
            Rating_flag = 1
            while Rating_flag == 1:
                pressed = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                events = pygame.event.get()
                WriteList = []
                rating = open('Rating.txt', 'r')
                list = [line.strip() for line in rating]

                for i in range(len(list)):
                    sol = list[i].split(' ')
                    WriteList += [[sol[0], sol[1] + ' ' + sol[2]]]

                for i in range(len(WriteList)):
                    WriteList[i] = Objects.Rating(int(WriteList[i][0]), WriteList[i][1])

                RaitList = sorted(WriteList, key=attrgetter('score'), reverse=True)

                Rating_back = Objects.Menu_Button(table, (250, 50))
                Back_rait = Fount1.render("Back", 1, BLACK)
                Rating_back.iso.blit(Back_rait, (40, 8))

                for i in range(len(RatingSpace)):
                    RatingSpace[i] = Objects.Rating_Space(table, (-80 + 15 * i+1, 30 + 60 * i+1))
                    Rating = str(RaitList[i].score) + ' ' + RaitList[i].name
                    Rait[i] = RatingFount.render(Rating, 1, DARKRED)

                table.blit(Menu, (0, 0))
                for i in range(len(RatingSpace)):
                    RatingSpace[i].iso.blit(Rait[i], (80 - 11 * i+1, 20))
                    table.blit(RatingSpace[i].iso, RatingSpace[i].rect)

                table.blit(Rating_back.iso, Rating_back.rect)

                for event in events:
                    if event.type == pygame.QUIT:
                        exit()

                if pressed[0] and Rating_back.rect.collidepoint(pos):
                    Rating_flag = 0

                pygame.display.update()
        elif pressed[0] and MenuButton3.rect.collidepoint(pos):
            exit()
        elif pressed[0] and Name_rect.collidepoint(pos):
            Print_flag = 1

        for event in events:
            if event.type == pygame.KEYDOWN and Print_flag == 1:
                if event.key == pygame.K_RETURN:
                    Print_flag = 0
                    print(My_Name)
                elif event.key == pygame.K_BACKSPACE:
                    My_Name = My_Name[:-1]
                elif event.key == pygame.K_SPACE:
                    My_Name += '_'
                else:
                    My_Name += event.unicode
            elif event.type == pygame.QUIT:
                exit()

        table.blit(Menu, (0, 0))
        table.blit(MenuButton1.iso, MenuButton1.rect)
        table.blit(MenuButton2.iso, MenuButton2.rect)
        table.blit(MenuButton3.iso, MenuButton3.rect)
        table.blit(Name, Name_rect)
        pygame.display.update()

    if not table_rect.contains(myShip.rect):
        GO_time += 1
        if GO_time >= 0:
            pygame.event.post(Event_GO)

    My_Score = score_update(fenemy.score, senemy.score, thenemy.score, My_Score)
    Score = Fount1.render('Score: ' + str(My_Score), 1, DARKRED)

    Enemy1_come[0] = comedelay(Enemy1_come[0], enemy1_comedelay)
    if Enemy1_come[0] == 0 and fenemy.status == 0:
        fenemy.recteate(0, 80, Enemy_Hitpoints, 1, Enemies01)

    Enemy1_come[1] = comedelay(Enemy1_come[1], enemy1_comedelay)
    if Enemy1_come[1] == 0 and senemy.status == 0:
        senemy.recteate(0, 160, Enemy_Hitpoints, 1, Enemies02)

    Enemy1_come[2] = comedelay(Enemy1_come[2], enemy1_comedelay)
    if Enemy1_come[2] == 0 and thenemy.status == 0:
        thenemy.recteate(0, 240, Enemy_Hitpoints, 1, Enemies03)

    if fenemy.status != 0:
        Enemy1_reload[0] = comedelay(Enemy1_reload[0], enemy1_shootdelay)
        if Enemy1_reload[0] == 0:
            Objects.Shoot2(table, fenemy.rect.midbottom, EnemyShoots)
    if senemy.status != 0:
        Enemy1_reload[1] = comedelay(Enemy1_reload[1], enemy1_shootdelay)
        if Enemy1_reload[1] == 0:
            Objects.Shoot2(table, senemy.rect.midbottom, EnemyShoots)
    if thenemy.status != 0:
        Enemy1_reload[2] = comedelay(Enemy1_reload[2], enemy1_shootdelay)
        if Enemy1_reload[2] == 0:
            Objects.Shoot2(table, thenemy.rect.midbottom, EnemyShoots)

    meteor_flag = comedelay(meteor_flag, meteor_comedelay)
    if meteor_flag == 0:
        meteoCoord = rand()
        Objects.meteor(table, meteoCoord[0], meteoCoord[1], meteors)

    if pressed[0] and myshoot_flag == 0:
        Objects.Shoot1(table, myShip.rect.x + 14, myShip.rect.y - 7, MyShoots)
        myshoot_flag += 1
    if (myshoot_flag >= 0) and (myshoot_flag < 20):
        myshoot_flag += 1
    else:
        myshoot_flag = 0

    table.blit(movespace, (0, 0))
    table.blit(scorespace, (0, 0))
    meteors.update(MyShoots, meteors)
    EnemyShoots.update()
    fenemy.update(MyShoots, Enemies01)
    senemy.update(MyShoots, Enemies02)
    thenemy.update(MyShoots, Enemies03)
    MyShoots.update()
    myShip.update(myShips, meteors, EnemyShoots)
    table.blit(Score, (30, 20))
    table.blit(Back_menu, Back_rect)

    if pressed[0] and Back_rect.collidepoint(pos):
        Enemy1_come = [-1, -160, -400]
        My_Score = retry()
        Start_flag = 0

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == Game_over:
            overspace.blit(Over, (60, 10))
            button_retry.blit(Retry, (77, 25))
            retry_rect.x = 95
            retry_rect.y = 305
            table.blit(overspace, (45, 250))
            table.blit(button_retry, retry_rect)
            if Write_flag == 0:
                rating = open('Rating.txt', 'a')
                if My_Name == '':
                    My_Name = 'Player'
                rating.write(str(My_Score) + ' - ' + My_Name + '\n')
                rating.close()
                Write_flag = 1
            if pressed[0] and retry_rect.collidepoint(pos):
                Enemy1_come = [-1, -160, -400]
                Write_flag = 0
                My_Score = retry()

    pygame.display.update()

