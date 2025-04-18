import tkinter as tk


root = tk.Tk()
root.title("ProjetTDD")
root.geometry("1280x720")
root.minsize(1280, 720)
root.configure(bg="#333333")


def event_change_couleur(event, couleur):
    event.widget.config(bg=couleur)


def efface(window):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            efface(widget)
        widget.destroy()
        del widget


def page_principale():
    efface(root)
    label1 = tk.Label(root,
                      text="Par Aziz Seghaier, Joé Napolitano, Louis Stanisière,"
                      " Elliot Meriot",
                      font=("Arial", 14),
                      bg="#333333",
                      fg="#ffffff")
    label2 = tk.Label(root, text="Projet TDD: Jeux Olympique", font=("Arial", 40),
                      bg="#333333",
                      fg="#ffffff")
    frame1 = tk.Frame(root, bg="#4a4a4a", padx=5, pady=10,
                      borderwidth=3, relief="solid")
    bouton1 = tk.Label(frame1,
                       text="Q1: Déterminez le nombre de médailles gagnées par Michael"
                       " Phelps. Son nom complet est Michael Fred Phelps, II.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton2 = tk.Label(frame1,
                       text="Q2: Trouvez des bornes inférieures et supérieures pour "
                       "le nombre de médailles par nation pour les Jeux Olympiques"
                       " de 2016.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton3 = tk.Label(frame1,
                       text="Q3: Déterminer quelles sont les 5 premières nations qui"
                       " ont eu le plus de médaillés au saut en longueur en 200 ans.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton4 = tk.Label(frame1,
                       text="Q4: Déterminer l'âge moyen des médaillés d'or au JO"
                       " d'hiver et au JO d'été.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton5 = tk.Label(frame1,
                       text="Q5: Quel est la personne la plus et la plus moin agée"
                       " ayant eu une médaille d'or.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton6 = tk.Label(frame1,
                       text="Q6: Quelle est la moyenne d'age des femmes et hommes"
                       " médaillées aux Jeux Olympiques depuis leur création ?",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton7 = tk.Label(frame1,
                       text="Q7: Quelle est la répartition des médailles par continent"
                       " au jeux Olympiques de 2016?.",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton8 = tk.Label(frame1,
                       text="Q8: Identifier les pays qui ont le ratio nombre de"
                       " médailles gagnées par des femmes sur nombre de médailles"
                       " gagnées par"
                       "\n des hommes le plus haut/le plus bas?",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       justify="left",
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton9 = tk.Label(frame1,
                       text="Q9: Comment le taux de participation des femmes aux Jeux"
                       " Olympiques a-t-elle évolué au fil du temps ?",
                       bg="#333333",
                       fg="#ffffff",
                       font=("Arial", 20),
                       anchor="w",
                       height=2,
                       borderwidth=3,
                       relief="solid",
                       padx=5,
                       pady=5)
    bouton10 = tk.Label(frame1,
                        text="Q10: Quel sont les sports où la France a gagné le plus"
                        " de médaille ?",
                        bg="#333333",
                        fg="#ffffff",
                        font=("Arial", 20),
                        anchor="w",
                        height=2,
                        borderwidth=3,
                        relief="solid",
                        padx=5,
                        pady=5)
    label1.pack(anchor=tk.W)
    label2.pack(pady=25)
    frame1.pack(expand=True)
    for widget in frame1.winfo_children():
        widget.pack(pady=2, fill="both")
        widget.bind("<Enter>", lambda event: event_change_couleur(event, "#4a4a4a"))
        widget.bind("<Leave>", lambda event: event_change_couleur(event, "#333333"))
    bouton1.bind("<Button-1>", lambda event: page_q1())
    bouton2.bind("<Button-1>", lambda event: page_q2())
    bouton3.bind("<Button-1>", lambda event: page_q3())
    bouton4.bind("<Button-1>", lambda event: page_q4())
    bouton5.bind("<Button-1>", lambda event: page_q5())
    bouton6.bind("<Button-1>", lambda event: page_q6())
    bouton7.bind("<Button-1>", lambda event: page_q7())
    bouton8.bind("<Button-1>", lambda event: page_q8())
    bouton9.bind("<Button-1>", lambda event: page_q9())
    bouton10.bind("<Button-1>", lambda event: page_q10())


def page_q1():
    efface(root)
    pass


def page_q2():
    efface(root)
    pass


def page_q3():
    efface(root)
    pass


def page_q4():
    efface(root)
    pass


def page_q5():
    efface(root)
    pass


def page_q6():
    efface(root)
    pass


def page_q7():
    efface(root)
    pass


def page_q8():
    efface(root)
    pass


def page_q9():
    efface(root)
    pass


def page_q10():
    efface(root)
    pass


page_principale()
root.mainloop()
