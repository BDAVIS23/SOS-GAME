

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

    # labels for the players 


PlayerL1=tk.Label(root,text="Blue Player:")
PlayerL1.grid(row=0,column=0 ,sticky='NESW')

PlayerL2=tk.Label(root,text="Red Player:")
PlayerL2.grid(row=0,column=12 ,sticky='NESW')

Gamelabel=tk.Label(root,text="Game Type:")
Gamelabel.grid(row=0,column=1 ,sticky='NESW')

turnlabel=tk.Label(root,text="Current Turn:")
turnlabel.grid(row=10, column=1,columnspan=2, sticky='NESW')



#  TURN COUNTER AND CHANGE TURN FUNCTION



currentturn=tk.StringVar()


RB=int(0)

def changeturn():
   global RB
   if RB % 2 ==0:
    currentturn.set("Blue Player")
    RB+=1
   elif RB % 2 ==1:
    currentturn.set("Red Player")
    RB+=1
    
changeturn()

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

newgamebutton = tk.Button(root, text= 'New Game', width =10, height=1) # new game button gui
newgamebutton.grid(row=10,column=12 ,sticky='NESW')







#                                       Game Board Buttons

#Button Change 
ButtonChange0=tk.StringVar()
def Update_SOB0():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange0.get()=='':
        ButtonChange0.set('S')
        changeturn()
        
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange0.get()=='':
         ButtonChange0.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange0.get()=='':
        ButtonChange0.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange0.get()=='':
      ButtonChange0.set('O')
      changeturn()
      

ButtonChange1=tk.StringVar()

def Update_SOB1():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange1.get()=='':
        ButtonChange1.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange1.get()=='':
         ButtonChange1.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange1.get()=='':
        ButtonChange1.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange1.get()=='':
      ButtonChange1.set('O')
      changeturn()





    
      
ButtonChange2=tk.StringVar()

def Update_SOB2():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange2.get()=='':
        ButtonChange2.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange2.get()=='':
         ButtonChange2.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange2.get()=='':
        ButtonChange2.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange2.get()=='':
      ButtonChange2.set('O')
      changeturn()





ButtonChange3=tk.StringVar()


def Update_SOB3():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange3.get()=='':
        ButtonChange3.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange3.get()=='':
         ButtonChange3.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange3.get()=='':
        ButtonChange3.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange3.get()=='':
      ButtonChange3.set('O')
      changeturn()


ButtonChange4=tk.StringVar()

def Update_SOB4():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange4.get()=='':
        ButtonChange4.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange4.get()=='':
         ButtonChange4.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange4.get()=='':
        ButtonChange4.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange4.get()=='':
      ButtonChange4.set('O')
      changeturn()





ButtonChange5=tk.StringVar()
def Update_SOB5():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange5.get()=='':
        ButtonChange5.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange5.get()=='':
         ButtonChange5.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange5.get()=='':
        ButtonChange5.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange5.get()=='':
      ButtonChange5.set('O')
      changeturn()





ButtonChange6=tk.StringVar()
def Update_SOB6():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange6.get()=='':
        ButtonChange6.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange6.get()=='':
         ButtonChange6.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange6.get()=='':
        ButtonChange6.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange6.get()=='':
      ButtonChange6.set('O')
      changeturn()






ButtonChange7=tk.StringVar()
def Update_SOB7():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange7.get()=='':
        ButtonChange7.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange7.get()=='':
         ButtonChange7.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange7.get()=='':
        ButtonChange7.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange7.get()=='':
      ButtonChange7.set('O')
      changeturn()





ButtonChange8=tk.StringVar()
def Update_SOB8():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange8.get()=='':
        ButtonChange8.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange8.get()=='':
         ButtonChange8.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange8.get()=='':
        ButtonChange8.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange8.get()=='':
      ButtonChange8.set('O')
      changeturn()





ButtonChange9=tk.StringVar()
def Update_SOB9():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange9.get()=='':
        ButtonChange9.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange9.get()=='':
         ButtonChange9.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange9.get()=='':
        ButtonChange9.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange9.get()=='':
      ButtonChange9.set('O')
      changeturn()






ButtonChange10=tk.StringVar()
def Update_SOB10():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange10.get()=='':
        ButtonChange10.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange10.get()=='':
         ButtonChange10.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange10.get()=='':
        ButtonChange10.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange10.get()=='':
      ButtonChange10.set('O')
      changeturn()





