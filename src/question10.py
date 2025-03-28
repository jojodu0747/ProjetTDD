# Quel sont les sports où la France a gagné le plus de médaille ?
import pandas as pd
from base_dd import BDD_EVENTS

#bdd avec médailles gagnées par la France:
med_France = BDD_EVENTS[(BDD_EVENTS["Team"] == "FRA") & (BDD_EVENTS["Medal"].notna())]

#nombre de médailles gagnées par la France
nb_med_France