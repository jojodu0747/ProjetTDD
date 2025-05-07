import Levenshtein
from base_dd import BDD_EVENTS


def levenshtein_score(name1, name2):
    return Levenshtein.distance(name1, name2)


def listerecherche(nom, D=5):
    """
    Cette fonction recherche les D noms les plus proches d'un nom donné dans la base de
    données
    Elle utilise la distance de Levenshtein pour évaluer la similarité entre les noms.

    parameters
    __________
    nom : str
        Le nom de l'athlète à rechercher dans la base de données.
    D : int, optionnel
        Le nombre de noms similaires à retourner. Par défaut, il est fixé à 5.

    returns
    _______
    list
        Une liste des D noms les plus proches trouvés dans la base de données.
    """
    df = BDD_EVENTS.loc[:, ['Name']]
    df = df.drop_duplicates(subset="Name")
    df["Score"] = df["Name"].apply(
        lambda x: Levenshtein.distance(nom, x)
    )

    meilleurs_noms = (
        df.sort_values(by="Score").head(D)["Name"].tolist()
    )
    return meilleurs_noms


def listerecherche_sport(sport, D=5):
    """
    Cette fonction recherche les D sports les plus proches d'un sport donné dans la
    base de données
    Elle utilise la distance de Levenshtein pour évaluer la similarité entre les sports.

    parameters
    __________
    sport : str
        Le nom de l'athlète à rechercher dans la base de données.
    D : int, optionnel
        Le nombre de noms similaires à retourner. Par défaut, il est fixé à 5.

    returns
    _______
    list
        Une liste des D sports les plus proches trouvés dans la base de données.
    """
    df = BDD_EVENTS.loc[:, ['Event']]
    df = df.drop_duplicates(subset="Event")
    df["Score"] = df["Event"].apply(
        lambda x: Levenshtein.distance(sport, x)
    )

    meilleurs_noms = (
        df.sort_values(by="Score").head(D)["Event"].tolist()
    )
    return meilleurs_noms
