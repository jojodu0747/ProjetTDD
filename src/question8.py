# Identifier les pays qui ont le ratio nombre de médailles
# gagnées par des femmes sur nombre de médailles gagnées
# par des hommes le plus haut/le plus bas ?

from base_dd import BDD_EVENTS, BDD_REGIONS


def ratio_F_H(nb_med_min=10, group_by_region=False, summer=True, winter=True):
    BDD_EVENTS_filtre = BDD_EVENTS[BDD_EVENTS["NOC"] != "UNK"]  # on filtre les pays inconnus
    BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["NOC"] != "IOA"]
    if not summer:
        BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["Season"] != "Summer"]
    if not winter:
        BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["Season"] != "Winter"]
    # unstack sert à mettre F et M en variables et non en valeurs de Sex:
    if not group_by_region:
        bdd_pays_sexes = BDD_EVENTS_filtre.groupby(["NOC", "Sex"]).size().unstack(fill_value=0)
        bdd_pays_sexes = bdd_pays_sexes.merge(BDD_REGIONS[['NOC', 'region', 'notes']], on='NOC', how='left')
    else:
        bdd_pays_sexes = BDD_EVENTS_filtre.merge(BDD_REGIONS[['NOC', 'region', 'notes']], on='NOC', how='left')
        bdd_pays_sexes = bdd_pays_sexes.groupby(["region", "Sex"]).size().unstack(fill_value=0)

    if len(bdd_pays_sexes[(bdd_pays_sexes["M"] == 0)]) != 0:
        print("Dans ces pays, seules des femmes ont gagné des médailles:", bdd_pays_sexes[(bdd_pays_sexes["M"] == 0)])
        bdd_pays_sexes = bdd_pays_sexes[(bdd_pays_sexes["M"] != 0)]

    bdd_pays_sexes = bdd_pays_sexes[bdd_pays_sexes["M"] + bdd_pays_sexes["F"] >= nb_med_min]
    bdd_pays_sexes["Ratio_F_H"] = bdd_pays_sexes["F"] / bdd_pays_sexes["M"]  # creation ratio
    bdd_pays_sexes.sort_values(by="Ratio_F_H", ascending=False, inplace=True)

    if group_by_region:
        bdd_pays_sexes.columns.name = None
        bdd_pays_sexes.reset_index(inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(["region", "Ratio_F_H", "F", "M"], axis=1)
    else:
        bdd_pays_sexes.drop(columns=['NOC'], inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(["region", "notes", "Ratio_F_H", "F", "M"], axis=1)

    bdd_pays_sexes.rename(columns={'region': 'Pays'}, inplace=True)

    print("Ces pays ont le ratio F/H le plus haut : \n", bdd_pays_sexes.head(10))
    print("Ces pays ont le ratio F/H le plus bas : \n", bdd_pays_sexes.tail(10))


ratio_F_H()

# idee 3 : periode (f(x1,x2,...,periode=None))