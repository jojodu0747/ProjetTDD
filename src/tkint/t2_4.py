#Expand

from tkinter import *

root = Tk()
root.title("t2_4")

a=Label(root, text="A", bg='#ff0000', width=20, height=5)
b=Label(root, text="B", bg='#00ff00', width=30, height=7)
c=Label(root, text="C", bg='#0000ff', width=5, height=1)
d=Label(root, text="D", bg='#ffff00', width=50, height=6)
e=Label(root, text="E", bg='#00ffff', width=20, height=5)
f=Label(root, text="F", bg='#ff00ff', width=10, height=10)

a.pack()
b.pack(expand=True)
c.pack()
d.pack(side=RIGHT)
e.pack(side=RIGHT, expand=True)
f.pack(side=RIGHT)

root.mainloop()
