import pygame
import random
import os
import sys

pygame.init()

pygame.mixer.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 600
screen_height = 350

clock = pygame.time.Clock()


# display window
game_window = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load("back.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

intro = pygame.image.load("intro.jpg")
intro = pygame.transform.scale(intro, (screen_width, screen_height)).convert_alpha()

over = pygame.image.load("game_over.jpg")
over = pygame.transform.scale(over, (screen_width, screen_height)).convert_alpha()

snake = pygame.image.load("snake.png")
snake = pygame.transform.scale(snake, (100, 100)).convert_alpha()



pygame.display.set_caption("Snake Nikel")
pygame.display.update()

font = pygame.font.SysFont("tahoma", 16)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])


def plot(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        # image
        game_window.blit(intro, (0, 0))
        game_window.blit(snake, (450, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("back_music.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    game_loop()
        pygame.display.update()
        clock.tick(50)


def game_loop():
    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")
    with open("high_score.txt", "r") as f:
        high_score = f.read()

    snk_list = []
    snk_lenght = 1

    snake_x = 50
    snake_y = 50
    snake_size = 13
    # food
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)

    valocity_x = 0
    valocity_y = 0
    init_valo = 4
    # score
    score = 0

    fps = 50

    game_over = False
    exit_game = False

    while not exit_game:

        if game_over:

            game_window.blit(over, (0, 0))
            # score
            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            text_screen("Your Score : " + str(score), white, 10, 8)
            text_screen("High Score : " + str(high_score), white, 480, 8)
            text_screen("PRESS ENTER TO CONTINUE", white, 200, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        valocity_x = init_valo
                        valocity_y = 0
                    if event.key == pygame.K_LEFT:
                        valocity_x = -init_valo
                        valocity_y = 0
                    if event.key == pygame.K_UP:
                        valocity_y = -init_valo
                        valocity_x = 0
                    if event.key == pygame.K_DOWN:
                        valocity_y = init_valo
                        valocity_x = 0

            snake_x += valocity_x
            snake_y += valocity_y

            # eat
            if abs(snake_x - food_x) < 9 and abs(snake_y - food_y) < 9:
                eat = pygame.mixer.Sound("eat.mp3")
                eat.set_volume(0.7)
                eat.play()
                score += 5
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                snk_lenght += 3
                if score > int(high_score):
                    high_score = score

            game_window.blit(bgimg, (0, 0))
            text_screen("Score : " + str(score), white, 8, 8)
            apple = pygame.image.load("apple.png")
            apple = pygame.transform.scale(apple, (15, 15)).convert_alpha()
            game_window.blit(apple, [food_x, food_y])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 2 or snake_x > screen_width-2 or snake_y < 2 or snake_y > screen_height-2:
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
                game_over = True

            plot(game_window, white, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()