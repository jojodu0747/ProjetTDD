#Grid

from tkinter import *


root = Tk()
root.geometry("400x400")
root.minsize(400, 400)
root.title("t1_0")
root.config(background="#ff0000")
root.grid_columnconfigure(index=0, pad=50, minsize=400)
root.grid_rowconfigure(0, pad=50)
root.grid_rowconfigure(1, pad=10)

label1 = Label(root,
              text="Quoicoubeh",bg="#00ffff", fg="#000000",
              anchor=CENTER, width=20, height=5)
label2 = Label(root,
              text="Quoicoubeh", bg="#ffff00", fg="#000000",
              anchor=S, width=20, height=5)
label3 = Label(root,
              text="Quoicoubeh", bg="#0000ff", fg="#000000",
              anchor=E, width=20, height=5)
label4 = Label(root,
              text="Quoicoubeh", bg="#00ff00", fg="#000000",
              anchor=W, width=20, height=5)
cv = Canvas(root, width=300, height=20, bg="#0000ff")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=0, column=1)
label4.grid(row=1, column=1)
cv.grid(row=2, column=0)

root.mainloop()
