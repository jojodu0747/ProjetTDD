from tkinter import *

root = Tk()
root.title("t3")
root.geometry("400x400")
root.config(bg="#ffffff")

a= Frame(root, bg="#ff0000")
b= Label(a, text="A", bg="#00ff00")

a.place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.25)
b.pack()

root.mainloop()
