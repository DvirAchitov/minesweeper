"""
Student: Dvir Ahituv
ID: 315093641
Assignment no. 6
Program: minesweeper.py
"""


import random,sys

def zeros(x,y,HiddenBoard,GameBoard):
            """This Func open all the area around the opened 0 """
            """and open in recursion all the other 0's if have""" 
            if GameBoard[x][y]!=" ":
                return 
            GameBoard[x][y]=HiddenBoard[x][y]
            if isOutofBounds(x,y+1,len(HiddenBoard)):
                if HiddenBoard[x][y+1]==0 and GameBoard[x][y+1]==" ":
                    zeros(x,y+1,HiddenBoard,GameBoard)
                if HiddenBoard[x][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x][y+1]=HiddenBoard[x][y+1]
            if isOutofBounds(x,y-1,len(HiddenBoard)):
                 if HiddenBoard[x][y-1]==0 and GameBoard[x][y-1]==" ":
                     zeros(x,y-1,HiddenBoard,GameBoard)
                 if HiddenBoard[x][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x][y-1]=HiddenBoard[x][y-1]
            if isOutofBounds(x+1,y,len(HiddenBoard)):
                 if HiddenBoard[x+1][y]==0 and GameBoard[x+1][y]==" ":
                     zeros(x+1,y,HiddenBoard,GameBoard)
                 if HiddenBoard[x+1][y]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x+1][y]=HiddenBoard[x+1][y]
            if isOutofBounds(x+1,y-1,len(HiddenBoard)):
                 if HiddenBoard[x+1][y-1]==0 and GameBoard[x+1][y-1]==" ":
                     zeros(x+1,y-1,HiddenBoard,GameBoard)
                 if HiddenBoard[x+1][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x+1][y-1]=HiddenBoard[x+1][y-1]
            if isOutofBounds(x+1,y+1,len(HiddenBoard)):
                 if HiddenBoard[x+1][y+1]==0 and GameBoard[x+1][y+1]==" ":
                     zeros(x+1,y+1,HiddenBoard,GameBoard)
                 if HiddenBoard[x+1][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x+1][y+1]=HiddenBoard[x+1][y+1]
            if isOutofBounds(x-1,y+1,len(HiddenBoard)):
                 if HiddenBoard[x-1][y+1]==0 and GameBoard[x-1][y+1]==" ":
                     zeros(x-1,y+1,HiddenBoard,GameBoard)
                 if HiddenBoard[x-1][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x-1][y+1]=HiddenBoard[x-1][y+1]
            if isOutofBounds(x-1,y,len(HiddenBoard)):
                 if HiddenBoard[x-1][y]==0 and GameBoard[x-1][y]==" ":
                     zeros(x-1,y,HiddenBoard,GameBoard)
                 if HiddenBoard[x-1][y]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x-1][y]=HiddenBoard[x-1][y]
            if isOutofBounds(x-1,y-1,len(HiddenBoard)):
                 if HiddenBoard[x-1][y-1]==0 and GameBoard[x-1][y-1]==" ":
                     zeros(x-1,y-1,HiddenBoard,GameBoard) 
                 if HiddenBoard[x-1][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x-1][y-1]=HiddenBoard[x-1][y-1]
    
def isOutofBounds(x,y,n):
      """This Func check around the selected number if his area is illigal """
      """ and if we dont get out of the gameboard"""
      if x<0 or x>n-1:
          return False
      if y<0 or y>n-1:
          return False
      return True

def minesweeper(n,mines_sizes): 
    """This func throw random mines into our game board"""
    """And creat for us the first board to play"""
    HiddenBoard = [[0 for row in range(n)] for colum in range(n)]
    GameBoard =[[" " for row in range(len(HiddenBoard))] for colum in range(len(HiddenBoard))]  
    mines=list()
    i=0
    while i <mines_sizes:
        r=[random.randint(0, n-1),random.randint(0, n-1)]
        if r not in mines:
            mines.append(r)
            i+=1
    for i in range (0,len(mines)):
        HiddenBoard[mines[i][0]][mines[i][1]]='\x1b[1;37;41m' + 'x' + '\x1b[0m'
    for x in range(len(HiddenBoard)):
        for y in range(len(HiddenBoard)):
            if HiddenBoard[x][y]=='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                if isOutofBounds(x,y+1,len(HiddenBoard)):
                    if HiddenBoard[x][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                        HiddenBoard[x][y+1]+=1
                if isOutofBounds(x,y-1,len(HiddenBoard)):
                     if HiddenBoard[x][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x][y-1]+=1
                if isOutofBounds(x+1,y,len(HiddenBoard)):
                     if HiddenBoard[x+1][y]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x+1][y]+=1
                if isOutofBounds(x+1,y-1,len(HiddenBoard)):
                     if HiddenBoard[x+1][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x+1][y-1]+=1
                if isOutofBounds(x+1,y+1,len(HiddenBoard)):
                     if HiddenBoard[x+1][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x+1][y+1]+=1
                if isOutofBounds(x-1,y+1,len(HiddenBoard)):
                     if HiddenBoard[x-1][y+1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x-1][y+1]+=1
                if isOutofBounds(x-1,y,len(HiddenBoard)):
                     if HiddenBoard[x-1][y]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x-1][y]+=1
                if isOutofBounds(x-1,y-1,len(HiddenBoard)):
                     if HiddenBoard[x-1][y-1]!='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                         HiddenBoard[x-1][y-1]+=1

    for i in range(len(HiddenBoard)):
        print(" "+"+---"*len(HiddenBoard)+"+")
        print(i+1,end="|")
        print(" "+" | ".join(str(" ") for cell in HiddenBoard[i]),end=" |\n")        
    print(" "+"+---"*len(HiddenBoard)+"+") 
    print("   "+"   ".join(str(i+1) for i in range(n)))
    return HiddenBoard,GameBoard
    
