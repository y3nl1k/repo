import pygame
import sys
import db
import random
import json


def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"snake_color": [50, 200, 50], "sound": True, "grid": False}

def save_settings(data):
    with open("settings.json", "w") as f:
        json.dump(data, f)


current_settings = load_settings()


pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

COLORS = {
    "Green": (50, 200, 50),
    "Blue": (50, 50, 200),
    "Purple": (150, 50, 200),
    "Pink": (255, 105, 180)
}
color_names = list(COLORS.keys())

current_color_idx = 0


STATE_MENU = "MENU"
STATE_GAME = "GAME"
STATE_GAMEOVER = "GAMEOVER"
STATE_LEADERBOARD = "LEADERBOARD"
STATE_SETTINGS = "SETTINGS"
current_state = STATE_MENU


user_name = ""
personal_best = 0


try:
    db.init_db()
    print("conne")
except Exception as e:                  
    print(e)

def draw_text(text, size, x, y, color=BLACK):
    font = pygame.font.SysFont("arial", size)
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(x, y))
    screen.blit(surf, rect)

def reset_game(user_name):
    from game import Snake, Food
    color = current_settings["snake_color"]
    new_snake = Snake(color)
    new_food = Food(WIDTH, HEIGHT, is_poison=False)
    new_poison = Food(WIDTH, HEIGHT, is_poison=True)
    new_walls = []
    best = db.get_personal_best(user_name)
    power_up = None
    effect_end_time = 0
    return new_snake, new_food, new_poison, new_walls, 0, 1, best, power_up, effect_end_time


