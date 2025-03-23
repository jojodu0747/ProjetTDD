import panda as pd

# Q1

Q1 = athlete_event[
    (athlete_event["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
len(Q1)

# Q2

# Q3

# création d'une table saut en longueur
table_saut_longueur = athlete_event[
    (athlete_event["Sport"].str.contains("Athletics"))
    & (athlete_event["Season"] == "Summer")
    & athlete_event["Event"].str.contains(
        "Athletics Men's Long Jump|Athletics Women's Long Jump"
    )
]
# Grouper par nation et compter le nombre de médailles de chacune d'entre elles
nombre_medailles = table_saut_longueur.groupby("NOC").size()
# Trier les résultats par ordre décroissant
classement = nombre_medailles.sort_values(ascending=False)

classement[0:5]

# Q4

# Q5

# Q6

# Q7

# Q8

# Q9

# Q10
