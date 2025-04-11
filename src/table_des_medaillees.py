from base_dd import BDD_EVENTS
import pandas as pd
import numpy as np

# création de la fonction qui restreint une table au sport

# affichage des différents sports (dans la doc et peut être utile dans les condtions de succès de la fonction)
BDD_EVENTS["Sport"].drop_duplicates().tolist()

print(BDD_EVENTS["Sport" == ['Ski Jumping', 'Volleyball']])

def table_par_sport (L):
    for a in L:
    BDD_EVENTS["Sport"][f"{a}"]