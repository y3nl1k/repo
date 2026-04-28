import pygame
import random

class Snake:
    def __init__(self, color):
        self.size = 10
        self.body = [[100, 100], [90, 100], [80, 100]]
        self.direction = "r"
        self.color = color
        self.score = 0
        self.level = 1
        self.speed = 10
        
        
        self.shield = False
        self.speed_boost_time = 0 

    def move(self):
        head = self.body[0].copy()
        if self.direction == "r": head[0] += self.size
        elif self.direction == "l": head[0] -= self.size
        elif self.direction == "u": head[1] -= self.size
        elif self.direction == "d": head[1] += self.size
        
        self.body.insert(0, head) 
    def check_collision(self, width, height, obstacles):
        head = self.body[0]
        
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            return True
      
        if head in self.body[1:]:
            return True
   
        if head in obstacles:
            return True
        return False
    

    def eat(self, is_poison=False):
        
        if is_poison:
           
            if len(self.body) > 2:
                self.body.pop()
                self.body.pop()
            else:
           
                return True 
        else:
         
            pass
        return False

class Food:
    def __init__(self, width, height, is_poison=False):
        self.size = 10
        self.is_poison = is_poison
       
        self.color = (200, 120, 0) if not is_poison else (139, 0, 0)
        self.pos = [random.randrange(0, width // 10) * 10, 
                    random.randrange(0, height // 10) * 10]

    def spawn(self, width, height, obstacles, snake_body):
        while True:
            new_pos = [random.randrange(0, width // 10) * 10, 
                       random.randrange(0, height // 10) * 10]
            if new_pos not in obstacles and new_pos not in snake_body:
                self.pos = new_pos
                break



class Obstacle:
    def __init__(self, snake_body, width, height, count):
        self.blocks = []
        while len(self.blocks) < count:
            new_block = [random.randrange(0, width // 10) * 10, 
                         random.randrange(0, height // 10) * 10]
            if new_block not in snake_body and abs(new_block[0] - snake_body[0][0]) > 30:
                self.blocks.append(new_block)

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, (100, 100, 100), (block[0], block[1], 9, 9))


class PowerUp:
    def __init__(self, width, height):
        self.size = 10
        self.pos = [random.randrange(0, width // 10) * 10, 
                    random.randrange(0, height // 10) * 10]
        self.type = random.choice(["speed", "slow", "shield"])
        self.spawn_time = pygame.time.get_ticks()
        self.colors = {"speed": (255, 255, 0), "slow": (0, 0, 255), "shield": (0, 255, 255)}
        self.color = self.colors[self.type]

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > 8000