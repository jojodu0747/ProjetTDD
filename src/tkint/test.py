import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple de Scrollbar")

# Canvas pour contenir des widgets
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)


frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")


# Ajouter du contenu dans le frame
for i in range(50):  # Exemple avec 50 labels
    label = tk.Label(frame, text=f"Label {i+1}")
    label.pack()

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Lancer la boucle principale de l'application
root.mainloop()
