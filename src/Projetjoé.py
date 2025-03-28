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
