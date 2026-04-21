import pygame
import random
from pygame.locals import *

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Levels")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FRUIT_COLOR = (200, 120, 0)
SNAKE_COLOR = (50, 200, 50)
WALL_COLOR = (100, 100, 100)


snake_speed = 7
score = 0
level = 1
cell_size = 10 


segments = [[50, 50], [60, 50], [70, 50]]
direction = "r"



walls = []

def generate_food():
    """Генерирует еду так, чтобы она не попала на змейку или стену"""
    while True:
        new_food = [random.randrange(0, WIDTH // 10) * 10, 
                    random.randrange(0, HEIGHT // 10) * 10]

        if new_food not in segments and new_food not in walls:
            return new_food

fruit = generate_food()
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[K_UP] and direction != "d": direction = "u"
    if keys[K_DOWN] and direction != "u": direction = "d"
    if keys[K_LEFT] and direction != "r": direction = "l"
    if keys[K_RIGHT] and direction != "l": direction = "r"


    head_x, head_y = segments[-1]
    if direction == "r": head_x += cell_size
    elif direction == "l": head_x -= cell_size
    elif direction == "u": head_y -= cell_size
    elif direction == "d": head_y += cell_size

    new_head = [head_x, head_y]

    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or 
        new_head in segments or new_head in walls):
        print(f"Game Over! Score: {score}")
        running = False

    segments.append(new_head) 

    if head_x == fruit[0] and head_y == fruit[1]:
        score += 1
        fruit = generate_food()
        

        if score % 3 == 0: 
            level += 1
            snake_speed += 2
            
            new_wall = [random.randrange(0, WIDTH // 10) * 10, 
                        random.randrange(0, HEIGHT // 10) * 10]
            walls.append(new_wall)
    else:
        segments.pop(0) 

    screen.fill(WHITE)

    
    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(wall[0], wall[1], 9, 9))


    pygame.draw.rect(screen, FRUIT_COLOR, pygame.Rect(fruit[0], fruit[1], 9, 9))

    
    for segment in segments:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], 9, 9))

    
    font = pygame.font.SysFont("times new roman", 20)
    score_surf = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_surf, (10, 10))

    pygame.display.flip()
    clock.tick(snake_speed)

pygame.quit()