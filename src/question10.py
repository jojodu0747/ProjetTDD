# Quel sont les sports où la France a gagné le plus de médaille ?
from base_dd import BDD_EVENTS

#bdd avec médailles gagnées par la France:
med_France = BDD_EVENTS[(BDD_EVENTS["NOC"] == "FRA") & (BDD_EVENTS["Medal"].notna())]

#nombre de médailles gagnées par la France par sport

nb_med_France = med_France.groupby(["Sport"]).size()
nb_med_France_sorted = nb_med_France.sort_values(ascending=False)
print(nb_med_France_sorted.head(10))

#idee 1 : choisir periode
# def f(x1, x2, ..., periode = None)
