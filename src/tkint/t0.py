#Taille

from tkinter import *

def update_label(event=None):
    label.config(width=root.winfo_width()//2, height=root.winfo_height()//2)

root = Tk()
root.geometry("400x300")
root.title("t0")
root.config(background="#ff0000")

label = Frame(root, bg="#00ff00")
label.pack(pady=20)


update_label()
root.bind("<Configure>", update_label)

root.mainloop()
