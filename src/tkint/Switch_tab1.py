from tkinter import *

root=Tk()
root.title("switch2")

def efface(window):
    for widget in window.winfo_children():
        print(widget)
        if isinstance(widget, Frame):
            efface(widget)
        widget.destroy()
        del widget

def tab1():
    efface(root)
    frame1=Frame(root, bg="#ff0000")
    frame2=Frame(frame1, bg="#00ff00", padx=20)
    bouton1=Button(frame1, text="P1", width=10, height=4, command=tab2)
    label1=Label(frame2, text="Tab1", bg="#ff0000")
    frame1.place(x=0, y=0, relwidth=1, relheight=1)
    frame2.pack()
    bouton1.pack(side=RIGHT)
    label1.pack()



def tab2():
    efface(root)
    frame1 = Frame(root, bg="#00ff00")
    bouton1=Button(frame1, text="P2", width=10, height=4, command=tab1)
    frame1.place(x=0, y=0, relwidth=1, relheight=1)
    bouton1.pack(side=LEFT)


tab1()

root.mainloop()
