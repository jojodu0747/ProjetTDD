import pandas as pd
import os

adresse = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
           + "/donnees_jeux_olympiques/")

BDD_EVENTS = pd.read_csv(adresse + "athlete_events.csv")
BDD_REGIONS = pd.read_csv(adresse + "noc_regions.csv")

print(BDD_EVENTS.describe())
