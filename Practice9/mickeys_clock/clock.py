import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")


main_clock = pygame.image.load("images/main_clock.png")
hands = pygame.image.load("images/hand2.png") 

hand_right = pygame.transform.scale(hands, (int(hands.get_width() * 0.3), int(hands.get_height() * 0.3)))
hand_left = pygame.transform.scale(hands, (int(hands.get_width() * 0.4), int(hands.get_height() * 0.4)))

clock_rect = main_clock.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def rotate_hand(surface, image, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    surface.blit(rotated_image, new_rect)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    
    sec_angle = -(seconds * 6)
    min_angle = -(minutes * 6)

    screen.fill((255, 255, 255))
    
    screen.blit(main_clock, clock_rect)

    rotate_hand(screen, hand_right, min_angle)
    rotate_hand(screen, hand_left, sec_angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()