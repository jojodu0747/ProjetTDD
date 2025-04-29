import csv
from base_dd import adresse


def plus_medailles_pur(region="France", limit=10, offset=0):
    noc = ""
    dic_nb_sport = {}
    with open(adresse + "noc_regions.csv", 'r', newline='') as bdd_regions:
        sprd_reg = csv.reader(bdd_regions)
        header_reg = next(sprd_reg)  #rend le header et l'"enlève" du spamreader
        idx_noc_reg = header_reg.index('NOC')  #indices de ces variables dans noc_regions
        idx_region = header_reg.index('region')
        for row in sprd_reg:
            if row[idx_region] == region:  #on trouve le noc correspondant à region
                noc = row[idx_noc_reg]
                break

    with open(adresse + "athlete_events.csv", 'r', newline='') as bdd_athlete:
        spamreader = csv.reader(bdd_athlete)
        header = next(spamreader)
        idx_NOC = header.index('NOC')  #indices de ces variables dans athlete_event
        idx_medal = header.index('Medal')
        idx_sport = header.index('Sport')
        for row in spamreader:  #on parcourt la bdd, row est un individu
            if row[idx_medal] != 'NA' and row[idx_NOC] == noc:
                sport = row[idx_sport]
                if sport in dic_nb_sport:
                    dic_nb_sport[sport] += 1
                else:
                    dic_nb_sport[sport] = 1

    dict_items = sorted(dic_nb_sport.items(), key=lambda x: -x[1])  #tri croissant selon la valeur
    # il faudra faire un dict_item[offset:limit]
    print(f"{'Sport':<20} {'Nombre de médailles':>20}")
    print("-" * 40)
    i = 0
    for item in dict_items:
        i += 1
        if i >= offset:
            print(f"{item[0]:<20} {item[1]:>20}")
        if i > limit:
            break

plus_medailles_pur()