running = True
while running:
    screen.fill(WHITE)
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if current_state == STATE_MENU:
        draw_text("SNAKE GAME", 50, WIDTH//2, 100)
        draw_text("Enter your name:", 20, WIDTH//2, 180)
        draw_text("Press L for Leaderboard", 16, WIDTH//2, 340, BLACK)
        draw_text("Press S for Settings", 16, WIDTH//2, 380, BLACK)
    
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    current_state = STATE_LEADERBOARD
                if event.key == pygame.K_s:
                    current_state = STATE_SETTINGS
      
        pygame.draw.rect(screen, GRAY, (WIDTH//2 - 100, 210, 200, 40))
        draw_text(user_name + "|", 24, WIDTH//2, 230)
        
        if len(user_name) > 0:
            draw_text("Press ENTER to Play", 18, WIDTH//2, 300, (0, 150, 0))
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(user_name) > 0:
                    try:
                        conn = db.get_connection()
                        cur = conn.cursor()
                        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT DO NOTHING", (user_name,))
                        conn.commit()
                        cur.close()
                        conn.close()
                        print(f"player {user_name} added")
                    except Exception as e:
                        print(e)
                   
                    snake, food, poison, walls, score, level, personal_best,power_up, effect_end_time = reset_game(user_name)
                    personal_best = db.get_personal_best(user_name)
                    current_state = STATE_GAME
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    if len(user_name) < 15 and event.unicode.isalnum():
                        user_name += event.unicode

            

    elif current_state == STATE_LEADERBOARD:
            
            screen.fill((30, 30, 30)) 
            draw_text("TOP 10 ALL-TIME", 40, WIDTH//2, 50, (255, 215, 0)) 
        
            top_scores = db.get_top_10()
            
    
            draw_text("Name          Score    Lvl", 20, WIDTH//2, 100, WHITE)
            draw_text("-" * 40, 20, WIDTH//2, 115, WHITE)

            y_pos = 140
            for i, row in enumerate(top_scores):
            
                name_text = f"{i+1}. {row[0][:10]}" 
                score_text = f"{row[1]}"
                level_text = f"{row[2]}"
                
        
                display_str = f"{name_text:<15} {score_text:<8} {level_text}"
                draw_text(display_str, 18, WIDTH//2, y_pos, WHITE)
                y_pos += 25

            draw_text("Press M to return to Menu", 18, WIDTH//2, 370, GRAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        current_state = STATE_MENU


    elif current_state == STATE_GAMEOVER:
        screen.fill((40, 10, 10)) 
        
        draw_text("GAME OVER", 50, WIDTH//2, 80, (255, 50, 50))
        draw_text(f"Player: {user_name}", 20, WIDTH//2, 150, WHITE)
        draw_text(f"Final Score: {score}", 30, WIDTH//2, 190, (255, 215, 0))
        draw_text(f"Level Reached: {level}", 22, WIDTH//2, 230, WHITE)
        draw_text(f"Your Personal Best: {personal_best}", 20, WIDTH//2, 280, (100, 200, 255))
        draw_text("Press R to Try Again", 20, WIDTH//2, 350, WHITE)
        draw_text("Press M for Main Menu", 20, WIDTH//2, 380, (150, 150, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake, food, poison, walls, score, level, personal_best, power_up, effect_end_time = reset_game(user_name)
                    current_state = STATE_GAME
                elif event.key == pygame.K_m:
                    current_state = STATE_MENU


    elif current_state == STATE_SETTINGS:
        screen.fill((40, 40, 40))
        draw_text("SETTINGS", 40, WIDTH//2, 50, WHITE)

        grid_status = "ON" if current_settings["grid"] else "OFF"
        sound_status = "ON" if current_settings["sound"] else "OFF"

        color_status = "unk"
        for name, rgb in COLORS.items():
            if tuple(current_settings["snake_color"]) == rgb:
                color_status = name

        draw_text(f"1. Grid: {grid_status} (Press G)", 25, WIDTH//2, 150, WHITE)
        draw_text(f"2. Sound: {sound_status} (Press S)", 25, WIDTH//2, 200, WHITE)

        pygame.draw.rect(screen, current_settings["snake_color"], (WIDTH//2 + 100, 300, 20, 20))


        draw_text("Press M to save and return", 18, WIDTH//2, 350, GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    current_settings["grid"] = not current_settings["grid"]
                if event.key == pygame.K_s:
                    current_settings["sound"] = not current_settings["sound"]
                if event.key == pygame.K_c:
                    current_color_idx = (current_color_idx + 1) % len(color_names)
                    new_color_name = color_names[current_color_idx]
                    current_settings["snake_color"] = COLORS[new_color_name]
                if event.key == pygame.K_m:
                    save_settings(current_settings) 
                    current_state = STATE_MENU


    elif current_state == STATE_GAME:
        screen.fill(WHITE)

        if 'snake' not in locals():
            from game import Snake, Food, Obstacle
            snake = Snake(new_color_name)
            food = Food(WIDTH, HEIGHT, is_poison=False)
            poison = Food(WIDTH, HEIGHT, is_poison=True)
            walls = []
            score = 0
            level = 1

        if current_settings["grid"]:
            for x in range(0, WIDTH, 10):
                pygame.draw.line(screen, (230, 230, 230), (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, 10):
                pygame.draw.line(screen, (230, 230, 230), (0, y), (WIDTH, y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != "d": snake.direction = "u"
        if keys[pygame.K_DOWN] and snake.direction != "u": snake.direction = "d"
        if keys[pygame.K_LEFT] and snake.direction != "r": snake.direction = "l"
        if keys[pygame.K_RIGHT] and snake.direction != "l": snake.direction = "r"


        snake.move()
        head = snake.body[0]


        if snake.check_collision(WIDTH, HEIGHT, walls):

            db.save_result(user_name, score, level)
            personal_best = db.get_personal_best(user_name)
            current_state = STATE_GAMEOVER
            
            del snake 
            continue
       
        if head == food.pos:
            score += 1
            snake.body.append(snake.body[-1]) 
            food.spawn(WIDTH, HEIGHT, walls, snake.body)
            
            if score % 5 == 0:
                level += 1
                snake.speed += 2
                if level >= 3:
                    from game import Obstacle
                    obs = Obstacle(snake.body + walls, WIDTH, HEIGHT, 3)
                    walls.extend(obs.blocks)

        else:
            snake.body.pop()

        if head == poison.pos:
            is_dead = snake.eat(is_poison=True)
            if is_dead:
                db.save_result(user_name, score, level)
                personal_best = db.get_personal_best(user_name)
                current_state = STATE_GAMEOVER
                del snake 
                continue    
            if len(snake.body)>0:
                snake.body.pop()  
            poison.spawn(WIDTH, HEIGHT, walls, snake.body)

       
        if power_up is None:
            if random.randint(1, 150) == 1: 
                from game import PowerUp
                power_up = PowerUp(WIDTH, HEIGHT)
        
        if power_up and power_up.is_expired():
            power_up = None

        
        if power_up and head == power_up.pos:
            effect_end_time = pygame.time.get_ticks() + 5000 
            if power_up.type == "speed": snake.speed += 7
            elif power_up.type == "slow": snake.speed = max(5, snake.speed - 5)
            elif power_up.type == "shield": snake.shield = True
            power_up = None

        
        if effect_end_time>0 and pygame.time.get_ticks() > effect_end_time:
            snake.speed = 10 + (level - 1) * 2 
            effect_end_time = 0
      
        if power_up:
            pygame.draw.rect(screen, power_up.color, (power_up.pos[0], power_up.pos[1], 9, 9))

   
        for segment in snake.body:
            pygame.draw.rect(screen, snake.color, (segment[0], segment[1], 9, 9))
        
        pygame.draw.rect(screen, food.color, (food.pos[0], food.pos[1], 9, 9))
        pygame.draw.rect(screen, poison.color, (poison.pos[0], poison.pos[1], 9, 9))
        
        for w in walls:
            pygame.draw.rect(screen, (100, 100, 100), (w[0], w[1], 9, 9))

        draw_text(f"Score: {score}  Level: {level}  Best: {personal_best}", 18, WIDTH//2, 20)

        clock.tick(snake.speed)

        
    pygame.display.flip()
    clock.tick(30)