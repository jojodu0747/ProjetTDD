from base_dd import BDD_EVENTS


BDD_EVENTS_2016 = BDD_EVENTS[BDD_EVENTS["Year"] == 2016]


BDD_medalists_2016 = BDD_EVENTS_2016[BDD_EVENTS_2016["Medal"].notna()]


BDD_medalists_2016 = BDD_medalists_2016.merge(BDD_EVENTS, on="NOC", how="left")


continent_map = {
    "Europe": ["FRA", "GER", "GBR", "RUS", "ITA"],
    "Amérique": ["USA", "CAN", "BRA", "ARG", "MEX"],
    "Asie": ["CHN", "JPN", "KOR", "IND"],
    "Afrique": ["KEN", "RSA", "EGY", "NGR"],
    "Océanie": ["AUS", "NZL", "FIJ"],
}


def continent(noc):
    for continent, countries in continent_map.items():
        if noc in countries:
            return continent
    return "Autre"


BDD_medalists_2016["Continent"] = BDD_medalists_2016["NOC"].apply(continent)

# Compter les médailles par continent
medals_by_continent = BDD_medalists_2016["Continent"].value_counts()
print(medals_by_continent)
