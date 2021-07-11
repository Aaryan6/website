import pygame
import sys
import math
from moviepy.editor import *

pygame.init()
pygame.mixer.init()


# value
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsclock = pygame.time.Clock()
fps = 50

# color
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)


def welcome():
    intro = pygame.image.load('intro.gif').convert()
    intro = pygame.transform.scale(intro, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameOn()
        SCREEN.blit(intro, (0, 0))
        pygame.display.update()
        fpsclock.tick(fps)

def gameOn():

    # player
    player_x = SCREEN_WIDTH/2
    player_y = SCREEN_HEIGHT - 100
    player_move_x = 0

    # enemy
    enemy_x = SCREEN_WIDTH / 2
    enemy_y = 20
    enemy_move_x = 2

    # player laser
    player_laser_x = player_x+10
    player_laser_y = player_y
    player_laser_vel = 0

    # enemy laser
    enemy_laser_x = SCREEN_WIDTH/2
    enemy_laser_y = 50
    enemy_laser_vel = 0

    # images
    player = pygame.image.load('player.png')
    player = pygame.transform.scale(player, (50, 80)).convert_alpha()

    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy = pygame.transform.rotate(pygame.transform.scale(enemy, (50, 80)).convert_alpha(), 180)

    player_laser = pygame.image.load('bullet.png').convert_alpha()
    player_laser = pygame.transform.rotate(pygame.transform.scale(player_laser, (28, 39)).convert_alpha(), -90)

    enemy_laser = pygame.image.load('bullet.png').convert_alpha()
    enemy_laser = pygame.transform.rotate(pygame.transform.scale(enemy_laser, (30, 40)).convert_alpha(), 90)

    back = pygame.image.load('space.jpg').convert()

    run = True
    gameOver = False
    iswin = False

    over = pygame.image.load('game_over.jpg')
    over = pygame.transform.scale(over, (SCREEN_WIDTH, SCREEN_HEIGHT))

    win = pygame.image.load('win.png')
    win = pygame.transform.scale(win, (SCREEN_WIDTH, SCREEN_HEIGHT))

    bim = pygame.mixer.Sound('lazer.mp3')

    def player_f(x, y):
        SCREEN.blit(player, [x, y])

    def player_laser_f(x, y):
        SCREEN.blit(player_laser, [x, y])

    def enemy_f(x, y):
        SCREEN.blit(enemy, [x, y])

    def enemy_laser_f(x, y):
        SCREEN.blit(enemy_laser, [x, y])


    while run:

        if gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            SCREEN.blit(over, (0, 0))
            pygame.display.update()

        elif iswin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            SCREEN.blit(win, (0, 0))
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    # player move
                    if event.key == pygame.K_LEFT:
                        player_move_x = 2

                    if event.key == pygame.K_RIGHT:
                        player_move_x = -2

                    if event.key == pygame.K_SPACE:
                        bim.play()
                        player_laser_vel = 4

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player_move_x = 0

            # player move
            player_x -= player_move_x
            if player_x > SCREEN_WIDTH - 70 or player_x < 30:
                player_move_x = 0

            # player laser
            if player_laser_y >= player_y:
                player_laser_x -= player_move_x

            player_laser_y -= player_laser_vel
            if player_laser_y < 20:
                player_laser_vel = 0
                player_laser_x = player_x+10
                player_laser_y = player_y

            # enemy
            enemy_x -= enemy_move_x
            if enemy_x <= 20:
                enemy_move_x = -3
            elif enemy_x >= SCREEN_WIDTH-70:
                enemy_move_x = 3

            # enemy laser
            enemy_laser_y += enemy_laser_vel
            if enemy_laser_y >= SCREEN_HEIGHT -20:
                enemy_laser_vel = 0
                enemy_laser_x = enemy_x+3
                enemy_laser_y = 60
            else:
                enemy_laser_vel = 5

            distance_w = math.sqrt((math.pow(enemy_x - player_laser_x, 2)) + (math.pow(enemy_y - player_laser_y, 2)))
            if distance_w < 33:
                iswin = True
            distance_l = math.sqrt((math.pow(player_x - enemy_laser_x, 2) + (math.pow(player_y - enemy_laser_y, 2))))
            if distance_l < 31:
                gameOver = True
                bim.stop()
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play()

            SCREEN.blit(back, (0, 0))
            player_laser_f(player_laser_x, player_laser_y)
            enemy_laser_f(enemy_laser_x, enemy_laser_y)
            player_f(player_x, player_y)
            enemy_f(enemy_x, enemy_y)
            fpsclock.tick(fps)
            pygame.display.update()

welcome()