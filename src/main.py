import tkinter as tk
from base_dd import adresse_fichier
from modalite import REGION, NOC, MEDAL, GAMES, YEAR, EVENT, SEASON
from question2_py_pur import question2_p
from question2 import question2
from question3 import top_nations_par_sport
from question4 import age_moyen_medailles
from question6_fonctions import calculate_grouped_mean
from question6_python_pur import moyenne_age_par_sexe
from question7_fonctions import compter_medailles_par_continent
from question8 import ratio_F_H
from question10 import plus_medailles
from question10_py_pur import plus_medailles_pur
from question1 import count_medaille
from question1_py_pur import count_medaille_pp
from liste_recherche import listerecherche
from question5 import question5
from question9 import question9

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
    "Q8: Quels sont les pays qui ont le ratio du nombre de médaillées"
    " femmes sur le nombre de médaillés hommes le plus haut et le plus bas ? ",
    "Q9: Comment le taux de participation des femmes aux Jeux"
    " Olympiques a-t-elle évolué au fil du temps ?",
    "Q10: Quels sont les sports dans lesquels il y a le plus de médaillés français ?"
        ]
AUTEUR = [
    "Joé", "Aziz", "Joé", "Joé", "Aziz", "Eliott", "Eliott", "Louis", "Aziz", "Louis"
]
FICHIER = [
    "question1.txt",
    "question2.txt",
    "question3.txt",
    "question4.txt",
    "question5.txt",
    "question6.txt",
    "question7.txt",
    "question8.txt",
    "question9.txt",
    "question10.txt"
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


def bouton_retour(frame_b):
    bouton_retour = tk.Label(frame_b,
                             text="Retour",
                             bg=COULEUR_PRINCIPALE,
                             fg=COULEUR_FONT,
                             font=("Arial", 20),
                             anchor="w",
                             height=2,
                             width=6,
                             borderwidth=3,
                             relief="solid",
                             padx=5,
                             pady=5)
    bouton_retour.pack(anchor="w", pady=5, padx=5)
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


def alterne_pp(l_param):
    l_param[0][0], l_param[1][0] = not l_param[0][0], not l_param[1][0]
    print(l_param)


def python_pur(l_param):
    checkboxpp = tk.Checkbutton(
        root,
        text='Python Pur',
        command=lambda: alterne_pp(l_param),
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
        if len(lb.curselection()) == 0:
            select = None
        else:
            for index in lb.curselection():
                select.insert(index, lb.get(index))
    elif type == "lint":
        if len(lb.curselection()) == 0:
            select = None
        else:
            for index in lb.curselection():
                select.insert(index, int(lb.get(index)))
    elif type == "str":
        select = lb.get(lb.curselection()[0])
    elif type == "int":
        select = int(lb.get(lb.curselection()[0]))
    elif type == "region":
        select = NOC[lb.curselection()[0]]
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


def f_joueur(frame, ssframe, text, param, i):
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
        width=50
    )
    ssframe[3] = tk.Button(ssframe[0], text="chercher",
                           command=lambda: j_submit(ssframe[2], ssframe[4]))
    ssframe[4] = tk.Listbox(ssframe[0], font=('Arial', 20),
                            selectmode="single", width=50, height=5)
    ssframe[5] = tk.Button(ssframe[0], text="submit",
                           command=lambda: submit(ssframe[4], param, i, "str"))
    ssframe[0].pack(side='left', expand=True)
    ssframe[1].pack()
    ssframe[2].pack()
    ssframe[3].pack()
    ssframe[4].pack()
    ssframe[5].pack()


def j_submit(entry, listbox):
    listbox.delete(0, tk.END)
    nom = entry.get()
    liste = listerecherche(nom)
    for name in liste:
        listbox.insert(tk.END, name)


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


def executer(frame, fonction, person, param, res, facu=None, lab=None):
    bouton_retour = tk.Label(
        frame,
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
    bouton_retour.pack(anchor="w", pady=5, padx=5)
    bouton_retour.bind("<Enter>",
                       lambda event: event_change_couleur(event, COULEUR_SECONDAIRE))
    bouton_retour.bind("<Leave>",
                       lambda event: event_change_couleur(event, COULEUR_PRINCIPALE))
    bouton_retour.bind("<Button-1>",
                       lambda event: applique(fonction, person, param, res, facu, lab))


def applique(fonction, person, param, res, facu, lab):
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
    if lab is None:
        print(res[0])
    else:
        affiche(lab, res)


def e_submit(entry, param, i, type):
    if type == "int":
        param[i] = int(entry.get())
    else:
        param[i] = entry.get()
    print(param)


def f_entry(frame, ssframe, text, param, i, type="str", fontsize=20):
    ssframe[0] = tk.Frame(frame)
    ssframe[1] = tk.Label(
        ssframe[0],
        text=text,
        font=('Arial', fontsize))
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


def affiche(lab, res):
    lab[0].config(text="Résultat\n" + str(res[0]))


def creer_affiche(lab):
    lab[0] = tk.Label(
        root,
        text='',
        font=("Courier New", 15),
        bg=COULEUR_PRINCIPALE,
        fg=COULEUR_FONT,
        borderwidth=3,
        relief="solid",
        padx=5,
        pady=5,
        justify="left")
    lab[0].pack(anchor="w")


def bouton_sauvegarde(frame, param, person, res, i):
    bouton_retour = tk.Label(
            frame,
            text="Sauvegarde",
            bg=COULEUR_PRINCIPALE,
            fg=COULEUR_FONT,
            font=("Arial", 20),
            anchor="w",
            height=2,
            borderwidth=3,
            relief="solid",
            padx=5,
            pady=5)
    bouton_retour.pack(anchor="w", pady=5, padx=5)
    bouton_retour.bind(
        "<Enter>", lambda event: event_change_couleur(event, COULEUR_SECONDAIRE))
    bouton_retour.bind(
        "<Leave>", lambda event: event_change_couleur(event, COULEUR_PRINCIPALE))
    bouton_retour.bind(
        "<Button-1>", lambda event: sauvegarde(param, person, res, i))


def sauvegarde(param, person, res, i):
    with open(adresse_fichier + FICHIER[i],
              "a",
              encoding="utf-8") as file:
        str = f"Python Pur:{param[int(person[0])][0]!s:>69}\n"
        str += "Argument:\n" + f"{*param[int(person[0])][1:]!s:>80}\n"
        str += "Résultat:\n" + f"{res[0]!s:>80}\n" + "-"*80 + "\n"
        file.write(str)


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
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(0)
    personnalise = [False]
    param_d = [False, "Michael Fred Phelps, II"]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [count_medaille, count_medaille_pp]
    res = [None]
    python_pur(l_param)
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None, None, None]
    f_joueur(framep, framep1, "Choix du joueur", param, 1)
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, param, res, 0)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 0)


