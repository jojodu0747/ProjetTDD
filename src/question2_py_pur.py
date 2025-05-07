from base_dd import adresse, n_doublon
import csv
from modalite import REGION, NOC


def bornes_p(liste_sessions, type_medaille, combine):
    """Cette fonction répond à la question 2.
    Elle donne les bornes inférieures et supérieures du nombre de médailles obtenues
    par chaque nation, selon les types de médailles pris en compte, et selon
    les sessions prises en compte.

    Parameters
    __________

    liste_sessions: list[str]
        Liste des sessions prises en compte par la fonction

    type_medaille: list[str]
        Liste des médailles pris en compte

    combine : bool
        Si True le calcul est fait sur l'ensemble des sessions sinon il est fait
        par session

    Returns
    _______

    str
        La liste des couples ((argmin, min), (argmax, max)) pour chaque session ou pour
        l'ensemble des sessions selon combine.
    """
    med_occ = {i: {j: {} for j in type_medaille} for i in liste_sessions}
    res_p = {i: dict() for i in liste_sessions}

    with open(adresse + "athlete_events.csv", 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        first = True
        n_ligne = 2
        for row in spamreader:
            if first:
                first = False
                continue
            if n_ligne in n_doublon:
                n_ligne += 1
                continue
            if (row[8] in liste_sessions and
                    row[-1] in type_medaille and row[7] not in res_p[row[8]].keys()):
                res_p[row[8]][row[7]] = 1
                med_occ[row[8]][row[-1]][row[7]] = [row[13]]
            elif (row[8] in liste_sessions and row[-1] in type_medaille and
                    row[7] not in med_occ[row[8]][row[-1]].keys()):
                res_p[row[8]][row[7]] += 1
                med_occ[row[8]][row[-1]][row[7]] = [row[13]]
            elif (row[8] in liste_sessions and row[-1] in type_medaille and
                    row[13] not in med_occ[row[8]][row[-1]][row[7]]):
                res_p[row[8]][row[7]] += 1
                med_occ[row[8]][row[-1]][row[7]].append(row[13])
            n_ligne += 1
    if combine:
        res_somme = {}
        res_min = None
        res_max = None
        for ses in liste_sessions:
            for i in res_p[ses].keys():
                if i not in res_somme.keys():
                    res_somme[i] = res_p[ses][i]
                else:
                    res_somme[i] += res_p[ses][i]
        for noc in res_somme.keys():
            if res_min is None:
                res_min = (noc, res_somme[noc])
            elif res_somme[noc] < res_min[1] or (res_somme[noc] == res_min[1] and
                                                 noc < res_min[0]):
                res_min = (noc, res_somme[noc])
            if res_max is None:
                res_max = (noc, res_somme[noc])
            elif res_somme[noc] > res_max[1] or (res_somme[noc] == res_max[1] and
                                                 noc < res_max[0]):
                res_max = (noc, res_somme[noc])
        res = [(res_min, res_max)]
        string = (
            f"{'min/max':^7}|{'Region':<50}|{'Médailles':>9}\n" + "-"*68 + "\n"
        )
        string += (
            f"{'max':^7}|{REGION[NOC.index(res[0][1][0])]:<50}|"
            f"{res[0][1][1]:>9}\n"
        )
        string += (
            f"{'min':^7}|{REGION[NOC.index(res[0][0][0])]:<50}|"
            f"{res[0][0][1]:>9}\n"
        )
        string += "-"*68 + "\n"
    else:
        res_min = {i: [] for i in liste_sessions}
        res_max = {i: [] for i in liste_sessions}
        for s in liste_sessions:
            for noc in res_p[s].keys():
                if len(res_min[s]) == 0:
                    res_min[s] = [noc, res_p[s][noc]]
                elif res_p[s][noc] < res_min[s][1] or (res_p[s][noc] == res_min[s][1]
                                                       and noc < res_min[s][0]):
                    res_min[s] = [noc, res_p[s][noc]]
                if len(res_max[s]) == 0:
                    res_max[s] = [noc, res_p[s][noc]]
                elif res_p[s][noc] > res_max[s][1] or (res_p[s][noc] == res_max[s][1]
                                                       and noc < res_max[s][0]):
                    res_max[s] = [noc, res_p[s][noc]]
        res = []
        for s in liste_sessions:
            res.append((tuple(res_min[s]), tuple(res_max[s])))
        string = (
            f"{'Session':<11}|{'min/max':^7}|{'Region':<50}|{'Médailles':>9}\n" + "-"*80 + "\n"
        )
        for i, x in enumerate(res):
            string += (
                f"{liste_sessions[i]:<11}|{'max':^7}|{REGION[NOC.index(x[1][0])]:<50}|"
                f"{x[1][1]:>9}\n"
            )
            string += (
                f"{'':<11}|{'min':^7}|{REGION[NOC.index(x[0][0])]:<50}|"
                f"{x[0][1]:>9}\n"
            )
            string += "-"*80 + "\n"
    return string
