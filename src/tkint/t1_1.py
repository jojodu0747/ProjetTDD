#Pad dans les labels

from tkinter import *


root = Tk()
root.geometry("420x420")
root.minsize(420, 420)
root.title("t1_1")
root.config(background="#ff0000")

label1 = Label(root,
              text="Quoicoubeh",bg="#00ffff", fg="#000000",
              anchor=CENTER, width=50, height=5, padx=40, pady=40)
label2 = Label(root,
              text="Quoicoubeh", bg="#ffff00", fg="#000000",
              anchor=S, width=50, height=5)
label3 = Label(root,
              text="Quoicoubeh", bg="#0000ff", fg="#000000",
              anchor=E, width=50, height=5)
label4 = Label(root,
              text="Quoicoubeh", bg="#00ff00", fg="#000000",
              anchor=W, width=50, height=5)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=0, column=1)
label4.grid(row=1, column=1)

root.mainloop()
