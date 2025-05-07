import csv
from base_dd import adresse, n_doublon


def count_medaille_pp(nom):
    """
    Cette fonction répond à la question 1.
    Elle calcule le nombre total de médailles remportées par un athlète donné.
    Le nom de l'athlète est passé en paramètre et la fonction renvoie le nombre
    total de médailles.

    Parameters
    __________

    nom : str
        Le nom de l'athlète pour lequel le nombre de médailles doit être calculé.

    Returns
    _______

    int
        Le nombre total de médailles remportées par l'athlète spécifié.
    """
    medal_count = 0
    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        spamreader = csv.reader(bdd_athlete)
        header = next(spamreader)
        idx_nom = header.index('Name')
        idx_medal = header.index('Medal')
        n = 2
        for row in spamreader:
            if n in n_doublon:
                n += 1
                continue
            n += 1
            if row[idx_medal] != 'NA' and row[idx_nom] == nom:
                medal_count += 1
    return medal_count
