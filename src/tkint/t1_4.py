#Sticky

from tkinter import *

root=Tk()
root.title("t1_4")

a=Label(root, text="A", bg='red', width=20, height=5)
a.grid(row=0, column=0)

b=Label(root, text="B", bg='lightblue', width=10)
b.grid(row=0, column=1, sticky=N)

c=Label(root, text="C", bg='lime',  height=5)
c.grid(row=1, column=0, sticky=E+W)

d=Label(root, text="D", bg='orange', width=5, height=2)
d.grid(row=1, column=1, sticky=NE)

root.mainloop()