def play(x,y,HiddenBoard,GameBoard,m):
    """This func its the play func' here we calculate all the cordinates"""
    """And we fill the gameboard with the choosen cordinates """
    """Also here we decide if the user win's / lose the game """
    if HiddenBoard[x][y]=='\x1b[1;37;41m' + 'x' + '\x1b[0m': # here we revealed all the mines if the user hit a mine and we stop the game as lose
        for x in range(len(HiddenBoard)):
            for y in range(len(HiddenBoard)):
                if HiddenBoard[x][y]=='\x1b[1;37;41m' + 'x' + '\x1b[0m':
                    GameBoard[x][y]=HiddenBoard[x][y]
        
        for i in range(len(GameBoard)):
            print(" "+"+---"*len(HiddenBoard)+"+")
            print(i+1,end="|")
            print(" "+" | ".join(str(cell) for cell in GameBoard[i]),end=" |\n")
        print(" "+"+---"*len(HiddenBoard)+"+") 
        print("   "+"   ".join(str(i+1) for i in range(len(HiddenBoard))))
        print(" __     __           _                           __")
        print(" \ \   / /          | |                     _   / /")
        print("  \ \_/ /__  _   _  | |     ___  ___  ___  (_) | | ")
        print("   \   / _ \| | | | | |    / _ \/ __|/ _ \     | | ")
        print("    | | (_) | |_| | | |___| (_) \__ \  __/  _  | | ")
        print("    |_|\___/ \__,_| |______\___/|___/\___| (_) | | ")
        print("                                                \_\\")

        sys.exit()   
    
    if HiddenBoard[x][y]!=0:          # Here we open the cordinate that the user choose if its not mine / "0"
        GameBoard[x][y]=HiddenBoard[x][y]
        for i in range(len(GameBoard)):
            print(" "+"+---"*len(HiddenBoard)+"+")
            print(i+1,end="|")
            print(" "+" | ".join(str(cell) for cell in GameBoard[i]),end=" |\n")
        print(" "+"+---"*len(HiddenBoard)+"+") 
        print("   "+"   ".join(str(i+1) for i in range(len(HiddenBoard))))    
   
    else:                          #if the user pick a cordinate with "0" here we calc the area around the "0" and we decide what cords to open
        zeros(x,y,HiddenBoard,GameBoard)
        
        for i in range(len(GameBoard)):
            print(" "+"+---"*len(HiddenBoard)+"+")
            print(i+1,end="|")
            print(" "+" | ".join(str(cell) for cell in GameBoard[i]),end=" |\n")
        print(" "+"+---"*len(HiddenBoard)+"+") 
        print("   "+"   ".join(str(i+1) for i in range(len(HiddenBoard))))
    counter=0
    for x in range(len(HiddenBoard)):   # here we check if the user win the game , else we tell the user to keep trying .
          for y in range(len(HiddenBoard)):
              if GameBoard[x][y]!=" ":
                  counter+=1
    if counter+m==len(HiddenBoard)*len(HiddenBoard[0]):
              print("           _                          _   _   _ ")
              print("          (_)                        | | | | | |")
              print("  __      ___ _ __  _ __   ___   __  | | | | | |")
              print("  \ \ /\ / / | '_ \| '_ \ / _ \/'__| | | | | | |")
              print("   \ V  V /| | | | | | | |  __/ |    |_| |_| |_|")
              print("    \_/\_/ |_|_| |_|_| |_|\___|_|    (_) (_) (_)")
                                                                          
              sys.exit() 

    print(" +-+-+-+-+ +-+-+-+-+-+-+")
    print(" |k|e|e|p| |t|r|y|i|n|g|")
    print(" +-+-+-+-+ +-+-+-+-+-+-+")
    
def main():
    check=False
    while check==False:
        try:
            x=int(input('enter a size: '))
            if x<=0:
                print("\nbad size try again")
                continue
            m=int(input('enter number of mines (No more twice the row size): '))   
            if m<=0:
                print("\nmines ammount cannot be a 0 or less please try again")
                continue
            if x*2<m:
                print("\nbad mines ammount try again")
                continue
        except ValueError:
            print('\nthis is not a integer')
            continue           
        else:
            check=True
    game=minesweeper(x,m)
    while True:
        try:
           z=int(input('Please enter X cordinate '))
           if z>x or 1>z:
               print('\x1b[1;37;41m' + 'Bad X Cordinate' + '\x1b[0m')
               continue
           t=int(input('Please enter Y cordinate '))
           if t>x or 1>t:
               print('\x1b[1;37;41m' + 'Bad Y Cordinate' + '\x1b[0m')
               continue
        except ValueError:
            print('\x1b[1;37;41m' + 'this is not a integer' + '\x1b[0m')
            continue
        else:
            play(z-1,t-1,game[0],game[1],m)    
main()