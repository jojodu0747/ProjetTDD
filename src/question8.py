from base_dd import BDD_EVENTS, BDD_REGIONS


def ratio_F_H(increasing=False, limit=10, offset=0, nb_med_min=10,
              years=None, group_by_region=False):
    """
    Calcule le ratio de participantes femmes par rapport aux hommes pour chaque pays en
    fonction du nombre total de médailles remportées.

    Parameters
    ----------
    increasing : bool
        Si True, trie les résultats par ratio croissant. Sinon, décroissant.
        Par défaut False.
    limit : int
        Nombre maximal de résultats à retourner. Par défaut 10.
    offset : int
        Décalage dans la liste triée des résultats. Par défaut 0.
    nb_med_min : int
        Nombre minimum de médailles requise (femmes et hommes) pour être inclus
        dans le classement. Par défaut 10.
    years : list[int] or None
        Liste d’années à prendre en compte.
        Si None, toutes les années sont prises en compte. Par défaut None.
    group_by_region : bool
        Si True, regroupe les résultats par region (pays actuel) au lieu de par NOC.
        Par défaut False.

    Returns
    -------
    pandas.DataFrame
        Un DataFrame contenant les colonnes :
        - "Country" : nom du pays ou de la région
        - "Ratio_F_H" : ratio F / M
        - "F" : nombre de participantes femmes
        - "M" : nombre de participants hommes
        - "notes" : note associée au pays (si group_by_region=False)
        Le DataFrame est trié par ratio_F_H selon le paramètre increasing
    """

    BDD_EVENTS_filtre = BDD_EVENTS[BDD_EVENTS["NOC"] != "UNK"]
    BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["NOC"] != "IOA"]
    if years is not None:
        BDD_EVENTS_filtre = BDD_EVENTS_filtre[BDD_EVENTS_filtre["Year"].isin(years)]
    if len(BDD_EVENTS_filtre) == 0:
        raise ValueError(f"Pas de données pour les années {years}.")
    if not group_by_region:
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
        "M"]

    if group_by_region:
        bdd_pays_sexes.columns.name = None
        bdd_pays_sexes.reset_index(inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(["region", "Ratio_F_H", "F", "M"],
                                                axis=1)
    else:
        bdd_pays_sexes.drop(columns=['NOC'], inplace=True)
        bdd_pays_sexes = bdd_pays_sexes.reindex(
            ["region", "notes", "Ratio_F_H", "F", "M"], axis=1)

    bdd_pays_sexes.rename(columns={'region': 'Country'}, inplace=True)
    pays_sexes_sorted = bdd_pays_sexes.sort_values(by="Ratio_F_H",
                                                   ascending=increasing)[
                                                    offset:offset+limit]
    return pays_sexes_sorted


# réponses à la question
print(ratio_F_H())
print(ratio_F_H(increasing=True))
