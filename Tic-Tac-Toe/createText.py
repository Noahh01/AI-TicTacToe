import pygame

def create_text(msg: str, surface, size: int, x: int, y: int, colour, center= False):
    """Renders text and displays it on screen.Center parameter used to center text (by defult not centered (False))"""
    
    font = pygame.font.SysFont('serif', size)
    text = font.render(msg, True, colour)
    if center:
        textSurface = text.get_rect()
        textSurface.center = surface.get_width()/2, surface.get_height()/2
        surface.blit(text, textSurface)
    else:
        surface.blit(text, (x, y))
    return True
 
def draw_score(score, surface, x, y):
    pygame.draw.rect(surface, (0, 0,0), (x, y, 150, 50))
    create_text('COUNT: ' + str(score), surface, 20, 395, 455, (255, 255, 255))
    
    
    