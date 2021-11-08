

import tkinter as tk
from tkinter import filedialog, Text
import os
from functools import partial

#                               CREATION OF THE ROOT, GRID AND TEXT



root=tk.Tk()

root.title('SOS Game')
root.geometry('1000x600')

# choosing the grid size
col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=20)

    # labels for the players 


Player1=tk.Label(root,text="Blue Player:")
Player1.grid(row=0,column=0 ,sticky='NESW')

Player2=tk.Label(root,text="Red Player:")
Player2.grid(row=0,column=12 ,sticky='NESW')

Gamelabel=tk.Label(root,text="Game Type:")
Gamelabel.grid(row=0,column=1 ,sticky='NESW')

turnlabel=tk.Label(root,text="Current Turn:")
turnlabel.grid(row=10, column=1,columnspan=2, sticky='NESW')

sizelabel=tk.Label(root,text="Board Size")
sizelabel.grid(row=10, column=6, sticky='NESW')

#  TURN COUNTER AND CHANGE TURN FUNCTION



currentturn=tk.StringVar()


RB=int(0)

def changeturn():
   global RB
   global button_free
   #buttonbool=button([i][j])
   if RB % 2 ==0 and button_free==True:
    currentturn.set("Blue Player")
    RB+=1
    
   elif RB % 2 ==1 and button_free==False:
    currentturn.set("Red Player")
    RB+=1
    
    


turntext=tk.Label(root,textvariable=currentturn)
turntext.grid(row=10, column=3)











         




# Game type selection

Gametype=tk.IntVar()

Simplegame=tk.Radiobutton(root, text='Simple Game', variable=Gametype, value=1, bg="white")


Simplegame.grid(row=0,column=2 ,sticky='NESW')

Generalgame=tk.Radiobutton(root, text='General Game', variable=Gametype, value=2, bg="white")


Generalgame.grid(row=0, column=3 ,sticky='NESW')


#                                    BLUE PLAYER SELECTIONS



Blueplayer=tk.IntVar()    #declares the selection as an integer value

Humanblue=tk.Radiobutton(root, text='Human', variable=Blueplayer, value =1, bg="white") #creates the button to select human


Humanblue.grid(row=1, column=0 ,sticky='NESW') #adjust location on button 


Computerblue=tk.Radiobutton(root, text='Computer', variable=Blueplayer, value =2, bg="white") #creates the button to select computer


Computerblue.grid(row=2, column=0 ,sticky='NESW') #adjust location of button


Blueletter=tk.IntVar()    #declares the selection as an integer value

BlueS=tk.Radiobutton(root, text='S', variable=Blueletter, value =1, bg="white") #creates the button to select S for blue


BlueS.grid(row=3, column=0 ,sticky='NESW') #adjust location on button 


BlueO=tk.Radiobutton(root, text='O', variable=Blueletter, value =2, bg="white") #creates the button to select O for blue


BlueO.grid(row=4,column=0 ,sticky='NESW') #adjust location of button


#                                               RED PLAYER SELECTIONS


Redplayer=tk.IntVar()    #declares the selection as an integer value

Humanred=tk.Radiobutton(root, text='Human', variable=Redplayer, value =1, bg="white") #creates the button to select human


Humanred.grid(row=1, column=12 ,sticky='NESW') #adjust location on button 


Computerred=tk.Radiobutton(root, text='Computer', variable=Redplayer, value =2, bg="white") #creates the button to select computer


Computerred.grid(row=2, column=12 ,sticky='NESW') #adjust location of button


Redletter=tk.IntVar()    #declares the selection as an integer value

RedS=tk.Radiobutton(root, text='S', variable=Redletter, value =1, bg="white") #creates the button to select S for blue


RedS.grid(row=3, column=12 ,sticky='NESW') #adjust location on button 


RedO=tk.Radiobutton(root, text='O', variable=Redletter, value =2, bg="white") #creates the button to select O for blue


RedO.grid(row=4, column=12 ,sticky='NESW') #adjust location of button




#                                         NEW GAME AND REPLAY BUTTON IMPLEMENTATION


replaybutton = tk.Button(root, text= 'Replay', width =10, height=1) # replay button gui
replaybutton.grid(row=9,column=12 ,sticky='NESW')



      





ButtonChange=tk.StringVar()


boardsize= tk.Entry(root,width=5)
boardsize.grid(row=10, column =9 , stick='NESW')


def gameboard_create():
   global size
   size=int(boardsize.get())
   if size>2:
    
    
    
    global  board
    board = []
    for i in range(size):
        m= i+2
        board.append(i)
        board[i]=[]
        for j in range(size):
            n=j+1
            board[i].append(j)
            board[i][j]=tk.Button(root,width=10,height=5,text='',command=partial(Update_SOB0,i,j,currentturn,Blueletter,Blueplayer,Redletter,Redplayer,checksos,Gametype))
            board[i][j].grid(row=m,column=n)
   elif size <= 2 :
    print("Board size must be greater then 2")
   elif size =='':
       print("Board size can't be null")

         


