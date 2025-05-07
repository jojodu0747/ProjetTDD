from base_dd import BDD_EVENTS
from liste_recherche import listerecherche


def count_medaille(nom):
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
    if BDD_EVENTS[BDD_EVENTS["Name"] == nom].empty:
        raise ValueError(
            f"Attention le nom '{nom}' n'a pas été trouvé dans la base de données. \n"
            + f"Vouliez-vous rechercher plutôt l'un de ces noms {listerecherche(nom)} ?"
        )
    Rep = BDD_EVENTS[BDD_EVENTS["Name"] == nom]
    res = f"{nom} a remporté {len(Rep.dropna())} médailles.\n"
    return res
