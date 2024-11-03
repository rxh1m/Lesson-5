import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

background = pygame.image.load("Lesson 5/images/background.png")
border = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

ship_width = 55
ship_height = 50
winner = ""

def draw_winner(text):
    font = pygame.font.SysFont('comicsans', 40)
    winner_text = font.render(text,1, "white")
    screen.blit(winner_text,(WIDTH/2, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(5000)

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
        self.health = 100
    def handle_movements(self,keys_pressed):
        if self.color == "yellow":
            if keys_pressed[pygame.K_w] and self.rect.y > 50:
                self.rect.y -= 5
            if keys_pressed[pygame.K_s] and self.rect.y < 500:
                self.rect.y += 5
            if keys_pressed[pygame.K_a] and self.rect.x > 50:
                self.rect.x -= 5
            if keys_pressed[pygame.K_d] and self.rect.x < border.x - 50:
                self.rect.x +=5
        if self.color == "red":
            if keys_pressed[pygame.K_UP] and self.rect.y > 50:
                self.rect.y -= 5
            if keys_pressed[pygame.K_DOWN] and self.rect.y < 500:
                self.rect.y += 5
            if keys_pressed[pygame.K_LEFT] and self.rect.x > border.x + 50:
                self.rect.x -= 5
            if keys_pressed[pygame.K_RIGHT] and self.rect.x < WIDTH - 50:
                self.rect.x +=5

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(x,y,10,5)
    def update(self):
        if self.color == "yellow":
            self.rect.x += 5
            if self.rect.x > WIDTH:
                self.kill()
        elif self.color == "red":
            self.rect.x -= 5
            if self.rect.x < 0:
                self.kill()

red = Spaceship(700,HEIGHT/2,"red")
yellow = Spaceship(300,HEIGHT/2,"yellow")

red_bullets = pygame.sprite.Group()
yellow_bullets = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullet = Bullet(yellow.rect.x + yellow.rect.width, yellow.rect.y + 25, "yellow")
                yellow_bullets.add(bullet)
            if event.key == pygame.K_r:
                bullet = Bullet(red.rect.x, red.rect.y + 25, "red")
                red_bullets.add(bullet)
    
    screen.fill("sky blue")
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,"white",border)
    screen.blit(red.image,red.rect.topleft)
    screen.blit(yellow.image,yellow.rect.topleft)
    
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,"yellow", bullet.rect)

    for bullet in red_bullets:
        pygame.draw.rect(screen,"red", bullet.rect)
        
    yellow_bullets.update()
    red_bullets.update()

    for bullet in yellow_bullets:
        if red.rect.colliderect(bullet.rect):
            red.health -= 1
            bullet.kill()

    for bullet in red_bullets:
        if yellow.rect.colliderect(bullet.rect):
            yellow.health -= 1
            bullet.kill()

    if red.health <= 0:
        winner = "Yellow wins!"  

    if yellow.health <= 0:
        winner = "Red wins!"                   

    if winner:
        draw_winner(winner)
        break
    
    
    keys_pressed = pygame.key.get_pressed()
    red.handle_movements(keys_pressed)
    yellow.handle_movements(keys_pressed)
    pygame.display.update()
