from raycasting_pygame.res.glob import *

class Ray:
    
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
    
    def update(self, walls):
        last_dist = m.inf
        endx = self.x + (WIDTH * 2) * m.cos(self.angle)
        endy = self.y + (WIDTH * 2) * m.sin(self.angle)
                
        for wall in walls:
            den = (wall.x1 - wall.x2) * (self.y - endy) - (wall.y1 - wall.y2) * (self.x - endx)  
            if den != 0:
                t = ((wall.x1 - self.x) * (self.y - endy) - (wall.y1 - self.y) * (self.x - endx)) / den
                u = -((wall.x1 - wall.x2) * (wall.y1 - self.y) - (wall.y1 - wall.y2) * (wall.x1 - self.x)) / den
                if 0 < t < 1 and 0 < u:
                    colx, coly = (wall.x1 + t*(wall.x2 - wall.x1), wall.y1 + t*(wall.y2 - wall.y1))
                    dist = m.sqrt(((colx - self.x)**2) + ((coly - self.y)**2))
                    if dist <= last_dist:
                        last_dist = dist
                        endx, endy = colx, coly
        
        self.endx, self.endy = endx, endy                
                           
       