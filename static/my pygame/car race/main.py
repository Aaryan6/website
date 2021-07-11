import pygame, sys, random, os

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH =318
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def welcome():
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            Gameloop()
        intro = pygame.image.load('intro.png').convert()
        SCREEN.blit(intro, [0, 0])
        pygame.display.update()

def Gameloop():

    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    class Game:
        def __init__(self):
            self.run = True
            self.road = pygame.image.load('road2.png').convert()
            self.road_y = -500
            self.road_h = self.road.get_height()
            self.i = 0
            # player car
            self.car_x = 100
            self.car_y = 430
            # enemy car
            self.obj_car_x = 100
            self.obj_car_y = -150
            # enemy car 2
            self.obj_car_x2 = 150
            self.obj_car_y2 = -300
            # score
            self.score = 0
            self.speed = 10

        def background(self):
            if self.i == 500:
                self.i = 0
            SCREEN.blit(self.road, (0, self.road_y + self.i))
            self.i += 5

        def car(self):
            # self.my_car = pygame.draw.rect(SCREEN, (255, 255, 255), [self.car_x, self.car_y, 30, 40])
            self.my_car_image = pygame.image.load('player.png').convert_alpha()
            self.my_car_image = pygame.transform.scale(self.my_car_image, [30, 50])
            self.rect = SCREEN.blit(self.my_car_image, [self.car_x, self.car_y])

        def car_move(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT] and self.car_x < 205:
                self.car_x += 5
            elif keys[pygame.K_LEFT] and self.car_x > 85:
                self.car_x -= 5
            elif keys[pygame.K_UP] and self.car_y > 20:
                self.car_y -= 5
            elif keys[pygame.K_DOWN] and self.car_y < 450:
                self.car_y += 5

        def obj_car(self):
            self.enemy_car_image = pygame.image.load('enemy.png')
            self.enemy_car_image = pygame.transform.rotate(pygame.transform.scale(self.enemy_car_image, [30, 50]), 180).convert_alpha()
            self.enemy_car = SCREEN.blit(self.enemy_car_image, [self.obj_car_x, self.obj_car_y])
            self.obj_car_y += self.speed
            if self.obj_car_y > 600:
                self.obj_car_x = random.randint(85, 205)
                self.obj_car_y = -150

        def obj_car2(self):
            self.enemy_car_image2 = pygame.image.load('enemy.png')
            self.enemy_car_image2 = pygame.transform.rotate(pygame.transform.scale(self.enemy_car_image2, [30, 50]), 180).convert_alpha()
            self.enemy_car2 = SCREEN.blit(self.enemy_car_image2, [self.obj_car_x2, self.obj_car_y2])
            self.obj_car_y2 += self.speed
            if self.obj_car_y2 > 700:
                self.obj_car_x2 = random.randint(85, 205)
                self.obj_car_y2 = -300

        def write_score(self):

            self.font = pygame.font.SysFont("imapct", 25)

            def text_screen(text, color, x, y):
                screen_text = self.font.render(text, True, color)
                SCREEN.blit(screen_text, [x, y])

            with open("high_score.txt", "r") as f:
                self.high_score = f.read()

            self.score += 0.05
            if self.score > int(self.high_score):
                self.high_score = self.score

            with open("high_score.txt", "w") as f:
                f.write(str(int(self.high_score)))

            text_screen(str(int(self.score)), (20, 20, 20), 10, 10)


    gm = Game()
    exit_game = False
    gameover = False

    while not exit_game:

        if gameover:
            over = pygame.image.load('over.png').convert()
            SCREEN.blit(over, [0, 0])

            font = pygame.font.SysFont("impact", 18, False)
            def text_screen(text, color, x, y):
                screen_text = font.render(text, True, color)
                SCREEN.blit(screen_text, [x, y])

            text_screen("High Score : " + str(int(gm.high_score)), (255, 255, 255), 200, 20)
            text_screen("Your Score : " + str(int(gm.score)), (255, 255, 255), 15, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    pygame.quit()
                    sys.exit()

            gm.background()
            gm.obj_car()
            gm.obj_car2()
            gm.car()
            gm.car_move()
            if gm.rect.colliderect(gm.enemy_car) or gm.rect.colliderect(gm.enemy_car2):
                gameover = True
                boom = pygame.mixer.Sound('boom.wav')
                boom.play()
            gm.write_score()
            pygame.display.update()
            clock.tick(70)

welcome()