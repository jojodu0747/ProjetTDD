import csv
from base_dd import adresse


def moyenne_age_par_sexe():
    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        reader = csv.reader(bdd_athlete)
        header = next(reader)

        idx_sex = header.index('Sex')
        idx_age = header.index('Age')
        idx_medal = header.index('Medal')

        total_ages = {'M': 0.0, 'F': 0.0}
        total_counts = {'M': 0, 'F': 0}

        for row in reader:
            medal = row[idx_medal]
            age = row[idx_age]
            sex = row[idx_sex]

            if medal != 'NA' and age != 'NA':
                try:
                    age_val = float(age)
                    if sex in total_ages:
                        total_ages[sex] += age_val
                        total_counts[sex] += 1
                except ValueError:
                    continue

        moyennes = {}
        for sexe in total_ages:
            if total_counts[sexe] > 0:
                moyennes[sexe] = round(total_ages[sexe] / total_counts[sexe], 2)
            else:
                moyennes[sexe] = None

        return moyennes


print(moyenne_age_par_sexe())
