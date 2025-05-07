from base_dd import BDD_EVENTS, BDD_REGIONS


def plus_medailles(noc="FRA", limit=10, offset=0, years=None, increasing=False):
    """
    Retourne un classement des sports dans lesquels il y a le plus d'athlètes médaillés
    d'un pays (region) donné.

    Parameters
    ----------
    noc : str
        NOC de la région pour laquelle on souhaite compter les médailles.
        Par défaut "FRA".
    limit : int
        Nombre maximal de résultats à retourner. Par défaut 10.
    offset : int
        Décalage dans la liste triée des sports. Par défaut 0.
    years : list[int] or None
        Liste d'années à prendre en compte.
        Si None, toutes les années sont prises en compte. Par défaut None.
    increasing : bool
        Si True, trie les sports par nombre croissant de médailles
        Sinon, décroissant. Par défaut False.

    Returns
    -------
    str
        Représente une un tableau (nom du sport, nombre de médailles), trie par le
        nombre de médailles selon le paramètre increasing.
    """
    if (not isinstance(years, list) or not all(isinstance(y, int) for y in years)) \
            and years is not None:
        raise TypeError("Le paramètre 'years' doit être une liste d'entiers.")

    region_values = BDD_REGIONS.loc[BDD_REGIONS["NOC"] == noc, "region"].values
    if len(region_values) == 0:
        raise ValueError(f"Le NOC '{noc}' n'existe pas dans la base de donnée.")

    region = region_values[0]
    if years is not None:
        bdd_e = BDD_EVENTS[BDD_EVENTS["Year"].isin(years)]
    else:
        bdd_e = BDD_EVENTS
    if len(bdd_e) == 0:
        raise ValueError(f"Pas de médaillés pour {region}({noc}) pour les année"
                         f"s {years}")

    med_region = bdd_e[(bdd_e["NOC"] == noc) & (bdd_e["Medal"].notna())]
    nb_med_region = med_region.groupby(["Sport"]).size()
    nb_med_region_sorted = nb_med_region.sort_values(ascending=increasing)[
                           offset:offset+limit]
    a = nb_med_region_sorted.reset_index(name="Nombre de médaillés")
    res = f"{'Sport':<20}|{'Nombre de médaillés':>20}\n" + "-" * 41 + "\n"
    for i in range(a.shape[0]):
        res += f"{a.loc[i][0]:<20}|{a.loc[i][1]:>20}\n"
    return res
