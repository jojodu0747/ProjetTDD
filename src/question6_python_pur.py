import csv
from base_dd import adresse, n_doublon


def moyenne_age_par_sexe():
    """
    Calcule la moyenne d'une colonne (target_column) pour les lignes où
    filter_column n'est pas NaN, groupée par group_column.

    returns
    -------
    {'M': float, 'F': float}
        Une série contenant la moyenne de target_column, groupée par group_column.
    """
    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        reader = csv.reader(bdd_athlete)
        header = next(reader)

        idx_sex = header.index('Sex')
        idx_age = header.index('Age')
        idx_medal = header.index('Medal')

        total_ages = {'M': 0.0, 'F': 0.0}
        total_counts = {'M': 0, 'F': 0}

        n = 2

        for row in reader:

            if n in n_doublon:
                n += 1
                continue
            n += 1
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
