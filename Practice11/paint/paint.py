import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    color = (0, 0, 255)
    tool = 'brush'
    
    points = []
    start_pos = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b: tool = 'brush'
                if event.key == pygame.K_e: tool = 'eraser'
                if event.key == pygame.K_r: tool = 'rect'
                if event.key == pygame.K_c: tool = 'circle'
                if event.key == pygame.K_s: tool = 'square'
                if event.key == pygame.K_t: tool = 'righttri'
                if event.key == pygame.K_q: tool = 'equtri'
                if event.key == pygame.K_h: tool = 'rhombus'
                
                if event.key == pygame.K_1: color = (255, 0, 0)
                if event.key == pygame.K_2: color = (0, 255, 0)
                if event.key == pygame.K_3: color = (0, 0, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos
                    if tool == 'brush' or tool == 'eraser':
                        points.append({'tool': tool, 'pos': event.pos, 'color': color, 'radius': radius})

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:
                    if tool == 'brush' or tool == 'eraser':
                        points.append({'tool': tool, 'pos': event.pos, 'color': color, 'radius': radius})

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    shape_tools = ['rect', 'circle', 'square', 'righttri', 'equtri', 'rhombus']
                    if tool in shape_tools:
                        points.append({'tool': tool, 'start': start_pos, 'end': event.pos, 'color': color, 'radius': radius})
                    start_pos = None



        
        screen.fill((255, 255, 255))

        for p in points:
           
        
            if p['tool'] == 'brush':
                pygame.draw.circle(screen, p['color'], p['pos'], p['radius'])
            elif p['tool'] == 'eraser':
                pygame.draw.circle(screen, (255, 255, 255), p['pos'], p['radius'])

            elif p['tool'] in ['rect', 'circle', 'square', 'righttri', 'equtri', 'rhombus']:
 
                        
                x1, y1 = p['start']
                x2, y2 = p['end']

                if p['tool'] == 'rect':
                    x = min(p['start'][0], p['end'][0])
                    y = min(p['start'][1], p['end'][1])
                    w = abs(p['start'][0] - p['end'][0])
                    h = abs(p['start'][1] - p['end'][1])
                    pygame.draw.rect(screen, p['color'], (x, y, w, h), 2)
                elif p['tool'] == 'circle':
                    r = int(((p['start'][0]-p['end'][0])**2 + (p['start'][1]-p['end'][1])**2)**0.5)
                    pygame.draw.circle(screen, p['color'], p['start'], r, 2)
                elif p['tool'] == 'square':
                    side = max(abs(x2-x1), abs(y2-y1))
                    newx2 = x1 + side if x2 > x1 else x1 - side
                    newy2 = y1 + side if y2 > y1 else y1 - side
                    pygame.draw.rect(screen, p['color'], (min(x1, newx2), min(y1, newy2), side, side), 2)
                elif p['tool'] == 'righttri':
                    pygame.draw.polygon(screen, p['color'], [(x1, y1), (x1, y2), (x2, y2)], 2)
                elif p['tool'] == 'equtri':
                    pygame.draw.polygon(screen, p['color'], [((x1+x2)/2, y1), (x1, y2), (x2, y2)], 2)
                elif p['tool'] == 'rhombus':
                    pygame.draw.polygon(screen, p['color'], [((x1+x2)/2, y1), (x2, (y1+y2)/2), ((x1+x2)/2, y2), (x1, (y1+y2)/2)], 2)
    
        if start_pos and (tool in ['rect', 'circle', 'square', 'righttri', 'equtri', 'rhombus']):
            curr_pos = pygame.mouse.get_pos()

            x1, y1 = start_pos  
            x2, y2 = curr_pos


            if tool == 'rect':
                pygame.draw.rect(screen, color, (min(start_pos[0], curr_pos[0]), min(start_pos[1], curr_pos[1]), abs(start_pos[0]-curr_pos[0]), abs(start_pos[1]-curr_pos[1])), 1)
            elif tool == 'circle':
                r = int(((start_pos[0]-curr_pos[0])**2 + (start_pos[1]-curr_pos[1])**2)**0.5)
                pygame.draw.circle(screen, color, start_pos, r, 1)
            elif tool == 'square':
                side = max(abs(x2-x1), abs(y2-y1))
                newx2 = x1 + side if x2 > x1 else x1 - side
                newy2 = y1 + side if y2 > y1 else y1 - side
                pygame.draw.rect(screen, color, (min(x1, newx2), min(y1, newy2), side, side), 1)
            elif tool == 'righttri':
                pygame.draw.polygon(screen, color, [(x1, y1), (x1, y2), (x2, y2)], 1)
            elif tool == 'equtri':
                pygame.draw.polygon(screen, color, [((x1+x2)/2, y1), (x1, y2), (x2, y2)], 1)
            elif tool == 'rhombus':
                pygame.draw.polygon(screen, color, [((x1+x2)/2, y1), (x2, (y1+y2)/2), ((x1+x2)/2, y2), (x1, (y1+y2)/2)], 1)
 

        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()