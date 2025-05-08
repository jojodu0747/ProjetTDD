from base_dd import BDD_EVENTS

# Dictionnaire des continents
continent_map = {
    "Europe": ["FRA", "GER", "GBR", "RUS", "ITA", "SAA", "FRG", "GDR", "EUN", "URS"],
    "Amérique": [
        "USA",
        "CAN",
        "MEX",
        "ARG",
        "BRA",
        "CHL",
        "COL",
        "VEN",
        "PER",
        "URU",
        "PAR",
    ],
    "Asie": ["CHN", "JPN", "KOR", "IND", "AUS", "IRN", "PAK", "HKG"],
    "Afrique": ["KEN", "RSA", "EGY", "NGR", "ETH", "TUN", "MAR", "ALG", "ZAF"],
    "Océanie": ["AUS", "NZL", "FIJ", "PNG", "SAM", "TGA", "WLF"],
}


# Fonction pour trouver le continent
def continent(noc):
    for cont, countries in continent_map.items():
        if noc in countries:
            return cont
    return "Autre"


# Fonction principale généralisée
def compter_medailles_par_continent(annee, BDD_EVENTS=BDD_EVENTS):
    """
    Cette fonction compte le nombre de médailles remportées par continent
    pour une année donnée dans la base de données des événements olympiques.

    parameters
    __________
    annee : int
        L'année pour laquelle on souhaite compter les médailles.
    BDD_EVENTS : pandas.DataFrame
        La base de données des événements olympiques.

    returns
    _______
    pandas.Series
        Une série contenant le nombre de médailles remportées par continent,
        triée par ordre décroissant.
    """
    df_year = BDD_EVENTS[BDD_EVENTS["Year"] == annee]
    df_medalists = df_year[df_year["Medal"].notna()]
    df_medalists = df_medalists.copy()
    df_medalists["Continent"] = df_medalists["NOC"].apply(continent)
    return df_medalists["Continent"].value_counts()


import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()
