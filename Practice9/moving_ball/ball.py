import pygame 

pygame.init()
screen = pygame.display.set_mode((800, 600), )
pygame.display.set_caption("ball")


ball_x = 400
ball_y = 300
ball_radius = 25
step = 20
clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    screen.fill((255,255,255)) 
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if ball_x - step >= ball_radius:
                    ball_x -= step
            
            if event.key == pygame.K_RIGHT:
                if ball_x + step <= 800 - ball_radius:
                    ball_x += step
            
            if event.key == pygame.K_UP:
                if ball_y - step >= ball_radius:
                    ball_y -= step
            
            if event.key == pygame.K_DOWN:
                if ball_y + step <= 600 - ball_radius:
                    ball_y += step
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()