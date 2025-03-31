from base_dd import BDD_EVENTS
import matplotlib.pyplot as plt


def question2(liste_sessions, type_medaille, combine):
    """Cette fonction répond à la question 2.
    Il donne les bornes inférieur et supérieur du nombre de médailles obtenue par chaque
    nation, selon les types de médailles pris en compte, et selon les sessions pris en
    compte. Il retourne un graphique dont la nature dépend des paramètres

    Parameters
    __________

    liste_sessions: list[str]
        Liste des sessions prises en compte par la fonction

    type_medaille: list[str]
        Liste des médailles pris en compte

    combine : bool
        Si le calcul est fait sur l'ensemble des sessions ou par session

    Returns
    _______

    list[tuple[int]]
        La liste des couple (inf, max) pour chaque session ou pour l'ensemble des
        sessions selon combine.
        Affiche en parallèle des graphiques.
    """
    pass


combine = False
liste_sessions = []
type_medaille = []
