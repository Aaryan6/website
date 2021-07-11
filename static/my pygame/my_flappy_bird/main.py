import pygame, sys, random

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gamestop = True

def welcome():
    global gamestop, run
    while gamestop:
        intro_img = pygame.image.load('intro.png').convert()
        SCREEN.blit(intro_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            GameOn()
            gamestop = False
            run = True
        pygame.display.update()

def GameOn():
    class BackGround:
        def __init__(self):
            self.back = pygame.image.load('back.png')
            self.back = pygame.transform.scale(self.back, [SCREEN_WIDTH, SCREEN_HEIGHT]).convert_alpha()
            self.back_width = self.back.get_width()
            self.back_i = 0

        def loop(self):
            SCREEN.blit(self.back, [self.back_i, 0])
            SCREEN.blit(self.back, [self.back_width + self.back_i, 0])
            self.back_i -= 2
            if self.back_i < -SCREEN_WIDTH:
                self.back_i = 0


    class Flappy_Bird:
        def __init__(self):
            # bird
            self.bird_img = pygame.image.load('bird.png')
            self.bird_img = pygame.transform.scale(self.bird_img, [40, 30]).convert_alpha()
            self.bird_x = SCREEN_WIDTH / 4
            self.bird_y = SCREEN_HEIGHT / 2
            self.bird_vel = 0.5
            self.bird_move = 0

        def jump(self):
            self.bird_rect = SCREEN.blit(self.bird_img, [self.bird_x, self.bird_y])
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                # fly = pygame.mixer.Sound('wing.wav')
                # fly.play()
                pygame.mixer.music.load('wing.wav ')
                pygame.mixer.music.play()
                self.bird_move = 0
                self.bird_move -= 7
            self.bird_move += self.bird_vel
            self.bird_y += self.bird_move


    class CreatePipes:
        def __init__(self):
            self.width = 60
            self.height = 450
            self.pipe_img = pygame.transform.scale(pygame.image.load('pipe.png'), [self.width, self.height]).convert_alpha()
            self.pipe_list = []

        def generate_pipes(self):

            can_gen = True

            for pipe in self.pipe_list:
                if pipe.x > SCREEN_WIDTH * 0.5:
                    can_gen = False
            if can_gen:
                self.pipe_list.append(
                    pygame.Rect(
                        SCREEN_WIDTH,
                        random.randint(int(SCREEN_HEIGHT * 0.4), int(SCREEN_HEIGHT * 0.7)),
                        self.width, self.height
                    )
                )

        def scrollpipe(self):
            for pipe in self.pipe_list:
                pipe.x -= 2
                if pipe.x < 0 - pipe.width:
                    self.pipe_list.remove(pipe)

    class Check_Death:
        def check_death(self, pipes):
            self.gameover = False
            for pipe in pipes:
                if bird.bird_rect.colliderect(pipe) or bird.bird_rect.colliderect(pygame.Rect(pipe.x, pipe.y - 630, pipe.width + 20, pipe.height)):
                    self.GameOver = True

            if bird.bird_y <= -5 or bird.bird_y >= SCREEN_HEIGHT - 5:
                pygame.mixer.music.load('wing.wav ')
                pygame.mixer.music.play()
                self.GameOver = True


    c_pipes = CreatePipes()
    bird = Flappy_Bird()
    bg = BackGround()
    death = Check_Death()
    death.GameOver = False
    run = True
    i = 0

    while run:

        if death.GameOver:
            welcome()
            run = False

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            bg.loop()
            bird.jump()
            c_pipes.generate_pipes()
            c_pipes.scrollpipe()
            for pipe in c_pipes.pipe_list:
                SCREEN.blit(c_pipes.pipe_img, pipe)
                SCREEN.blit(pygame.transform.flip(c_pipes.pipe_img, False, True), pygame.Rect(
                    pipe.x,
                    pipe.y - 630,
                    pipe.width + 20, pipe.height
                ))
            death.check_death(pipes=c_pipes.pipe_list)

            for pipe in c_pipes.pipe_list:
                if -1< pipe.x - bird.bird_x < 1:
                    i += 1
                    print(i)

            clock.tick(60)
            pygame.display.update()

welcome()