import pygame

#colour
white = (255, 255, 255)

class button:
    
    def __init__(self, surface, colour, x, y, w, h, text=''):
        self.surface = surface
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
    
    def draw_button(self, outline = None):
        if outline:
            pygame.draw.rect(self.surface, outline, (self.x - 2, self.y - 2, self.w + 4, self.h + 4))
            
        pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.w, self.h))
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, True, white)
            self.surface.blit(text, (self.x + (self.w/2 - text.get_width()/2), self.y + (self.h/2 - text.get_height()/2)))        
        
    def interactive(self, pos):
        if self.x < pos[0] < (self.x + self.w) and self.y < pos[1] < (self.y + self.h):  
            return True
        else:
            return False
    
        
    
        
        
        
            
    
        