#Pad hors labels

from tkinter import *

root=Tk()
root.title("t1_2")

a=Label(root, text="A", bg='red', width=20, height=5)
b=Label(root, text="B", bg='lightblue', width=20, height=5)
c=Label(root, text="C", bg='lime', width=30, height=5)
d=Label(root, text="D", bg='orange', width=20, height=5)

a.grid(row=0, column=0, padx=50)
b.grid(row=0, column=1)
c.grid(row=1, column=0)
d.grid(row=1, column=1, pady=50)


root.mainloop()
