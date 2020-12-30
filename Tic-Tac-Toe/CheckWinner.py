from createText import create_text

#Checks For Horizontal Win
def check_for_win_H(lst):
    a = set()
          
    for elem in lst:
        for i in range(3):
            a.add(elem[i])
        
        if len(a) == 1 and None not in a:    
            if 0 in a:
                return 'PLAYER O WINS!'
            else:
                return 'PLAYER X WINS!'
        else:
            a = set()

#Checks for Vertical Win            
def check_for_win_V(lst):
    a = set()
    
    for x in range(3):
        for y in range(3):
            a.add(lst[y][x])
         
        if len(a) == 1 and None not in a:   
            if 0 in a:
                return 'PLAYER O WINS!'
            else:
                return 'PLAYER X WINS!'
        else:
            a = set()

#Checks For Diagonal Win
def check_for_win_D(lst):
    if lst[0][0] == lst[1][1] == lst[2][2] and lst[0][0] != None:
        if lst[0][0] == 0:
            return 'PLAYER O WINS!'
        else:
            return 'PLAYER X WINS!'
    
    elif lst[0][2] == lst[1][1] == lst[2][0] and lst[0][2] != None:
        if lst[0][2] == 0:
            return 'PLAYER O WINS!'
        else:
            return 'PLAYER X WINS!'        

#Gets Winner    
def Winner_text(h, v, d, count):
    if h != None:
        return h
    if v != None:
        return v
    if d != None:
        return d
    elif count == 9:
        return 'YOU TIED!'
    
     
    