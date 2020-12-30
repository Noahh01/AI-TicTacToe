import pygame
from Grid import*
from button import* 
from createText import create_text
from CheckWinner import*
from AI import*

#Display
pygame.init()
win = pygame.display.set_mode((380, 380))
pygame.display.set_caption('Tic-Tac-Toe')
win.fill((255, 255, 255))

#Colours 
black = (0, 0, 0)
white = (255, 255,255)
red = (255, 0, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)

#Class Objects Grid
one = Grid(win, 0, 0, 0, 0)
two = Grid(win, 130, 0, 0, 1)
three = Grid(win, 260, 0, 0, 2)
four = Grid(win, 0, 130, 1, 0)
five = Grid(win, 130, 130, 1, 1)
six = Grid(win, 260, 130, 1, 2)
seven = Grid(win, 0, 260, 2, 0)
eight = Grid(win, 130, 260, 2, 1)
nine = Grid(win, 260, 260, 2, 2)
grid = [one, two, three, four, five, six, seven, eight, nine]

#Class Object AI
CPU = AI_Player(grid, Grid.game_board)

#Grid
start = False
text = None
AI = False

#Buttons
multi_player = button(win, cyan, 25, 250, 150, 50, '2 PLAYERS')
multi_player.draw_button()
cpu = button(win, cyan, 205, 250, 150, 50, 'CPU')
cpu.draw_button()

#Text message
create_text("SELECT 2 PLAYERS OR CPU", win, 25, 33, 75, black)
   
#Main script
run = True
while run:
    
    if AI:
        pygame.time.delay(200)
        CPU.AI_start()  
        CPU.AI_attack()
        text = Winner_text(h, v, d, Grid.count)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
            
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() 
                        
            if start:   
                Grid.find_rect_pressed(pos, grid) 
            else: 
                if multi_player.interactive(pos):
                    win.fill(white)
                    Grid.draw_grid(grid)
                    start = True
                if cpu.interactive(pos):
                    win.fill(white)
                    Grid.draw_grid(grid)
                    start = True
                    AI = True
                    
    if text != None:
        pygame.time.delay(300)
        pygame.draw.rect(win, white, (0, 0, 380, 380))
        create_text(text, win, 35, 0, 0, black, True)
                  
    h = check_for_win_H(Grid.game_board)
    v = check_for_win_V(Grid.game_board)
    d = check_for_win_D(Grid.game_board)
    text = Winner_text(h, v, d, Grid.count)
    
    pygame.display.update()
pygame.quit()
