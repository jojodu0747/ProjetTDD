import tkinter as tk

# Constantes
COULEUR_PRINCIPALE = "#25292D"
COULEUR_SECONDAIRE = "#4a4a4a"
COULEUR_FONT = "#ffffff"
QUESTION = [
    "Q1: Déterminez le nombre de médailles gagnées par Michael"
    " Phelps. Son nom complet est Michael Fred Phelps, II.",
    "Q2: Trouvez des bornes inférieures et supérieures pour "
    "le nombre de médailles par nation pour les Jeux Olympiques"
    " de 2016.",
    "Q3: Déterminer quelles sont les 5 premières nations qui"
    " ont eu le plus de médaillés au saut en longueur en 200 ans.",
    "Q4: Déterminer l'âge moyen des médaillés d'or au JO"
    " d'hiver et au JO d'été.",
    "Q5: Quel est la personne la plus et la plus moin agée"
    " ayant eu une médaille d'or.",
    "Q6: Quelle est la moyenne d'age des femmes et hommes"
    " médaillées aux Jeux Olympiques depuis leur création ?",
    "Q7: Quelle est la répartition des médailles par continent"
    " au jeux Olympiques de 2016?.",
    "Q8: Identifier les pays qui ont le ratio nombre de"
    " médailles gagnées par des femmes sur nombre de médailles"
    " gagnées par"
    "\n des hommes le plus haut/le plus bas?",
    "Q9: Comment le taux de participation des femmes aux Jeux"
    " Olympiques a-t-elle évolué au fil du temps ?",
    "Q10: Quel sont les sports où la France a gagné le plus"
    " de médaille ?"
        ]
AUTEUR = [
    "Joé", "Aziz", "Joé", "Joé", "Aziz", "Eliott", "Eliott", "Louis", "Aziz", "Louis"
]
MEDALS = ['Bronze', 'Silver', 'Gold']


# Initialisation
root = tk.Tk()
root.title("ProjetTDD")
root.geometry("1280x720")
root.minsize(1280, 720)
root.configure(bg=COULEUR_PRINCIPALE)


# Définition des fonctions influençant les pages
def event_change_couleur(event, couleur):
    event.widget.config(bg=couleur)


def efface(window):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            efface(widget)
        widget.destroy()
        del widget


def bouton_retour():
    bouton_retour = tk.Label(root,
                             text="Retour",
                             bg=COULEUR_PRINCIPALE,
                             fg=COULEUR_FONT,
                             font=("Arial", 20),
                             anchor="w",
                             height=2,
                             borderwidth=3,
                             relief="solid",
                             padx=5,
                             pady=5)
    bouton_retour.pack(side="left", anchor="n", pady=5, padx=5)
    bouton_retour.bind("<Enter>",
                       lambda event: event_change_couleur(event, COULEUR_SECONDAIRE))
    bouton_retour.bind("<Leave>",
                       lambda event: event_change_couleur(event, COULEUR_PRINCIPALE))
    bouton_retour.bind("<Button-1>", lambda event: page_principale())


def presentation_question(i):
    label1 = tk.Label(root,
                      text='Par: ' + AUTEUR[i],
                      font=("Arial", 17),
                      bg=COULEUR_PRINCIPALE,
                      fg=COULEUR_FONT,
                      padx=10)
    label1.pack(side="top", anchor="w")
    label2 = tk.Label(root,
                      text=QUESTION[i],
                      font=("Arial", 25),
                      bg=COULEUR_PRINCIPALE,
                      fg=COULEUR_FONT,
                      pady=10,
                      padx=10,
                      justify="left")
    label2.pack(side="top", anchor="w")


def python_pur():
    framepyp = tk.Frame(
        root, bg=COULEUR_SECONDAIRE, padx=5, pady=10, borderwidth=3, relief="solid"
    )
    labelpyp = tk.Label(
        framepyp,
        text="Python Pur",
        font=("Arial", 25),
        bg=COULEUR_PRINCIPALE,
        g=COULEUR_FONT,
        pady=10,
        padx=10
    )


# Définition des pages
def page_principale():
    efface(root)
    label1 = tk.Label(root,
                      text="Par Aziz Seghaier, Joé Napolitano, Louis Stanisière,"
                      " Elliot Meriot",
                      font=("Arial", 14),
                      bg=COULEUR_PRINCIPALE,
                      fg=COULEUR_FONT)
    label2 = tk.Label(root, text="Projet TDD: Jeux Olympique", font=("Arial", 40),
                      bg=COULEUR_PRINCIPALE,
                      fg=COULEUR_FONT)
    frame1 = tk.Frame(root, bg=COULEUR_SECONDAIRE, padx=5, pady=10,
                      borderwidth=3, relief="solid")
    label1.pack(anchor=tk.W)
    label2.pack(pady=25)
    frame1.pack(expand=True)

    bouton = [None for i in range(10)]
    fonction = [
        page_q1,
        page_q2,
        page_q3,
        page_q4,
        page_q5,
        page_q6,
        page_q7,
        page_q8,
        page_q9,
        page_q10
        ]

    def bouton_pp(i):
        bouton[i] = tk.Label(
            frame1,
            text=QUESTION[i],
            bg=COULEUR_PRINCIPALE,
            fg=COULEUR_FONT,
            font=("Arial", 20),
            anchor="w",
            height=2,
            justify="left",
            borderwidth=3,
            relief="solid",
            padx=5,
            pady=5)
        bouton[i].pack(pady=2, fill="both")
        bouton[i].bind("<Enter>", lambda event: event_change_couleur(
            event, COULEUR_SECONDAIRE))
        bouton[i].bind("<Leave>", lambda event: event_change_couleur(
            event, COULEUR_PRINCIPALE))
        bouton[i].bind("<Button-1>", lambda event: fonction[i]())

    for i in range(10):
        bouton_pp(i)


def page_q1():
    efface(root)
    bouton_retour()
    presentation_question(0)


def page_q2():
    efface(root)
    bouton_retour()
    presentation_question(1)
    param_d = []
    python_pur()


def page_q3():
    efface(root)
    bouton_retour()
    presentation_question(2)


def page_q4():
    efface(root)
    bouton_retour()
    presentation_question(3)


def page_q5():
    efface(root)
    bouton_retour()
    presentation_question(4)


def page_q6():
    efface(root)
    bouton_retour()
    presentation_question(5)


def page_q7():
    efface(root)
    bouton_retour()
    presentation_question(6)


def page_q8():
    efface(root)
    bouton_retour()
    presentation_question(7)


def page_q9():
    efface(root)
    bouton_retour()
    presentation_question(8)


def page_q10():
    efface(root)
    bouton_retour()
    presentation_question(9)


page_principale()
root.mainloop()
