import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load("Lesson 5/images/background.png")
border = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

ship_width = 55
ship_height = 50

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        if color == "yellow":
            self.image = pygame.image.load("Lesson 5/images/yellowship.png")
            self.image = pygame.transform.rotate(self.image,90)
        elif color == "red":
            self.image = pygame.image.load("Lesson 5/images/redship.png")
            self.image = pygame.transform.rotate(self.image,270)
        self.color = color
        self.image = pygame.transform.scale(self.image,(ship_width,ship_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
    def handle_movements(self,keys_pressed):
        if self.color == "yellow":
            if keys_pressed[pygame.K_w] and self.rect.y > 50:
                self.rect.y -= 5
            if keys_pressed[pygame.K_a]:
                self.rect.x -= 5
            if keys_pressed[pygame.K_s] and self.rect.y < 500:
                self.rect.y += 5
            if keys_pressed[pygame.K_d]:
                self.rect.x +=5
        if self.color == "red":
            if keys_pressed[pygame.K_UP] and self.rect.y > 50:
                self.rect.y -= 5
            if keys_pressed[pygame.K_DOWN] and self.rect.y < 500:
                self.rect.y += 5
            if keys_pressed[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys_pressed[pygame.K_RIGHT]:
                self.rect.x +=5

red = Spaceship(700,HEIGHT/2,"red")
yellow = Spaceship(300,HEIGHT/2,"yellow")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    screen.fill("sky blue")
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,"white",border)
    screen.blit(red.image,red.rect.topleft)
    screen.blit(yellow.image,yellow.rect.topleft)
    keys_pressed = pygame.key.get_pressed()
    red.handle_movements(keys_pressed)
    yellow.handle_movements(keys_pressed)
    pygame.display.update()
