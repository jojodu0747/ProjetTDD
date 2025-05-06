import tkinter as tk

def on_enter(event):
    event.widget.config(bg="#1E90FF", cursor="hand1")  # couleur hover + curseur main

def on_leave(event):
    event.widget.config(bg="#4682B4")  # couleur normale

def on_click():
    print("Bouton cliqué !")

root = tk.Tk()
root.title("Bouton Label stylé")

# Création du "bouton"
label_button = tk.Label(
    root,
    text="OK",
    bg="#4682B4",          # couleur normale
    fg="white",
    font=("Arial", 16, "bold"),
    width=10,
    height=2
)

label_button.pack(padx=20, pady=20)

# Lier les événements
label_button.bind("<Enter>", on_enter)
label_button.bind("<Leave>", on_leave)
label_button.bind("<Button-1>", lambda event: on_click())

root.mainloop()
