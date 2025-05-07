from base_dd import BDD_EVENTS
from liste_recherche import listerecherche_sport


def top_nations_par_sport(sport, annee_debut, annee_fin, D):
    """
    Cette fonction répond à la question 3.
    Elle calcule le nombre total de médailles remportées par chaque nation dans un sport
    donné entre deux années spécifiques.
    Le sport, les années de début et de fin sont passés en paramètres, ainsi que le
    nombre D de nations

    parameters
    __________

    sport : str
        Le sport pour lequel le classement des nations doit être calculé.
    annee_debut : int
        L'année de début de la période à considérer.
    annee_fin : int
        L'année de fin de la période à considérer.
    D : int la longueur du classement renvoyé

    returns
    _______

    pandas.Series
        Une série contenant le nombre de médailles remportées par chaque nation dans le
        sport spécifié,
        triée par ordre décroissant. Seules les D premières nations sont retournées.
    """
    # Filtrer la base de données pour le sport et les années spécifiés et ne garder
    # que les médailles
    if BDD_EVENTS[BDD_EVENTS["Event"] == sport].empty:
        raise ValueError(
            f"Attention le sport '{sport}' n'a pas été trouvé dans la base de "
            f"données.  \n" + f"Vouliez-vous rechercher plutôt l'un de ces sports"
            f" {listerecherche_sport(sport)} ?"
        )
    table_saut_longueur = BDD_EVENTS[
        (BDD_EVENTS["Event"] == sport)
        & BDD_EVENTS["Year"].between(annee_debut, annee_fin)
    ]
    # Grouper par nation et compter le nombre de médailles de chacune d'entre elles
    nombre_medailles = table_saut_longueur.groupby("NOC").size()
    # Trier les résultats par ordre décroissant
    classement = nombre_medailles.sort_values(ascending=False)
    return classement[0:D]
