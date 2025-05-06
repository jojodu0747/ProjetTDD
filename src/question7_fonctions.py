from base_dd import BDD_EVENTS

# Dictionnaire des continents
continent_map = {
    "Europe": ["FRA", "GER", "GBR", "RUS", "ITA"],
    "Amérique": ["USA", "CAN", "BRA", "ARG", "MEX"],
    "Asie": ["CHN", "JPN", "KOR", "IND"],
    "Afrique": ["KEN", "RSA", "EGY", "NGR"],
    "Océanie": ["AUS", "NZL", "FIJ"],
}


# Fonction pour trouver le continent
def continent(noc):
    for cont, countries in continent_map.items():
        if noc in countries:
            return cont
    return "Autre"


# Fonction principale généralisée
def compter_medailles_par_continent(annee, BDD_EVENTS):
    df_year = BDD_EVENTS[BDD_EVENTS["Year"] == annee]
    df_medalists = df_year[df_year["Medal"].notna()]
    df_medalists = df_medalists.copy()
    df_medalists["Continent"] = df_medalists["NOC"].apply(continent)
    return df_medalists["Continent"].value_counts()


print(compter_medailles_par_continent(2012, BDD_EVENTS))
