import tkinter as tk
from modalite import REGION, SEX, SPORT, MEDAL, GAMES, YEAR, EVENT, SEASON
from question2_py_pur import question2_p
from question2 import question2
from question3 import top_nations_par_sport
from question4 import age_moyen_medailles

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
    labelpq1 = tk.Label(
        root,
        text='Par: ' + AUTEUR[i],
        font=("Arial", 17),
        bg=COULEUR_PRINCIPALE,
        fg=COULEUR_FONT,
        padx=10)
    labelpq1.pack(side="top", anchor="w")
    labelpq2 = tk.Label(
        root,
        text=QUESTION[i],
        font=("Arial", 25),
        bg=COULEUR_PRINCIPALE,
        fg=COULEUR_FONT,
        pady=10,
        padx=10,
        justify="left")
    labelpq2.pack(side="top", anchor="w")


def alterne(param, i):
    param[i] = not param[i]
    print(param)


def python_pur(param):
    checkboxpp = tk.Checkbutton(
        root,
        text='Python Pur',
        command=lambda: alterne(param, 0),
        font=('Arial', 20),
        fg=COULEUR_FONT,
        bg=COULEUR_PRINCIPALE,
        padx=25,
        pady=10,
        anchor='w'
        )
    checkboxpp.pack(anchor='w')


def personnaliser_p(personnalise, frame):
    checkboxp = tk.Checkbutton(
        root,
        text='Personnaliser les arguments',
        command=lambda: personnaliser_f(personnalise, frame),
        font=('Arial', 20),
        fg=COULEUR_FONT,
        bg=COULEUR_PRINCIPALE,
        padx=25,
        pady=10,
        anchor='w'
        )
    checkboxp.pack(anchor='w')


def personnaliser_f(personnalise, frame):
    if personnalise[0]:
        frame.pack_forget()
    else:
        frame.pack(fill="both")
        frame.update_idletasks()
    personnalise[0] = not personnalise[0]


def submit(lb, param, i, type):
    select = []
    if type == "lstr":
        for index in lb.curselection():
            select.insert(index, lb.get(index))
    elif type == "lint":
        for index in lb.curselection():
            select.insert(index, int(lb.get(index)))
    elif type == "str":
        select = lb.get(lb.curselection()[0])
    param[i] = select
    print(param)


def f_listbox(frame, ssframe, text, typesel, liste, param, i, fontsize,
              width=None, type="lstr"):
    ssframe[0] = tk.Frame(frame)
    ssframe[0].pack(side='left', expand=True)
    ssframe[1] = tk.Label(
        ssframe[0],
        text=text,
        font=('Arial', 20))
    ssframe[1].pack()
    ssframe[2] = tk.Listbox(ssframe[0], font=('Arial', fontsize),
                            selectmode=typesel, width=width)
    for x in liste:
        ssframe[2].insert(tk.END, x)
    ssframe[2].pack()
    ssframe[3] = tk.Button(
        ssframe[0], text="submit", font=('Arial', 20), command=lambda: submit(
            ssframe[2], param, i, type))
    ssframe[3].pack()


def f_checkbox(frame, ssframe, text, param, i):
    ssframe[0] = tk.Frame(frame)
    ssframe[0].pack(side='left', expand=True)
    ssframe[1] = tk.Checkbutton(
        ssframe[0],
        text=text,
        command=lambda: alterne(param, i),
        font=('Arial', 20),
        fg=COULEUR_FONT,
        bg=COULEUR_PRINCIPALE,
        padx=25,
        pady=10,
        anchor='w'
        )
    ssframe[1].pack()


def executer(fonction, person, param, res, facu=None):
    bouton_retour = tk.Label(
        root,
        text="Executer",
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
    bouton_retour.bind("<Button-1>",
                       lambda event: applique(fonction, person, param, res, facu))


def applique(fonction, person, param, res, facu):
    if facu is None:
        res[0] = fonction[param[int(person[0])][0]](*param[int(person[0])][1:])
    elif facu == 3:
        l1, l2 = param[0], param[1]
        l1a = [*l1[:2], *l1[2], l1[3]]
        l2a = [*l2[:2], *l2[2], l2[3]]
        paramb = [l1a, l2a]
        print(paramb[int(person[0])][1:])
        res[0] = fonction[paramb[int(person[0])][0]](*paramb[int(person[0])][1:])
    elif facu == 4:
        l1, l2 = param[0], param[1]
        l1a = [*l1[:3], *l1[3]]
        l2a = [*l2[:3], *l2[3]]
        paramb = [l1a, l2a]
        print(paramb[int(person[0])][1:])
        res[0] = fonction[paramb[int(person[0])][0]](*paramb[int(person[0])][1:])
    print(res[0])


def e_submit(entry, param, i, type):
    if type == "int":
        param[i] = int(entry.get())
    else:
        param[i] = entry.get()
    print(param)


def f_entry(frame, ssframe, text, param, i, type="str"):
    ssframe[0] = tk.Frame(frame)
    ssframe[1] = tk.Label(
        ssframe[0],
        text=text,
        font=('Arial', 20))
    ssframe[2] = tk.Entry(
        ssframe[0],
        font=('Arial', 20),
        bg='#111111',
        fg='#00FF00',
        width=10
    )
    ssframe[3] = tk.Button(ssframe[0], text="submit",
                           command=lambda: e_submit(ssframe[2], param, i, type))
    ssframe[0].pack(side='left', expand=True)
    ssframe[1].pack()
    ssframe[2].pack(side="left")
    ssframe[3].pack(side="left")


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
    personnalise = [False]
    param_d = [False, ["2016 Summer"], MEDAL, False]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [question2, question2_p]
    res = [None]
    python_pur(param)
    framep = tk.Frame(
        root, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None]
    f_listbox(framep, framep1, "Choix des sessions", "multiple", GAMES, param, 1, 20)
    f_listbox(framep, framep2, "Choix des médails", "multiple", MEDAL, param, 2, 20)
    f_checkbox(framep, framep3, "Sessions combiné", param, 3)
    personnaliser_p(personnalise, framep)
    executer(fonction, personnalise, l_param, res)


def page_q3():
    efface(root)
    bouton_retour()
    presentation_question(2)
    personnalise = [False]
    param_d = [False, "Athletics Men's Long Jump", [1896, 2016], 5]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [top_nations_par_sport]
    res = [None]
    framep = tk.Frame(
        root, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix du sport", "single", EVENT, param, 1, 14, 70,
              "str")
    f_listbox(framep, framep2, "Choix de l'année de début et de fin",
              "multiple", YEAR, param, 2, 14, 10, "lint")
    f_entry(framep, framep3, "Nombre de nation", param, 3, "int")
    personnaliser_p(personnalise, framep)
    executer(fonction, personnalise, l_param, res, 3)


def page_q4():
    efface(root)
    bouton_retour()
    presentation_question(3)
    personnalise = [False]
    param_d = [False, "Summer", "Gold", [1896, 2016]]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [age_moyen_medailles]
    res = [None]
    framep = tk.Frame(
        root, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix de la saison", "single", SEASON, param, 1, 14,
              type="str")
    f_listbox(framep, framep2, "Choix de la médaille", "single", MEDAL, param,
              2, 14, type="str")
    f_listbox(framep, framep3, "Choix de l'année de début et de fin",
              "multiple", YEAR, param, 3, 14, 10, "lint")
    personnaliser_p(personnalise, framep)
    executer(fonction, personnalise, l_param, res, 4)


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
