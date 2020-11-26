from raycasting_pygame.lib.ray import Ray
from raycasting_pygame.res.glob import *

class Source:
    def __init__(self, step):
        self.step = step
        
    def update(self, mx, my, screen, walls):
        rays = []
        
        #make rays
        turn_angle = 0
        while turn_angle < 360:
            ray = Ray(mx, my, m.radians(turn_angle))
            rays.append(ray)
            turn_angle += self.step        
        for ray in rays:
            ray.update(walls)

        #connect rays to make shadows
        i = 0
        while i <= (360 / self.step) + 1:
            print("in loop")
            if i + 1 < len(rays):
                pygame.draw.polygon(screen, colors.white, [(mx, my), (rays[i].endx, rays[i].endy), (rays[i+1].endx, rays[i+1].endy)]) 
            i += 1
        pygame.draw.polygon(screen, colors.white, [(mx, my), (rays[0].endx, rays[0].endy), (rays[len(rays)-1].endx, rays[len(rays)-1].endy)])               