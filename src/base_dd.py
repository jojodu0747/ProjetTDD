import os
import pandas as pd
import csv

adresse = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
           + "/donnees_jeux_olympiques/")

BDD_EVENTS = pd.read_csv(adresse + "athlete_events.csv")
BDD_REGIONS = pd.read_csv(adresse + "noc_regions.csv")

<<<<<<< HEAD
=======
BDD_EVENTS.drop_duplicates()

BDD = []
ID = "1"
n_doublon = set()
n_ligne = 2
header = True

with open(adresse + "athlete_events.csv", 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if header is True:
            header = False
            continue
        elif row[0] != ID:
            BDD = [row]
            ID = row[0]
            n_ligne += 1
            continue
        elif row in BDD:
            n_doublon.add(n_ligne)
            n_ligne += 1
        else:
            BDD.append(row)
            n_ligne += 1

del BDD, ID, n_ligne, header


# n_doublon correspond à l'ensemble des lignes qui sont des doublons
# (1 étant la ligne du header)
>>>>>>> bea903d3ab2dad74d552946d4fd36e4e6eefd9c5
