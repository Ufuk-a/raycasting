from raycasting_pygame.lib.ray import Ray
from raycasting_pygame.res.glob import *

class Source:
    def __init__(self, step, offset):
        self.step = step
        self.offset = offset
        
    def update(self, mx, my, screen, walls):
        rays = []
        
        #make rays
        for wall in walls:
            
            #get angles
            sdx, sdy = wall.y1 - my, wall.x1 - mx 
            edx, edy = wall.y2 - my, wall.x2 - mx
            s_angle = m.atan2(sdy, sdx)
            e_angle = m.atan2(edx, edy)
            
            #make main rays
            s_ray = Ray(mx, my, s_angle)
            e_ray = Ray(mx, my, e_angle)
            rays.extend((s_ray, e_ray))
            
            #make offset rays
            s_offset1 = Ray(mx, my, s_angle + self.offset)
            s_offset2 = Ray(mx, my, s_angle - self.offset)
            e_offset1 = Ray(mx, my, e_angle + self.offset)
            e_offset2 = Ray(mx, my, e_angle - self.offset)
            rays.extend((s_offset1, s_offset2, e_offset1, e_offset2))
            
        #compute all end points
        for ray in rays:
            ray.update(walls)
        
        #connect rays to make shadows
        i = 0
        while i < len(rays):
            if i + 1 < len(rays):
                pygame.draw.polygon(screen, colors.white, [(mx, my), (rays[i].endx, rays[i].endy), (rays[i+1].endx, rays[i+1].endy)]) 
            i += 1
        pygame.draw.polygon(screen, colors.white, [(mx, my), (rays[0].endx, rays[0].endy), (rays[len(rays)-1].endx, rays[len(rays)-1].endy)])               