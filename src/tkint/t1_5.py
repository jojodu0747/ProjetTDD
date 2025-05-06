#Effet de Sticky sur les 2 Pads

from tkinter import *

root=Tk()
root.title("t1_5")

a=Label(root, text="A", bg='red', width=20, height=5, padx=50)
a.grid(row=0, column=0, sticky=E+W)

b=Label(root, text="B", bg='lightblue', width=10)
b.grid(row=0, column=1, sticky=E+W, padx=50)

c=Label(root, text="C", bg='lime',  height=5)
c.grid(row=1, column=0, sticky=E+W)

d=Label(root, text="D", bg='orange', width=5, height=2)
d.grid(row=1, column=1, sticky=E+W)

root.mainloop()
