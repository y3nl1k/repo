'''import pygame 

pygame.init()
screen=pygame.display.set_mode((800, 600), )
xx=50
yy=50
running = True
clock = pygame.time .Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                if xx-20>=0:
                    xx-=20

            if event.key == pygame.K_RIGHT:
                if xx+20<=800-100:
                    xx+=20


            if event.key == pygame.K_UP:
                if yy-20>=0:
                    yy-=20


            if event.key == pygame.K_DOWN:
                if yy+20<=600-140:
                    yy+=20

    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (xx, yy, 100, 140))


    pygame.display.flip()
    clock.tick(30)
pygame.quit()'''
