import pygame
from Grid import*
import random
from CheckWinner import*
import copy

class AI_Player:
    StartCoor = None
    
    def __init__(self, grid: list, board: list):   #grid is the rects and board is the 2D list
        self.grid = grid
        self.board = board
    

    def find_box(self, r: int, c: int):
        """ Returns a tuple of the Gird object (the box) that the AI has seclected, the row and column.
        """
        for box in self.grid:
            if r == box.r and c == box.c:
                return box, r, c        
    
    
    def AI_start(self):
        """ Plays a random corner as AI's first move.
        """
        if Grid.count == 0:
            coor = [0, 2, 0, 2, 0, 2]
            c = random.choice(coor)
            r = random.choice(coor)
            for box in self.grid:
                if box.r == r and box.c == c:
                    Grid.find_AI_rect(box)
                    AI_Player.StartCoor = r, c
                    
    
    def get_moves(self):  
        """ Returns a 2d array containing all possible moves remaining.
        """
        moves = []             
        for r in range(3):
            for c in range(3):
                                
                if self.board[r][c] == None:
                    moves.append([r,c])
        return moves   
    
    
    def add_to_copy(self, r, c, val):
        """ Creates deepcopy of game board (2d array).
        """
        newboard = copy.deepcopy(self.board)
        newboard[r][c] = val
        
        return newboard
                       
    
    def AI_corners(self, coor:tuple):
        """ Checks for available postions in the corner to assist in winning.
        """
        if coor[0] == 0:
            #Checks horizontal corners
            if (coor[1] == 0) and (0 not in self.board[0]):
                box = self.find_box(0, 2)  
            elif (0 not in self.board[0]):
                box = self.find_box(0,0)
            #Checks vertical corner   
            elif (self.board[1][coor[1]] == None and self.board[2][coor[1]] == None):
                box = self.find_box(2, coor[1]) 
            #Checks diagonal corners 
            else:
                if (coor[1] == 0 and self.board[2][2] == None):
                    box = self.find_box(2, 2)
                elif (self.board[2][0] == None):
                    box = self.find_box(2, 0)
                    
        else:
            #Checks horizontal corners
            if (coor[1] == 0) and (0 not in self.board[2]):
                box = self.find_box(2, 2)   
            elif (0 not in self.board[2]):
                box = self.find_box(2, 0)            
            #Checks vertical corners   
            elif (self.board[1][coor[1]] == None and self.board[0][coor[1]] == None):
                box = self.find_box(0, coor[1])  
            #Checks diagonal corners 
            else:
                if (coor[1] == 0 and self.board[0][2] == None):
                    box = self.find_box(0, 2)
                elif (self.board[0][0] == None):
                    box = self.find_box(0, 0)            
         
                
        Grid.find_AI_rect(box[0])
        AI_Player.StartCoor = box[1], box[2]
    
    
    
    def AI_analyze(self):
        """ Checks for potentail win or counter move. Uses available moves 
        to determine if postion will result in winner for AI or user.
        """
        #Checks for potential win at available move
        for move in self.get_moves():
            cpu = self.add_to_copy(move[0], move[1], 1)
            
            if check_for_win_H(cpu) == 'PLAYER X WINS!' or check_for_win_V(cpu) == 'PLAYER X WINS!' or check_for_win_D(cpu) == 'PLAYER X WINS!':
                box = self.find_box(move[0], move[1])
                Grid.find_AI_rect(box[0])
                return True
        
        #Checks for counter move
        for move in self.get_moves():  
            player = self.add_to_copy(move[0], move[1], 0)
            
            if check_for_win_H(player) == 'PLAYER O WINS!' or check_for_win_V(player) == 'PLAYER O WINS!' or check_for_win_D(player) == 'PLAYER 0 WINS!':
                box = self.find_box(move[0], move[1])
                Grid.find_AI_rect(box[0])
                return True   
        
        
    def AI_open_spot(self):
        """Finds first available spot on board (Uses break to just iterate once).
        """
        for move in self.get_moves(): 
            box = self.find_box(move[0], move[1])
            Grid.find_AI_rect(box[0]) 
            break
    
    
    def AI_attack(self):
        """ Controls AI players moves.
        """
        if Grid.count == 2:
            self.AI_corners(AI_Player.StartCoor)
        elif Grid.count == 4:
            a = self.AI_analyze()
            if a == None:
                self.AI_corners(AI_Player.StartCoor)
        elif Grid.count == 6 or Grid.count == 8:
            a = self.AI_analyze()
            if a == None:
                self.AI_open_spot()            
          