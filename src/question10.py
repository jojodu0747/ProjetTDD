# Quels sont les sports où la France a gagné le plus de médaille ?
from base_dd import BDD_EVENTS
from base_dd import BDD_REGIONS

def plus_medailles(region="France", limit=10, offset=0):
    noc = BDD_REGIONS.loc[BDD_REGIONS['region'] == region, "NOC"].iloc[0]
    noc = BDD_REGIONS.loc[BDD_REGIONS["region"] == region, "NOC"].values[0]
    med_region = BDD_EVENTS[(BDD_EVENTS["NOC"] == noc) & (BDD_EVENTS["Medal"].notna())]
    #nombre de médailles gagnées par la France par sport
    nb_med_region = med_region.groupby(["Sport"]).size()
    nb_med_region_sorted = nb_med_region.sort_values(ascending=False)[offset:limit]
    print(nb_med_region_sorted)

plus_medailles()
#idee 1 : choisir periode
# def f(x1, x2, ..., periode = None)