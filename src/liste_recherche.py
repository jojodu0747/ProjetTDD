import Levenshtein


def levenshtein_score(name1, name2):
    return Levenshtein.distance(name1, name2)


def listerecherche(nom, D=5):
    """
    Cette fonction recherche les D noms les plus proches d'un nom donné dans la base de données
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
    BDD_EVENTS["Score"] = BDD_EVENTS["Name"].apply(
        lambda x: Levenshtein.distance(nom, x)
    )

    meilleurs_noms = (
        BDD_EVENTS.sort_values(by="Score")
        .drop_duplicates(subset="Name")
        .head(D)["Name"]
        .tolist()
    )

    return meilleurs_noms