import pygame
import random
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (150, 550)        
        
        self.shield = False
        self.nitro_frames = 0 
        self.speed = 5
        self.hp = 3

    def move(self):
        button = pygame.key.get_pressed()
        current_speed = self.speed
        if self.nitro_frames > 0:
            current_speed *= 2
            self.nitro_frames -= 1

        if button[K_a] and self.rect.left > 0:
            self.rect.move_ip(-current_speed, 0)
        if button[K_d] and self.rect.right < 400:
            self.rect.move_ip(current_speed, 0)

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


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -100)
        self.speed = 5

    def move(self, score):
        self.rect.move_ip(0, self.speed + (score // 10))
        if self.rect.top > 600:
            self.rect.top = -100
            self.rect.center = (random.randint(40, 360), -100)


class Coin(pygame.sprite.Sprite):
    def __init__(self, itype="coin"): 
        super().__init__()
        self.type = itype
        
        if self.type == "coin":
            img = pygame.image.load("racer/dollar.png")
            self.weigh = random.choice([1, 2, 3])
        
            if self.weigh == 1: s = 20
            elif self.weigh == 2: s = 30
            else: s = 50
            self.image = pygame.transform.scale(img, (s, s))
        else:
        
            self.image = pygame.image.load(f"racer/{itype}.png")
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.weigh = 0

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -50)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.kill()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obj_type):
        super().__init__()
        self.type = obj_type
        
        self.image = pygame.image.load(f"racer/{obj_type}.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        self.rect.center = (random.randint(40, 360), random.randint(-500, -50))

    def move(self, speed):
        self.rect.move_ip(0, speed) 
        if self.rect.top > 600:
            self.kill()