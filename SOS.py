
import tkinter as tk
from tkinter import filedialog, Text
import os


#                               CREATION OF THE ROOT, CANVAS AND TEXT



root=tk.Tk()

root.title('SOS Game')
root.geometry('800x800')

canvas = tk.Canvas(root, height=700, width=700, bg="white" ) #creation of the background for the game
canvas.place(x=50, y=50)
canvas.create_text(250,60, text= "SOS", fill="black") # text label for the type of game

canvas.create_text(100,200, text="Blue Player" , fill="black" ) # text label for blue player

canvas.create_text(600,200, text="Red Player" , fill="black" )  # text label for red player

canvas.create_text(250,615, text="Current Turn:" , fill="black" ) #text label for whose turn it currently is





#                                     GAME TYPE SELECTION

Gametype=tk.IntVar()
Simplegame=tk.Radiobutton(root, text='Simple Game', variable=Gametype, value=1, bg="white")
Simplegame.pack()

Simplegame.place(x=325, y=100)

Generalgame=tk.Radiobutton(root, text='General Game', variable=Gametype, value=2, bg="white")
Generalgame.pack()

Generalgame.place(x=425, y=100)


 
#                                    BLUE PLAYER SELECTIONS



Blueplayer=tk.IntVar()    #declares the selection as an integer value

Humanblue=tk.Radiobutton(root, text='Human', variable=Blueplayer, value =1, bg="white") #creates the button to select human
Humanblue.pack()

Humanblue.place(x=105,y=275) #adjust location on button 


Computerblue=tk.Radiobutton(root, text='Computer', variable=Blueplayer, value =2, bg="white") #creates the button to select computer
Computerblue.pack()

Computerblue.place(x=105,y=400) #adjust location of button


Blueletter=tk.IntVar()    #declares the selection as an integer value

BlueS=tk.Radiobutton(root, text='S', variable=Blueletter, value =1, bg="white") #creates the button to select S for blue
BlueS.pack()

BlueS.place(x=105,y=300) #adjust location on button 


BlueO=tk.Radiobutton(root, text='O', variable=Blueletter, value =2, bg="white") #creates the button to select O for blue
BlueO.pack()

BlueO.place(x=105,y=325) #adjust location of button


#                                               RED PLAYER SELECTIONS


Redplayer=tk.IntVar()    #declares the selection as an integer value

Humanred=tk.Radiobutton(root, text='Human', variable=Redplayer, value =1, bg="white") #creates the button to select human
Humanred.pack()

Humanred.place(x=615,y=275) #adjust location on button 


Computerred=tk.Radiobutton(root, text='Computer', variable=Redplayer, value =2, bg="white") #creates the button to select computer
Computerred.pack()

Computerred.place(x=615,y=400) #adjust location of button


Redletter=tk.IntVar()    #declares the selection as an integer value

RedS=tk.Radiobutton(root, text='S', variable=Redletter, value =1, bg="white") #creates the button to select S for blue
RedS.pack()

RedS.place(x=615,y=300) #adjust location on button 


RedO=tk.Radiobutton(root, text='O', variable=Redletter, value =2, bg="white") #creates the button to select O for blue
RedO.pack()

RedO.place(x=615,y=325) #adjust location of button



Recordgame=tk.IntVar()
Record=tk.Checkbutton(root,text='Record Game', variable=Recordgame, bg="white")
Record.place(x=105,y=650)


#                                      GAME BOX CREATION

## Vertical lines

canvas.create_rectangle(200,200,500,500)
canvas.create_line(230,200,230,500)
canvas.create_line(260,200,260,500)
canvas.create_line(290,200,290,500)
canvas.create_line(320,200,320,500)
canvas.create_line(350,200,350,500)
canvas.create_line(380,200,380,500)
canvas.create_line(410,200,410,500)
canvas.create_line(440,200,440,500)
canvas.create_line(470,200,470,500)
canvas.create_line(500,200,500,500)

## Horizontal lines


canvas.create_line(200,230,500,230)
canvas.create_line(200,260,500,260)
canvas.create_line(200,290,500,290)
canvas.create_line(200,320,500,320)
canvas.create_line(200,350,500,350)
canvas.create_line(200,380,500,380)
canvas.create_line(200,410,500,410)
canvas.create_line(200,440,500,440)
canvas.create_line(200,470,500,470)
canvas.create_line(200,500,500,500)



#                                         NEW GAME AND REPLAY BUTTON IMPLEMENTATION


replaybutton = tk.Button(root, text= 'Replay', width =10, height=1) # replay button gui
replaybutton.place( x= 600, y= 650)

newgamebutton = tk.Button(root, text= 'New Game', width =10, height=1) # new game button gui
newgamebutton.place( x= 600, y= 680)



root.mainloop()
