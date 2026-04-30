import pygame
import sys
from racerclasses import Player, Enemy, Coin, bg, Obstacle
import persistence 
import random


pygame.init()
WIDTH, HEIGHT = 400, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

user_name = ""
STATE_MENU = "MENU"
STATE_GAME = "GAME"
STATE_GAMEOVER = "GAMEOVER"
STATE_SETTINGS = "SETTINGS"       
STATE_LEADERBOARD = "LEADERBOARD" 

current_state = STATE_MENU

saving_done = False

game_settings = persistence.load_settings()

def reset_game():
    '''default game settings'''
    global p1, enemies, coins, all_sprites, score, background, obstacles, hp, active_pows
    p1 = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group(enemy)
    coins = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(p1, enemy)
    score = 0
    hp = 3  
    active_pows = []
    background = bg()

def draw_text(text, font_size, y_pos, color=(255, 255, 255)):
    
    font = pygame.font.SysFont("Verdana", font_size)
    text_surf = font.render(str(text), True, color)
    screen_width = screen.get_width()
    text_rect = text_surf.get_rect(center=(screen_width // 2, y_pos))
    screen.blit(text_surf, text_rect)

def infoset(screen, hp, active_pows):
    '''hp, shield timer info'''
    pygame.draw.rect(screen, (220, 0, 0), (10, 35, hp*30, 10))
    y_offset = 60
    current_time = pygame.time.get_ticks()

    for pow in active_pows[:]:
        timeleft = (pow["end_time"] - current_time) // 1000

        if timeleft > 0:
            font = pygame.font.SysFont("Verdana", 12)
            powtext = font.render(f"{pow['type'].upper()}: {timeleft}s", True, (0, 0, 255))
            screen.blit(powtext, (10, y_offset))
            y_offset += 25
        else:
            active_pows.remove(pow) 

reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if current_state == STATE_MENU:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset_game()
                current_state = STATE_GAME
        
        if current_state == STATE_GAMEOVER:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                current_state = STATE_GAME


    if current_state == STATE_MENU:
        screen.fill((50, 50, 50))
        #menu screen
        draw_text("RACER", 64, 150, (255, 0, 0))
        draw_text("Enter your name:", 24, 250, (255, 255, 255))
        pygame.draw.rect(screen, (255, 255, 255), (100, 280, 200, 40))
        draw_text(user_name + "|", 28, 300, (0, 0, 0))
        if len(user_name) > 0:
            draw_text("Press SPACE to Start", 20, 380, (0, 255, 0))
        else:
            draw_text("Type your name to unlock Start", 18, 380, (150, 150, 150))
        draw_text("Press L for Leaderboard", 18, 420, (200, 200, 200)) 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: 
                    current_state = STATE_LEADERBOARD


                if event.key == pygame.K_s:
                    current_state = STATE_SETTINGS
                
                if event.key == pygame.K_SPACE and len(user_name) > 0:
                    reset_game()
                    current_state = STATE_GAME
                
                
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                
                
                elif event.key != pygame.K_SPACE:
                    if len(user_name) < 10 and event.unicode.isalnum():
                        user_name += event.unicode
        
        
    elif current_state == STATE_GAME:
        #game screen
        background.move()
        background.draw(screen)
        
        p1.move()
        for enemy in enemies:
            enemy.move(score)
        
        if random.randint(1, 50) == 1:
            choice = random.random()
            if choice < 0.6: 
                new_item = Coin("coin")
                coins.add(new_item)
                all_sprites.add(new_item)
            elif choice < 0.8: 
                new_bonus = Coin(random.choice(["nitro", "shield", "repair"]))
                coins.add(new_bonus)
                all_sprites.add(new_bonus)
            else: 
                new_obs = Obstacle(random.choice(["oil", "barrier", "pothole"]))
                obstacles.add(new_obs)
                all_sprites.add(new_obs)

        for c in coins:
            c.move()

        for obs in obstacles:
            obs.move(5)
        
        global hp, active_pows
        #intersect obst
        hit_obstacles = pygame.sprite.spritecollide(p1, obstacles, True)
        for obs in hit_obstacles:
            if obs.type == "oil":
                p1.rect.move_ip(random.choice([-30, 30]), 0)
            elif obs.type == "barrier" or obs.type == "pothole":
                if p1.shield:
                    p1.shield = False
                else:
                    hp -= 1

        if hp <= 0:
            current_state = STATE_GAMEOVER
        
        #intersect powerups and coins
        hit_items = pygame.sprite.spritecollide(p1, coins, True)
        for item in hit_items:
            if item.type == "coin":
                score += item.weigh
            
            elif item.type == "nitro":
                p1.speed += 5 
            
            elif item.type == "shield":
                p1.shield = True 
                new_effect = {
                    "type": "shield", 
                    "end_time": pygame.time.get_ticks() + 5000 
                }
                active_pows.append(new_effect)
                for p in coins:
                    if pygame.sprite.collide_rect(p1, p):
                        p.kill()
                
            elif item.type == "repair":
                if hp<3:
                    hp+=1
                
       #intersect enemies 
        if pygame.sprite.spritecollideany(p1, enemies):
            if p1.shield:
                p1.shield = False 
                pygame.sprite.spritecollide(p1, enemies, True) 
                enemies.add(Enemy())
            else:
                current_state = STATE_GAMEOVER

        
        infoset(screen, hp, active_pows)

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

    elif current_state == STATE_GAMEOVER:
        #gameover screen
        if not saving_done:
            persistence.add_score(user_name, score)
            saving_done = True
            
        screen.fill((200, 0, 0))
        draw_text("GAME OVER", 64, 200, (255, 255, 255))
        draw_text(f"{user_name}, your score: {score}", 32, 300, (255, 255, 0))
        draw_text("Press R to Restart or M for Menu", 20, 400, (255, 255, 255))
        
        for event in pygame.event.get():
            #through screens
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    saving_done = False 
                    current_state = STATE_GAME
                if event.key == pygame.K_m:
                    current_state = STATE_MENU
                    saving_done = False

    elif current_state == STATE_LEADERBOARD:
        #lb screen
        screen.fill((20, 20, 20)) 
        draw_text("TOP 10 RACERS", 40, 60, (255, 215, 0))

        scores = persistence.load_leaderboard()
        
        y_offset = 130
        
        if not scores:
            draw_text("No records yet!", 20, 250, (150, 150, 150))
        else:
            
            for i, entry in enumerate(scores[:10]):
                name = entry['name']
                pts = entry['score']
               
                row_text = f"{i+1}. {name.ljust(10)} {str(pts).rjust(5)}"
                
                draw_text(row_text, 22, y_offset, (255, 255, 255))
                y_offset += 35 

        draw_text("Press M to return to Menu", 18, 550, (100, 100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    current_state = STATE_MENU

    elif current_state == STATE_SETTINGS:
        #settings screen
        screen.fill((40, 40, 40)) 
        
        draw_text("SETTINGS", 40, 100, (255, 215, 0)) 
        
        sound_text = "ON" if game_settings["sound"] else "OFF"
        draw_text(f"Sound: {sound_text} (Press S)", 25, 200)
        
        color_text = game_settings["car_color"].upper()
        draw_text(f"Car Color: {color_text} (Press C)", 25, 280)
        
        draw_text("Press M to Menu", 18, 450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    game_settings["sound"] = not game_settings["sound"]
                    persistence.save_settings(game_settings) 

                    
                if event.key == pygame.K_c:
                    if game_settings["car_color"] == "red":
                        game_settings["car_color"] = "blue"
                    else:
                        game_settings["car_color"] = "red"
                    persistence.save_settings(game_settings)
                    new_path = f"racer/Player_{game_settings['car_color']}.png"
                    p1.image = pygame.image.load(new_path)


                if event.key == pygame.K_m:
                    current_state = STATE_MENU
    
    
    pygame.display.flip()
    clock.tick(60)