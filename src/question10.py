# Quels sont les sports où la France a gagné le plus de médaille ?
from base_dd import BDD_EVENTS
from base_dd import BDD_REGIONS


def plus_medailles(region="France", limit=10, offset=0, years=None, increasing=False):
    noc = BDD_REGIONS.loc[BDD_REGIONS["region"] == region, "NOC"].values[0]
    if years is not None:
        bdd_e = BDD_EVENTS[BDD_EVENTS["Year"].isin(years)]
    else:
        bdd_e = BDD_EVENTS
    med_region = bdd_e[(bdd_e["NOC"] == noc) & (bdd_e["Medal"].notna())]
    #nombre de médailles gagnées par la France par sport
    nb_med_region = med_region.groupby(["Sport"]).size()
    nb_med_region_sorted = nb_med_region.sort_values(ascending=increasing)[
                           offset:offset+limit]
    print(nb_med_region_sorted)

plus_medailles()