def page_q2():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(1)
    personnalise = [False]
    param_d = [False, ["2016 Summer"], MEDAL, False]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [question2, question2_p]
    res = [None]
    python_pur(l_param)
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None]
    f_listbox(framep, framep1, "Choix des sessions", "multiple", GAMES, param, 1, 20)
    f_listbox(framep, framep2, "Choix des médails", "multiple", MEDAL, param, 2, 20)
    f_checkbox(framep, framep3, "Sessions combiné", param, 3)
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 1)


def page_q3():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(2)
    personnalise = [False]
    param_d = [False, "Athletics Men's Long Jump", [1896, 2016], 5]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [top_nations_par_sport]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix du sport", "single", EVENT, param, 1, 14, 70,
              "str")
    f_listbox(framep, framep2, "Choix de l'année de début et de fin",
              "multiple", YEAR, param, 2, 14, 10, "lint")
    f_entry(framep, framep3, "Nombre de nation", param, 3, "int")
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, 3, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 2)


def page_q4():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(3)
    personnalise = [False]
    param_d = [False, "Summer", "Gold", [1896, 2016]]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [age_moyen_medailles]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
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
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, 4, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 3)


def page_q5():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(4)
    personnalise = [False]
    param_d = [False, ["Gold"], None]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [question5]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix des médails", "multiple", MEDAL, param, 1, 20)
    f_listbox(framep, framep2, "Choix des années",
              "multiple", YEAR, param, 2, 14, 10, "lint")
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 4)


def page_q6():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(5)
    personnalise = [False]
    param_d = [False]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [calculate_grouped_mean, moyenne_age_par_sexe]
    res = [None]
    python_pur(l_param)
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 5)


def page_q7():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(6)
    personnalise = [False]
    param_d = [False, 2016]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [compter_medailles_par_continent]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix de l'année'", "single", YEAR, param, 1, 20,
              type="int")
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 6)


def page_q8():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(7)
    personnalise = [False]
    param_d = [False, False, 10, 0, 10, None, False]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [ratio_F_H]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None, None, None]
    framep4 = [None, None, None, None]
    framep5 = [None, None, None, None]
    framep6 = [None, None]
    f_checkbox(framep, framep1, "Ordre croissant", param, 1)
    f_entry(framep, framep2, "Limit", param, 2, "int", 15)
    f_entry(framep, framep3, "Offset", param, 3, "int", 15)
    f_entry(framep, framep4, "Nombre de médailles requis", param, 4, "int", 15)
    f_listbox(framep, framep5, "Choix des années",
              "multiple", YEAR, param, 5, 14, 10, "lint")
    f_checkbox(framep, framep6, "Regroupe par région au lieu de NOC", param, 6)
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 7)


def page_q9():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(8)
    personnalise = [False]
    param_d = [False, [1896, 1952, 2016]]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [question9]
    res = [None]
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    f_listbox(framep, framep1, "Choix des années",
              "multiple", YEAR, param, 1, 14, 10, "lint")
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 8)


def page_q10():
    efface(root)
    frame_b = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    frame_b.pack(side="left", fill="both")
    bouton_retour(frame_b)
    presentation_question(9)
    personnalise = [False]
    param_d = [False, "FRA", 10, 0, None, False]
    param = param_d.copy()
    l_param = [param_d, param]
    fonction = [plus_medailles, plus_medailles_pur]
    res = [None]
    python_pur(l_param)
    framepp = tk.Frame(root, bg=COULEUR_PRINCIPALE)
    framep = tk.Frame(
        framepp, bg=COULEUR_PRINCIPALE, padx=5, pady=10)
    framep1 = [None, None, None, None]
    framep2 = [None, None, None, None]
    framep3 = [None, None, None, None]
    framep4 = [None, None, None, None]
    framep5 = [None, None]
    f_listbox(framep, framep1, "Région", "single", REGION, param, 1, 14, 30, "region")
    f_entry(framep, framep2, "Limit", param, 2, "int", 15)
    f_entry(framep, framep3, "Offset", param, 3, "int", 15)
    f_listbox(framep, framep4, "Choix des années",
              "multiple", YEAR, param, 4, 14, 10, "lint")
    f_checkbox(framep, framep5, "Ordre croissant", param, 5)
    personnaliser_p(personnalise, framep)
    framepp.pack(fill="both")
    lab_affiche = [None]
    creer_affiche(lab_affiche)
    executer(frame_b, fonction, personnalise, l_param, res, lab=lab_affiche)
    bouton_sauvegarde(frame_b, l_param, personnalise, res, 9)


page_principale()
root.mainloop()
