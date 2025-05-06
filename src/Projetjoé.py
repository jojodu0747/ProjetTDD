import pandas as pd
import numpy as np
from base_dd import BDD_EVENTS

print(BDD_EVENTS.head())  # avoir un résumé des premiere ligne de la bdd

BDD_EVENTS.describe()  # avoir un résumé de la bdd
print(BDD_EVENTS.columns)  # avoir les colonnes de la BDD


# Déterminez le nombre de médailles gagnées par Michael Phelps. Son nom complet est Michael
# Fred Phelps, II

Q1 = BDD_EVENTS[
    (BDD_EVENTS["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
len(Q1)
# on conditionne directement sur la colonnne Name avec str.contains (propre à Panda)
# str.contains('ce que tu veux que ça contienne')
# Case = False si on veut pas differencier majuscules et minuscules (True l'inverse)
# na = False peut être utile si ça renvoie des na dans la requète, .dropna() enleve les na

# création d'une table saut en longueur
table_saut_longueur = BDD_EVENTS[
    (BDD_EVENTS["Sport"].str.contains("Athletics"))
    & (BDD_EVENTS["Season"] == "Summer")
    & BDD_EVENTS["Event"].str.contains(
        "Athletics Men's Long Jump|Athletics Women's Long Jump"
    )
]
table_saut_longueur.describe()

# Grouper par nation et compter le nombre de médailles
nombre_medailles = table_saut_longueur.groupby("NOC").size()

# Trier les résultats par ordre décroissant
classement = nombre_medailles.sort_values(ascending=False)
classement[0:5]

print("Type de 'Sport' :", BDD_EVENTS["Sport"].dtype)
print("Type de 'Season' :", BDD_EVENTS["Season"].dtype)

BDD_EVENTS["Sport"].unique()
BDD_EVENTS["Season"].unique()

BDD_EVENTS[BDD_EVENTS["Season"] == "Summer"]

BDD_EVENTS["NOC"]

# brouillon Q1

Q1 = BDD_EVENTS[
    (BDD_EVENTS["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
print(len(Q1))


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


print(listerecherche("michael phelps", 5))
