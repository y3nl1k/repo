import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((300, 600))

class player(pygame.sprite.Sprite):
    def __init__(self, path = "racer\Player.png"):
        super().__init__()
        impimg=pygame.image.load(path)
        self.image=impimg
        self.rect=self.image.get_rect()
        self.rect.center=(47, 553)

    def move(self):
        button=pygame.key.get_pressed()

        if button[K_a]:
            self.rect.centerx-=3
        elif button[K_d]:
            self.rect.centerx+=3

        if self.rect.centerx<47:
            self.rect.centerx=47
        if self.rect.centerx>253:
            self.rect.centerx=253


class opp(pygame.sprite.Sprite):
    def __init__(self, path = "racer\Enemy.png"):
        super().__init__()
        imping=pygame.image.load(path)
        self.image=imping
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(47, 253), 75)
        self.fspead = 5
        self.spead = self.fspead
        

    def move(self, curscore):
        
        self.rect.centery+=self.spead

        if self.rect.centery>675:
            self.rect.centery=-75
            self.rect.centerx=random.randint(47, 253)
        
        plus = curscore//10
        self.spead = self.fspead+plus


class Coin(pygame.sprite.Sprite):
    def __init__(self, path = "racer\dollar.png"):
        super().__init__()
        self.weigh=random.choice([1, 2, 3])

        imping=pygame.image.load(path)
        if self.weigh==1:
            self.image=pygame.transform.scale(imping, (20, 20))
        
        elif self.weigh==2:
            self.image=pygame.transform.scale(imping, (30, 30))
        
        else: 
            self.image=pygame.transform.scale(imping, (50, 50))
        
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(47, 253), 100)
        self.spead = 9

    def move(self):
        self.rect.centery+=self.spead
        if self.rect.centery>675:
            self.rect.centery=-75
            self.rect.centerx=random.randint(47, 253)



class bg():
    def __init__(self):
        self.image = pygame.image.load("racer/AnimatedStreet.png")
        self.rect = self.image.get_rect()
        
        self.y1 = 0
        self.y2 = -self.rect.height
        self.speed = 5

    def move(self):
    
        self.y1 += self.speed
        self.y2 += self.speed
        
    
        if self.y1 >= self.rect.height:
            self.y1 = -self.rect.height
            
    
        if self.y2 >= self.rect.height:
            self.y2 = -self.rect.height

    def draw(self, screen):
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))


playa=player()
oppon=opp()

cars=pygame.sprite.Group()
cars.add(playa)
cars.add(oppon)

oppons=pygame.sprite.Group()
oppons.add(oppon)

background = bg()
honk_sound = pygame.mixer.Sound("racer\crash.wav")


coins = pygame.sprite.Group()
score_coins = 0
font_score = pygame.font.SysFont("Verdana", 20)

ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, 2000)


running = True

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==ADDCOIN:
            new_item = Coin()     
            coins.add(new_item)



    background.move()
    background.draw(screen)

    
    for car in cars:
        screen.blit(car.image, car.rect)
        if isinstance(car, opp):
            car.move(score_coins)
        else:
            car.move()


    for coin in coins:
        coin.move()
        screen.blit(coin.image, coin.rect)

    collided_coins = pygame.sprite.spritecollide(playa, coins, True)
    for coin in collided_coins:
        score_coins += coin.weigh

    

    
    score_text = font_score.render(f"Coins: {score_coins}", True, (0, 0, 0))
    screen.blit(score_text, (200, 10))


    if pygame.sprite.spritecollideany(playa, oppons):
        screen.fill((255, 10, 10))
        font=pygame.font.SysFont("open dyslexic", 28)
        text = font.render("final score " + str(score_coins), True, (0, 255, 255))

        rect = text.get_rect()
        rect.center=(150, 300)
        honk_sound.play()   
        screen.blit(text,rect)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    
    pygame.time.Clock().tick(60)
    pygame.display.flip()
 


