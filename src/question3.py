from base_dd import BDD_EVENTS

# création d'une table saut en longueur
table_saut_longueur = BDD_EVENTS[
    (BDD_EVENTS["Sport"].str.contains("Athletics"))
    & (BDD_EVENTS["Season"] == "Summer")
    & BDD_EVENTS["Event"].str.contains(
        "Athletics Men's Long Jump|Athletics Women's Long Jump"
    )
]
# Grouper par nation et compter le nombre de médailles de chacune d'entre elles
nombre_medailles = table_saut_longueur.groupby("NOC").size()
# Trier les résultats par ordre décroissant
classement = nombre_medailles.sort_values(ascending=False)

print(classement[0:5])
