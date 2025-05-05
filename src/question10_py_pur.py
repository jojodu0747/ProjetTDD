import csv
from base_dd import adresse, n_doublon


def plus_medailles_pur(region="France", limit=10, offset=0, years=None,
                       increasing=False):
    """
    Retourne les sports dans lesquels les athlètes d'un pays (region) donné ont
    remporté le plus de médailles.

    Parameters
    ----------
    region : str
        Nom de la région pour laquelle on souhaite compter les médailles.
        Par défaut "France".
    limit : int
        Nombre maximal de résultats à retourner. Par défaut 10.
    offset : int
        Décalage dans la liste triée des sports. Par défaut 0.
    years : list[int] or None
        Liste d'années à filtrer.
        Si None, toutes les années sont prises en compte. Par défaut None.
    increasing : bool
        Si True, trie les sports par nombre croissant de médailles
        Sinon, décroissant. Par défaut False.

    Returns
    -------
    list[tuple]
        Une liste de tuples (nom du sport, nombre de médailles), triée par le
        nombre de médailles selon le paramètre increasing.
    """
    noc = ""
    dic_nb_sport = {}
    with open(adresse + "noc_regions.csv", 'r', newline='') as bdd_regions:
        sprd_reg = csv.reader(bdd_regions)
        header_reg = next(sprd_reg)  # rend le header et l'"enlève" du spamreader
        idx_noc_reg = header_reg.index(
            'NOC')  # indices de ces variables dans noc_regions
        idx_region = header_reg.index('region')
        for row in sprd_reg:
            if row[idx_region] == region:  # on trouve le noc correspondant à region
                noc = row[idx_noc_reg]
                break
        if noc == "":
            raise ValueError(f"Le pays '{region}' n'existe pas dans la base de donnée.")

    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        spamreader = csv.reader(bdd_athlete)
        header = next(spamreader)
        idx_NOC = header.index('NOC')  # indices de ces variables dans athlete_event
        idx_medal = header.index('Medal')
        idx_sport = header.index('Sport')
        idx_year = header.index('Year')
        n_ligne = 2
        for row in spamreader:  # on parcourt la bdd, row est un individu
            if n_ligne in n_doublon:
                n_ligne += 1
                continue
            n_ligne += 1
            if row[idx_medal] != 'NA' and row[idx_NOC] == noc \
                    and (years is None or row[idx_year] in years):
                sport = row[idx_sport]
                if sport in dic_nb_sport:
                    dic_nb_sport[sport] += 1
                else:
                    dic_nb_sport[sport] = 1
    if increasing:
        list_items = sorted(dic_nb_sport.items(), key=lambda x: x[1])
    else:
        list_items = sorted(dic_nb_sport.items(), key=lambda x: -x[1])
    list_items = list_items[offset:offset + limit]
    return list_items


# réponse à la question
rep = plus_medailles_pur()
print(f"{'Sport':<20} {'Nombre de médailles':>20}")
print("-" * 40)
for item in rep:
    print(f"{item[0]:<20} {item[1]:>20}")
