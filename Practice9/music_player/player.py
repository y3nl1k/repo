import pygame
import os


pygame.init()
pygame.mixer.init() 

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

music_dir = "music_player/music/"
songs = [f for f in os.listdir(music_dir) if f.endswith('.wav')]
current_track = 0

def play_music():
    if songs:
        track_path = os.path.join(music_dir, songs[current_track])
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()

font = pygame.font.SysFont("Arial", 24)

running = True
is_paused = False

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                if not pygame.mixer.music.get_busy(): 
                    play_music()
                else:
                    if is_paused:
                        pygame.mixer.music.unpause()
                        is_paused = False
                    else:
                        pygame.mixer.music.pause()
                        is_paused = True
            
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            
            elif event.key == pygame.K_n: 
                current_track = (current_track + 1) % len(songs)
                play_music()
                is_paused = False
            
            elif event.key == pygame.key.key_code("b"): 
                current_track = (current_track - 1) % len(songs)
                play_music()
                is_paused = False
                
            elif event.key == pygame.K_q: 
                running = False
    instructions = [
        "P: Play/Pause",
        "S: Stop",
        "N: Next Track",
        "B: Previous Track",
        "Q: Quit"
    ]
    
    y_offset = 50
    for line in instructions:
        text_surf = font.render(line, True, BLACK)
        screen.blit(text_surf, (50, y_offset))
        y_offset += 30

    
    if songs:
        current_text = f"Playing: {songs[current_track]}"
        status = " (PAUSED)" if is_paused else " (PLAYING)"
        track_surf = font.render(current_text + status, True, (200, 0, 0))
        screen.blit(track_surf, (50, 300))
    else:
        error_surf = font.render("No music files found in music/ folder!", True, (255, 0, 0))
        screen.blit(error_surf, (50, 300))

    pygame.display.flip()

pygame.quit()