from tkinter import *

root=Tk()

def tab1():
    frame1.lift()

def tab2():
    frame2.lift()

frame1=Frame(root, bg="#ff0000")
bouton1=Button(frame1, text="P1", width=10, height=4, command=tab2)
bouton1.pack(side=RIGHT)

frame2=Frame(root, bg="#00ff00")
bouton2=Button(frame2, text="P2", width=10, height=4, command=tab1)
bouton2.pack(side=LEFT)

frame2.place(x=0, y=0, relwidth=1, relheight=1)
frame1.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()
