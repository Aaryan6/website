import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((749, 300))
clock = pygame.time.Clock()

font = pygame.font.SysFont("tahoma", 16)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


class Game:

    def __init__(self):
        self.run = True
        self.dino_x = 200
        self.dino_y = 205
        self.cactus_x = 1000
        self.cactus_y = 205
        self.i = 0
        self.points = 0
        self.jumpCount = 18
        self.isJump = False
        self.image = pygame.image.load('dino_base.png')
        self.image_w = self.image.get_width()
        self.dino = pygame.image.load('dinot.png')
        self.dino = pygame.transform.scale(self.dino, (80, 80))
        self.cactus = pygame.image.load('cactus.png')
        self.cactus = pygame.transform.scale(self.cactus, (40, 70))

    def loop(self):
        if self.i <= -749:
            self.i = 0
        screen.fill((32, 33, 36))
        screen.blit(self.image, (self.i, 179))
        screen.blit(self.image, (self.image_w + self.i, 179))
        self.i -= 7

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.isJump = True
        if self.isJump:
            self.dino_y -= self.jumpCount
            self.jumpCount -= 1
            if self.jumpCount < -18:
                self.isJump = False
                self.jumpCount = 18
        self.rect = screen.blit(self.dino, (self.dino_x, self.dino_y))

    def obj(self):
        self.cactus_x -= 7
        if self.cactus_x <= 0:
            self.cactus_x = 1000
        self.obstacle = screen.blit(self.cactus, (self.cactus_x, self.cactus_y))

    def isCollison(self):
        if self.rect.colliderect(self.obstacle):
            print("Game over")
            self.run = False
            pygame.draw.rect(screen, (255, 255, 0), self.rect, 4)
            pygame.quit()

std = Game()

while std.run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            std.run = False
            pygame.quit()
            sys.exit()
    std.loop()
    std.obj()
    std.jump()
    std.points += 0.1
    text_screen("Points : "+str(int(std.points)), (255, 255, 255), 20, 20)
    pygame.display.update()
    clock.tick(60)
    std.isCollison()
    # print(random_place)
pygame.quit()
quit()