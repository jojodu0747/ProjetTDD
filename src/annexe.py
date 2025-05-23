import matplotlib.pyplot as plt
import pandas as pd
from question7 import compter_medailles_par_continent
from base_dd import BDD_EVENTS
from modalite import YEAR

# Question 7

# Obtenir la liste des années disponibles
annees = sorted(BDD_EVENTS["Year"].dropna().unique())

# Créer une DataFrame vide pour stocker les résultats
resultats = pd.DataFrame()

# Remplir le tableau pour chaque année
for annee in annees:
    data = compter_medailles_par_continent(annee, BDD_EVENTS)
    resultats[annee] = data

# Transposer pour avoir les années en lignes
resultats = resultats.T.fillna(0)

# Tracer le graphique
plt.figure(figsize=(14, 7))
resultats.plot(kind="bar", stacked=True, colormap="tab20", figsize=(15, 7))

plt.title("Répartition des médailles par continent au fil des années")
plt.xlabel("Année")
plt.ylabel("Nombre de médailles")
plt.legend(title="Continent", bbox_to_anchor=(0.99, 1), loc="upper left")
plt.tight_layout()
plt.grid(True, linestyle="--", alpha=0.6)
# plt.show()

# Question 9


def plot_evolution_femmes(annee=None):
    if annee is None:
        annee = YEAR

    dfM = BDD_EVENTS.loc[
        (BDD_EVENTS["Sex"] == "M") & (BDD_EVENTS["Year"].isin(annee)),
        ["ID", "Year"]
    ].drop_duplicates().groupby("Year").count()

    dfF = BDD_EVENTS.loc[
        (BDD_EVENTS["Sex"] == "F") & (BDD_EVENTS["Year"].isin(annee)),
        ["ID", "Year"]
    ].drop_duplicates().groupby("Year").count()

    for x in annee:
        if x not in dfF.index:
            dfF.loc[x] = 0
        if x not in dfM.index:
            dfM.loc[x] = 0

    dfF = dfF.sort_index()
    dfM = dfM.sort_index()

    dfT = round(dfF / (dfF + dfM) * 100, 2)

    plt.figure(figsize=(10, 6))
    plt.plot(dfT.index, dfT["ID"], marker='o', linestyle='-')
    plt.xlabel("Année")
    plt.ylabel("Pourcentage de femmes (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