ButtonChange11=tk.StringVar()
def Update_SOB11():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange11.get()=='':
        ButtonChange11.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange11.get()=='':
         ButtonChange11.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange11.get()=='':
        ButtonChange11.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange11.get()=='':
      ButtonChange11.set('O')
      changeturn()





ButtonChange12=tk.StringVar()
def Update_SOB12():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange12.get()=='':
        ButtonChange12.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange12.get()=='':
         ButtonChange12.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange12.get()=='':
        ButtonChange12.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange12.get()=='':
      ButtonChange12.set('O')
      changeturn()





ButtonChange13=tk.StringVar()
def Update_SOB13():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange13.get()=='':
        ButtonChange13.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange13.get()=='':
         ButtonChange13.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange13.get()=='':
        ButtonChange13.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange13.get()=='':
      ButtonChange13.set('O')
      changeturn()






ButtonChange14=tk.StringVar()
def Update_SOB14():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange14.get()=='':
        ButtonChange14.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange14.get()=='':
         ButtonChange14.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange14.get()=='':
        ButtonChange14.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange14.get()=='':
      ButtonChange14.set('O')
      changeturn()




ButtonChange15=tk.StringVar()
def Update_SOB15():
    if currentturn.get() =="Blue Player" and Blueletter.get()==1 and Blueplayer.get()==1 and ButtonChange15.get()=='':
        ButtonChange15.set('S')
        changeturn()
    elif currentturn.get() == "Blue Player" and Blueletter.get()==2 and Blueplayer.get()==1 and ButtonChange15.get()=='':
         ButtonChange15.set('O')
         changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==1 and Redplayer.get()==1 and ButtonChange15.get()=='':
        ButtonChange15.set('S')
        changeturn()
    elif currentturn.get() == "Red Player" and Redletter.get()==2 and Redplayer.get()==1 and ButtonChange15.get()=='':
      ButtonChange15.set('O')
      changeturn()




# Buttons





# Row 1




B0=tk.Button(root,textvariable=ButtonChange0, width=10, height=5, command=Update_SOB0)
B0.grid(row=2, column=1, sticky='NESW')

B1=tk.Button(root,textvariable=ButtonChange1, width=10, height=5, command=Update_SOB1)
B1.grid(row=2, column=2 ,sticky='NESW')

B2=tk.Button(root,textvariable=ButtonChange2, width=10, height=5, command=Update_SOB2)
B2.grid(row=2, column=3 ,sticky='NESW')

B3=tk.Button(root,textvariable=ButtonChange3, width=10, height=5, command=Update_SOB3)
B3.grid(row=2, column=4 ,sticky='NESW')

# Row 2

B4=tk.Button(root,textvariable=ButtonChange4, width=10, height=5, command=Update_SOB4)
B4.grid(row=3, column=1 ,sticky='NESW')

B5=tk.Button(root,textvariable=ButtonChange5, width=10, height=5, command=Update_SOB5)
B5.grid(row=3, column=2 ,sticky='NESW')

B6=tk.Button(root,textvariable=ButtonChange6, width=10, height=5, command=Update_SOB6)
B6.grid(row=3, column=3 ,sticky='NESW')

B7=tk.Button(root,textvariable=ButtonChange7, width=10, height=5, command=Update_SOB7)
B7.grid(row=3, column=4 ,sticky='NESW')

# Row 3

B8=tk.Button(root,textvariable=ButtonChange8, width=10, height=5, command=Update_SOB8)
B8.grid(row=4, column=1 ,sticky='NESW')

B9=tk.Button(root,textvariable=ButtonChange9, width=10, height=5, command=Update_SOB9)
B9.grid(row=4, column=2 ,sticky='NESW')

B10=tk.Button(root,textvariable=ButtonChange10, width=10, height=5, command=Update_SOB10)
B10.grid(row=4, column=3 ,sticky='NESW')

B11=tk.Button(root,textvariable=ButtonChange11, width=10, height=5, command=Update_SOB11)
B11.grid(row=4, column=4 ,sticky='NESW')

# Row 4

B12=tk.Button(root,textvariable=ButtonChange12, width=10, height=5, command=Update_SOB12)
B12.grid(row=4, column=1 ,sticky='NESW')

B13=tk.Button(root,textvariable=ButtonChange13, width=10, height=5, command=Update_SOB13)
B13.grid(row=4, column=2 ,sticky='NESW')

B14=tk.Button(root,textvariable=ButtonChange14, width=10, height=5, command=Update_SOB14)
B14.grid(row=4, column=3 ,sticky='NESW')

B15=tk.Button(root,textvariable=ButtonChange15, width=10, height=5, command=Update_SOB15)
B15.grid(row=4, column=4 ,sticky='NESW')




root.mainloop()




