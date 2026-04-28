import pygame
import datetime


def flood_fill(surf, start_pos, new_col):
    target_col = surf.get_at(start_pos)
    if target_col == new_col: return
    width, height = surf.get_size()
    pixels_to_fill = [start_pos]
    while pixels_to_fill:
        cx, cy = pixels_to_fill.pop()
        if 0 <= cx < width and 0 <= cy < height and surf.get_at((cx, cy)) == target_col:
            surf.set_at((cx, cy), new_col)
            pixels_to_fill.append((cx - 1, cy))
            pixels_to_fill.append((cx + 1, cy))
            pixels_to_fill.append((cx, cy - 1))
            pixels_to_fill.append((cx, cy + 1))


def draw_shape(surf, tool, start, end, col, thickness):
    x1, y1 = start
    x2, y2 = end
    if tool == 'line':
        pygame.draw.line(surf, col, start, end, thickness)
    elif tool == 'rect':
        pygame.draw.rect(surf, col, (min(x1, x2), min(y1, y2), abs(x1-x2), abs(y1-y2)), thickness)
    elif tool == 'circle':
        r = int(((x1-x2)**2 + (y1-y2)**2)**0.5)
        pygame.draw.circle(surf, col, start, r, thickness)
    elif tool == 'square':
        side = max(abs(x2-x1), abs(y2-y1))
        nx2 = x1 + side if x2 > x1 else x1 - side
        ny2 = y1 + side if y2 > y1 else y1 - side
        pygame.draw.rect(surf, col, (min(x1, nx2), min(y1, ny2), side, side), thickness)
    elif tool == 'righttri':
        pygame.draw.polygon(surf, col, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif tool == 'equtri':
        pygame.draw.polygon(surf, col, [((x1+x2)/2, y1), (x1, y2), (x2, y2)], thickness)
    elif tool == 'rhombus':
        pts = [((x1+x2)/2, y1), (x2, (y1+y2)/2), ((x1+x2)/2, y2), (x1, (y1+y2)/2)]
        pygame.draw.polygon(surf, col, pts, thickness)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    canvas = pygame.Surface((800, 600))
    canvas.fill((255, 255, 255))
    clock = pygame.time.Clock()
    
    thickness = 2
    color = (0, 0, 255)
    tool = 'brush'
    start_pos = None
    last_pos = None
    
 
    font = pygame.font.SysFont("Arial", 24)
    text_input = ""
    text_pos = None
    typing = False

    while True:
 
        screen.blit(canvas, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
 
            if typing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        img = font.render(text_input, True, color)
                        canvas.blit(img, text_pos)
                        text_input = ""; typing = False
                    elif event.key == pygame.K_ESCAPE:
                        text_input = ""; typing = False
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        text_input += event.unicode
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b: tool = 'brush'
                if event.key == pygame.K_e: tool = 'eraser'
                if event.key == pygame.K_r: tool = 'rect'
                if event.key == pygame.K_c: tool = 'circle'
                if event.key == pygame.K_s: tool = 'square'
                if event.key == pygame.K_t: tool = 'righttri'
                if event.key == pygame.K_q: tool = 'equtri'
                if event.key == pygame.K_h: tool = 'rhombus'
                if event.key == pygame.K_l: tool = 'line'
                if event.key == pygame.K_p: tool = 'pencil'
                if event.key == pygame.K_f: tool = 'fill'
                if event.key == pygame.K_x: tool = 'text'

                
                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    pygame.image.save(canvas, f"paint_{now}.png")
                    print("Saved!")
                
            
                if event.key == pygame.K_1: color = (255, 0, 0)
                if event.key == pygame.K_2: color = (0, 255, 0)
                if event.key == pygame.K_3: color = (0, 0, 255)
                if event.key == pygame.K_4: thickness = 2
                if event.key == pygame.K_5: thickness = 5
                if event.key == pygame.K_6: thickness = 10

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos
                    if tool == 'fill':
                        flood_fill(canvas, event.pos, color)
                    elif tool == 'pencil':
                        last_pos = event.pos
                    elif tool == 'text':
                        typing = True; text_pos = event.pos

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if tool == 'brush':
                        pygame.draw.circle(canvas, color, event.pos, thickness)
                    elif tool == 'eraser':
                        pygame.draw.circle(canvas, (255, 255, 255), event.pos, thickness)
                    elif tool == 'pencil' and last_pos:
                        pygame.draw.line(canvas, color, last_pos, event.pos, thickness)
                        last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    shape_tools = ['rect', 'circle', 'square', 'righttri', 'equtri', 'rhombus', 'line']
                    if tool in shape_tools and start_pos:
                        draw_shape(canvas, tool, start_pos, event.pos, color, thickness)
                    start_pos = None
                    last_pos = None

        
        if start_pos and (tool in ['rect', 'circle', 'square', 'righttri', 'equtri', 'rhombus', 'line']):
            draw_shape(screen, tool, start_pos, pygame.mouse.get_pos(), color, 1)

        if typing:
            txt_img = font.render(text_input + "|", True, color)
            screen.blit(txt_img, text_pos)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()