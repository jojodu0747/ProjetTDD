import pandas as pd
import numpy as np

athlete_event = pd.read_csv(
    r"C:\Users\napol\Documents\Python\projTDD\ProjetTDD\donnees_jeux_olympiques\donnees_jeux_olympiques\athlete_events.csv"
)

print(athlete_event.head())  # avoir un résumé des premiere ligne de la bdd

athlete_event.describe()  # avoir un résumé de la bdd
print(athlete_event.columns)  # avoir les colonnes de la BDD


# Déterminez le nombre de médailles gagnées par Michael Phelps. Son nom complet est Michael
# Fred Phelps, II

Q1 = athlete_event[
    (athlete_event["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
len(Q1)
# on conditionne directement sur la colonnne Name avec str.contains (propre à Panda)
# str.contains('ce que tu veux que ça contienne')
# Case = False si on veut pas differencier majuscules et minuscules (True l'inverse)
# na = False peut être utile si ça renvoie des na dans la requète, .dropna() enleve les na

# création d'une table saut en longueur
table_saut_longueur = athlete_event[
    (athlete_event["Sport"].str.contains("Athletics"))
    & (athlete_event["Season"] == "Summer")
    & athlete_event["Event"].str.contains(
        "Athletics Men's Long Jump|Athletics Women's Long Jump"
    )
]
table_saut_longueur.describe()

# Grouper par nation et compter le nombre de médailles
nombre_medailles = table_saut_longueur.groupby("NOC").size()

# Trier les résultats par ordre décroissant
classement = nombre_medailles.sort_values(ascending=False)
classement[0:5]

print("Type de 'Sport' :", athlete_event["Sport"].dtype)
print("Type de 'Season' :", athlete_event["Season"].dtype)

athlete_event["Sport"].unique()
athlete_event["Season"].unique()

athlete_event[athlete_event["Season"] == "Summer"]

athlete_event["NOC"]
