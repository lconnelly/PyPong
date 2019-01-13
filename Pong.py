#two players: one humna, one computer
#each player hasa bar, and player mvoes the bar to bound ball
#this is  a native implemenatation that doesn't handle collision
## final project:
#add 3 things
#when either of the player gets 10 points, the game quit.
#and then display player won" or "computer won"
#when the point differentec ebtween two players is with 1,
#increase the ball speed
#when the player scores 3 times in a row
#increase the height of thebar
#reduce the bar to normal size after the player loses

#feel free to change anything in the game
#as long as your subission contains the features above




import pygame
import random
from pygame.locals import *
from time import sleep
from sys import exit


pygame.init()

WIN_CONDITION = 10

#set the size of the display winow
screen = pygame.display.set_mode((640, 480),0 ,0) #flag settings
#set the caption of the display window
pygame.display.set_caption("Pong Game")

#graphics on the window
#background,

# the bars, the ball
#1. surface -> size
#2. Conert()
#3. fill with given color
#background
back = pygame.Surface((640, 480))
background = back.convert()
background.fill((100, 100, 100)) #RGB 0 - 255

#the ball
ball_surface = pygame.Surface((15, 15))
#draw a circle with the ball surface
circle= pygame.draw.circle(ball_surface, (0, 255, 0),
                           (int(15/2), int(15/2)), int(15/2))

ball = ball_surface.convert()
ball.set_colorkey((0, 0 , 0))



#variables
#position of the bars
#position of the ball
#bar moving speed
#ball moving spped
# player scores,
bar1_x = 10.0 #floats
bar1_y = 215.0

bar2_x = 620.0
bar2_y = 215.0

ball_x = 307.5
ball_y  = 232.5

bar1_move = 0
bar2_move = 0
bar1_streak = 0
bar2_streak = 0

x_speed = 200.0 #both players have the same speed
y_speed = 200.0
ball_speed = 200.0
original_ball_speed = ball_speed

bar1_score = 0
bar2_score = 0


#timw/clock
clock = pygame.time.Clock()
font = pygame.font.SysFont("NeuzeitGro", 12)

#font of all the words on the display window

#actual game play

while True:

    #player needs to move keyboard
    #in programming called events
    # the bars
    bar1_surface = pygame.Surface((10, 50*(3 if bar1_streak >= 3 else 1)))
    bar1 = bar1_surface.convert()
    bar1.fill((200, 200, 100))

    bar2_surface = pygame.Surface((10, 50*(3 if bar2_streak >= 3 else 1)))
    bar2 = bar2_surface.convert()
    bar2.fill((100, 150, 200))

    for event in pygame.event.get():
        #quit
        #up key is to move up
        #down key is to move down
        #left key is to move left
        #right key is to move right
        #add extra player
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -bar_speed
            elif event.key == K_DOWN:
                bar1_move = bar_speed

        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0
            elif event.key == K_DOWN:
                bar1_move = 0

    #dispaly scores and all those htings
    score1 = font.render(str(bar1_score), True, (255, 255, 255))
    score2 = font.render(str(bar2_score), True, (255, 255, 255))

    screen.blit(background, (0, 0)) #if you want to draw image onto another
    #middle line
    frame = pygame.draw.rect(screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    middle_line= pygame.draw.aaline(screen, (255, 255, 255), (330, 5), (330, 475))

    #blit all thes tuff onto the screen
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(score1, (200, 200))
    screen.blit(score2, (400, 200))


    #how does human player bar move

    bar1_y = bar1_y + bar1_move #old local by amount moved impacted by keyboard

    #how does the ball move?
    #how can we c alaculate the travel distance of an object
    #time x volicity
    #calc time
    #calc the distance by doig  time * ball speed

    time_passed = clock.tick(30)
    time_sec  =time_passed / 1000 #calc time in seconds

    ball_x = ball_x + time_sec*x_speed * (1.33 if abs(bar1_score - bar2_score) <= 1 else 1) #similer to ternary
    ball_y = ball_y + time_sec*y_speed * (1.33 if abs(bar1_score - bar2_score) <= 1 else 1)
    bar_speed = ball_speed*time_sec

    #how tod o AI for the computer?

    #1. a bar cannot go otuside the screen
    #called clamp in computer graphics

    #how do we actually move stuff?
    #if the bal lands on the bar
    #gthe ball chagnes direction and boundes
    #if the ball lands outside of the bar
    #how to move
    #thesea re hard coded numbers, there should be a better to write

    if ball_x >= 305:
        if not bar2_y == ball_y + 7.5*(3 if bar2_streak >= 3 else 1): #as long asi it is not this
            if bar2_y < ball_y + 7.5*(3 if bar2_streak >= 3 else 1):
                bar2_y = bar2_y + bar_speed
            if bar2_y > ball_y - 42.5*(3 if bar2_streak >= 3 else 1):
                bar2_y = bar2_y + - bar_speed
        else:
            bar2_y = ball_y + 7.5



    #cant go out of screen
    if bar1_y >= 420 and bar1_streak < 3:
        bar1_y = 420
    elif bar1_y >= 320 and bar1_streak >= 3:
        bar1_y = 320
    elif bar1_y <= 10:
        bar1_y = 10

    if bar2_y >= 420:
        bar2_y = 420
    elif bar2_y <= 10:
        bar2_y  = 10


#How to actually move stuff

    if ball_x <= bar1_x + 10:
        if ball_y >= bar1_y - 7.5*(3 if bar1_streak >= 3 else 1) and ball_y <= bar1_y + 42.5*(3 if bar1_streak >= 3 else 1):
            ball_x  = 20
            x_speed = -x_speed

    if ball_x >= bar2_x -15:
        if ball_y >= bar2_y -7.5*(3 if bar2_streak >= 3 else 1) and ball_y <= bar2_y +42.5*(3 if bar2_streak >= 3 else 1):
            ball_x = 605
            x_speed = -x_speed


#missing the bar

    if ball_x< 5:
        bar2_score = bar2_score +1
        if bar2_score == WIN_CONDITION:
            break;
        bar2_streak += 1
        bar1_streak = 0

        ball_x = 320
        ball_y = 232.5

        bar1_y = 215
        bar2_y = 215

    elif ball_x > 620:
        bar1_score = bar1_score +1
        if bar1_score == WIN_CONDITION:
            break;
        bar1_streak += 1
        bar2_streak = 0
        ball_x = 307.5
        ball_y = 232.5

        bar1_y = 215
        bar2_y = 215


#change direction of teh ball
    #this not the best do this. Prper way should be collison

    if ball_y <= 10:
        y_speed = -y_speed
        ball_y = 11
    elif ball_y >= 456.5:
        y_speed = -y_speed
        ball_y = 455.5


    pygame.display.update()

while True:
    for event in pygame.event.get():
        #quit
        if event.type == QUIT:
            exit()
    winMessage = {}
    if bar1_score == WIN_CONDITION:
        P1W = "Player wins!"
        winMessage = font.render(str(P1W), True, (255, 255, 255))
        screen.blit(winMessage, (200, 150))

    elif bar2_score == WIN_CONDITION:
        C1W=  "Computer wins!"
        winMessage = font.render(str(C1W), True, (255, 255, 255))
        screen.blit(winMessage, (400, 150))

    pygame.display.update()


