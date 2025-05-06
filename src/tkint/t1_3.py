#Span

from tkinter import *

root=Tk()
root.title("t1_3")

a=Label(root, text="A", bg='red', width=20, height=5)
a.grid(row=0, column=0)

b=Label(root, text="B", bg='lightblue', width=20, height=5)
b.grid(row=0, column=1)

x=Label(root, text="X", bg='gray', width=20, height=5)
x.grid(row=1, column=0,columnspan=2)

y=Label(root, text="X", bg='gray', width=20, height=5)
y.grid(row=0, column=2,rowspan=2)

c=Label(root, text="C", bg='lime', width=20, height=5)
c.grid(row=2, column=0)

d=Label(root, text="D", bg='orange', width=20, height=5)
d.grid(row=2, column=1)

root.mainloop()
