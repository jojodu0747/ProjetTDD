import csv
from base_dd import adresse

def count_medaille(nom):
    medal_count = 0
    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        spamreader = csv.reader(bdd_athlete)
        header = next(spamreader)
        idx_nom = header.index('Name')
        idx_medal = header.index('Medal')
        for row in spamreader:
            if row[idx_medal] != 'NA' and row[idx_nom] == nom:
                medal_count += 1
    return medal_count
 
print(count_medaille("Michael Fred Phelps, II"))
