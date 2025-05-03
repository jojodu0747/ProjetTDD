# Identifier les pays qui ont le ratio nombre de médailles
# gagnées par des femmes sur nombre de médailles gagnées
# par des hommes le plus haut/le plus bas ?

from base_dd import BDD_EVENTS, BDD_REGIONS


def ratio_F_H(increasing=False, limit=10, offset=0, nb_med_min=10,
              years=None, group_by_region=False):
    BDD_EVENTS_filtre = BDD_EVENTS[BDD_EVENTS["NOC"] != "UNK"]
    BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["NOC"] != "IOA"]
    if years is not None:
        BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["Year"].isin(years)]
    if not group_by_region:
        # unstack sert à mettre F et M en variables et non en valeurs de Sex:
        bdd_pays_sexes = BDD_EVENTS_filtre.groupby(["NOC", "Sex"]).size().unstack(
            fill_value=0)
        bdd_pays_sexes = bdd_pays_sexes.merge(BDD_REGIONS[['NOC', 'region',
                                                           'notes']],
                                              on='NOC',
                                              how='left')
    else:
        bdd_pays_sexes = BDD_EVENTS_filtre.merge(BDD_REGIONS[['NOC', 'region',
                                                              'notes']],
                                                 on='NOC',
                                                 how='left')
        bdd_pays_sexes = bdd_pays_sexes.groupby(["region", "Sex"]).size().unstack(
            fill_value=0)

    bdd_pays_sexes = bdd_pays_sexes[
        bdd_pays_sexes["M"] + bdd_pays_sexes["F"] >= nb_med_min]
    # cette operation rendra float('Inf') si M = 0 :
    bdd_pays_sexes["Ratio_F_H"] = bdd_pays_sexes["F"] / bdd_pays_sexes[
        "M"]  # creation ratio

    if group_by_region:
        bdd_pays_sexes.columns.name = None
        bdd_pays_sexes.reset_index(inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(["region", "Ratio_F_H", "F", "M"],
                                                axis=1)
    else:
        bdd_pays_sexes.drop(columns=['NOC'], inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(
            ["region", "notes", "Ratio_F_H", "F", "M"], axis=1)

    bdd_pays_sexes.rename(columns={'region': 'Pays'}, inplace=True)
    pays_sexes_sorted = bdd_pays_sexes.sort_values(by="Ratio_F_H",
                                                   ascending=increasing)[offset:limit]
    print(pays_sexes_sorted)

ratio_F_H(increasing=True, group_by_region=True)