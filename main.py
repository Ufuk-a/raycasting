from raycasting_pygame.lib.source import Source
from raycasting_pygame.lib.wall import Wall
from raycasting_pygame.res.glob import *

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    walls = [Wall(0, 0, 600, 0),
             Wall(0, 0, 0, 600),
             Wall(599, 599, 599, 1),
             Wall(599, 599, 1, 599)]
    source = Source(1)
    running = True
    drawing = False 
    sx, sy = None, None

    while running:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawing = True
                sx, sy = event.pos
            if drawing and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                drawing = False   
                ex, ey = event.pos
                wall = Wall(sx, sy, ex, ey) 
                walls.append(wall)
                

        screen.fill(colors.black)
        if drawing and pygame.mouse.get_pressed()[0] == 1:
            pygame.draw.line(screen, colors.white, (sx, sy), (mx, my))
        if not drawing:
            source.update(mx, my, screen, walls)
        for wall in walls:
            wall.draw(screen)
        pygame.display.update()        

    pygame.quit()                        


if __name__ == "__main__":
    main()                        