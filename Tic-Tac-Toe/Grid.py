import pygame
from createText import create_text

class Grid:
    player_x = 'X'
    player_o = 'O'
    count = 0
    game_board = [[None, None, None], [None, None, None], [None, None, None]]

    def __init__(self, surface, x, y, r, c, rect=None, pressed=True):
        self.surface = surface
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.rect = rect
        self.pressed = pressed
    
    def append_grid(self, game_board:list):
        """ Appends X as 1 and O as 0, to 2D aray. Used to determine the winner and used for AI. 
        """
        if Grid.count % 2 == 0:
            game_board[self.r][self.c] = 1
        else:
            game_board[self.r][self.c] = 0
        return game_board
                    
    @staticmethod   
    def draw_grid(grid:list):
        """ Draws gird onto screen.
        """
        for elem in grid:
            elem.rect = pygame.draw.rect(elem.surface, (0, 0, 0), (elem.x, elem.y, 125, 125))
    
    @staticmethod
    def find_rect_pressed(pos, grid):
        """ Finds the sqaure pressed by the player.
        """
        for elem in grid:
            if elem.rect.collidepoint(pos):
                center_point = elem.rect.center
                elem.append_grid(Grid.game_board)
                elem.draw_player(center_point)
                
    @staticmethod
    def find_AI_rect(box):
        """ Finds the sqaure the AI has chosen.
        """
        center_point = box.rect.center
        box.append_grid(Grid.game_board)
        return box.draw_player(center_point)
                     
    
    def draw_player(self, center):
        """ Draws the X or O char on the screen depending on the turn.
        """
        if self.pressed:
            font = pygame.font.SysFont('comicsans', 160)
            if Grid.count % 2 == 0:
                player = Grid.player_x
            else:
                player = Grid.player_o
            text = font.render(player, True, (255, 255, 255))
            text_surface = text.get_rect()
            text_surface.center = center
            self.surface.blit(text, text_surface)
            Grid.count += 1
        self.pressed = False
    
            

    
    
    