from base_dd import BDD_EVENTS


def count_medaille(nom):
    """
    Cette fonction répond à la question 1.
    Elle calcule le nombre total de médailles remportées par un athlète donné.
    Le nom de l'athlète est passé en paramètre et la fonction renvoie le nombre total de médailles.

    Parameters
    __________

    nom : str
        Le nom de l'athlète pour lequel le nombre de médailles doit être calculé.

    Returns
    _______

    int
        Le nombre total de médailles remportées par l'athlète spécifié.
    """
    Rep = BDD_EVENTS[BDD_EVENTS["Name"] == nom]
    res = f"{nom} a remporté {len(Rep.dropna())} médailles.\n"
    return res
