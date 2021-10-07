

import tkinter as tk
from tkinter import filedialog, Text
import os


#                               CREATION OF THE ROOT, GRID AND TEXT



root=tk.Tk()

root.title('SOS Game')
root.geometry('525x400')
f=tk.Frame(root)
# choosing the grid size
col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=20)

    # labels for the players and game

PlayerL1=tk.Label(root,text="Blue Player:")
PlayerL1.grid(row=0,column=0 ,sticky='NESW')

PlayerL2=tk.Label(root,text="Red Player:")
PlayerL2.grid(row=0,column=12 ,sticky='NESW')

Gamelabel=tk.Label(root,text="Game Type:")
Gamelabel.grid(row=0,column=1 ,sticky='NESW')

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

newgamebutton = tk.Button(root, text= 'New Game', width =10, height=1) # new game button gui
newgamebutton.grid(row=10,column=12 ,sticky='NESW')

#                                       Game Board Buttons

# Row 1

B0=tk.Button(root,text=" ", width=10, height=5)
B0.grid(row=2, column=1, sticky='NESW')

B1=tk.Button(root,text=" ", width=10, height=5)
B1.grid(row=2, column=2 ,sticky='NESW')

B2=tk.Button(root,text=" ", width=10, height=5)
B2.grid(row=2, column=3 ,sticky='NESW')

B3=tk.Button(root,text=" ", width=10, height=5)
B3.grid(row=2, column=4 ,sticky='NESW')

# Row 2

B0=tk.Button(root,text=" ", width=10, height=5)
B0.grid(row=3, column=1 ,sticky='NESW')

B1=tk.Button(root,text=" ", width=10, height=5)
B1.grid(row=3, column=2 ,sticky='NESW')

B2=tk.Button(root,text=" ", width=10, height=5)
B2.grid(row=3, column=3 ,sticky='NESW')

B3=tk.Button(root,text=" ", width=10, height=5)
B3.grid(row=3, column=4 ,sticky='NESW')

# Row 3

B0=tk.Button(root,text=" ", width=10, height=5)
B0.grid(row=4, column=1 ,sticky='NESW')

B1=tk.Button(root,text=" ", width=10, height=5)
B1.grid(row=4, column=2 ,sticky='NESW')

B2=tk.Button(root,text=" ", width=10, height=5)
B2.grid(row=4, column=3 ,sticky='NESW')

B3=tk.Button(root,text=" ", width=10, height=5)
B3.grid(row=4, column=4 ,sticky='NESW')

# Row 4

B0=tk.Button(root,text=" ", width=10, height=5)
B0.grid(row=4, column=1 ,sticky='NESW')

B1=tk.Button(root,text=" ", width=10, height=5)
B1.grid(row=4, column=2 ,sticky='NESW')

B2=tk.Button(root,text=" ", width=10, height=5)
B2.grid(row=4, column=3 ,sticky='NESW')

B3=tk.Button(root,text=" ", width=10, height=5)
B3.grid(row=4, column=4 ,sticky='NESW')


root.mainloop()