newgamebutton = tk.Button(root, text= 'New Game', width =10, height=1, command=gameboard_create) # new game button gui
newgamebutton.grid(row=10,column=12 ,sticky='NESW')


def popup_win(currentturn):
    Winner=currentturn.get()
    win=tk.Toplevel(root)
    #popup_win.tkraise(root)
    win.title("Winner")
    tk.Label(win,text= Winner + " is the winner!").pack(side="top", fill="x")
    #tk.Button(win,text="Okay",command=popup_win.destroy).pack()




def checksos(i,j,Gametype,currentturn,Redplayer,Blueplayer):
    w = len(board[i])
    h = len(board[j])
    blucnt=(board[i])
    redcnt=(board[i])

    
    draw=0
    
    # Check for horizontals.
    
    for row in board:
        s = ''.join([cell['text'] for cell in row])
        if 'SOS' in s:
            print("found horizontal sos")
            if Gametype.get()==1:
                popup_win(currentturn)
            #elif Gametype.get()==2 and Blueplayer.get()==1 and currentturn.get()== "Blue Player":
            #    next(blucnt)
            #    print(blucnt)
                
                
            #elif Gametype.get()==2 and Redplayer.get()==1 and currentturn.get()== "Red Player":
            #    next(redcnt)               
            #    print(redcnt)
              
                

                
                
        
    # Check for verticals.

    for col in range(w):
        s = ''.join([board[i][col]['text'] for i in range(h)])
        if 'SOS' in s:
            print("found vertical sos")
            if Gametype.get()==1:
                popup_win(currentturn)
            #elif Gametype.get()==2 and Blueplayer.get()==1 and currentturn.get()== "Blue Player":
            #    blucnt+=1
            #    print("blue count is " + blucnt)
            #elif Gametype.get()==2 and Redplayer.get()==1 and currentturn.get()== "Red Player":
            #    redcnt +=1
            #    print("red count is" + redcnt)
      
    # Check for diagonals.  There are N-2 diagonals in each direction;
    # the outermost 2 are too short to hold SOS.

    for offset in range(0,w-2):
        # Start from the top and go SE.  If offset is 1, the
        # first string gets 1,0 then 2,1 then 3,2; the other
        # string gets 0,1 then 1,2 then 2,3.
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        for i in range(0,w-offset):
            s1.append( board[i+offset][i]['text'] )
            s2.append( board[i][i+offset]['text'] )
            s3.append( board[i+offset][w-i-1]['text'] )
            s4.append( board[h-i-1][i+offset]['text'] )
        if 'SOS' in ''.join(s1) or 'SOS' in ''.join(s2) or \
           'SOS' in ''.join(s3) or 'SOS' in ''.join(s4):
            print("found diagonal sos")
            if Gametype.get()==1:
                popup_win(currentturn)
            #elif Gametype.get()==2 and Blueplayer.get()==1 and currentturn.get()== "Blue Player":
            #    blucnt+=1
            #    print("blue count is" + blucnt)
            #elif Gametype.get()==2 and Redplayer.get()==1 and currentturn.get()== "Red Player":
            #    redcnt +=1
            #    print("red count is " + redcnt)
      


        



button_free = True
changeturn()
def Update_SOB0(i,j,currentturn,Blueletter,Blueplayer,Redletter,Redplayer,checksos,Gametype):
    global button_free
    buttontext=(board[i][j]) 
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and button_free==True and buttontext["text"]=='':
        buttontext.configure(text='S')
        button_free= False
        
        checksos(i,j,Gametype,currentturn,Redplayer,Blueplayer)
        changeturn()
        
    elif currentturn.get() =="Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and button_free==True and buttontext["text"]=='':
        buttontext.configure(text='O')
        button_free= False
        
        checksos(i,j,Gametype,currentturn,Redplayer,Blueplayer)
        changeturn()
       
    elif currentturn.get() =="Red Player" and Redletter.get()==1 and Redplayer.get()==1 and button_free==False and buttontext["text"]=='':
        buttontext.configure(text='S')
        button_free= True
        
        checksos(i,j,Gametype,currentturn,Redplayer,Blueplayer)
        changeturn()

    elif currentturn.get() =="Red Player" and Redletter.get()==2 and Redplayer.get()==1 and button_free==False and buttontext["text"]=='':
        buttontext.configure(text='O')
        button_free= True
        
        checksos(i,j,Gametype,currentturn,Redplayer,Blueplayer)
        changeturn()
















root.mainloop()






