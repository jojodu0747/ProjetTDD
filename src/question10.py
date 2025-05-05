from base_dd import BDD_EVENTS, BDD_REGIONS


def plus_medailles(region="France", limit=10, offset=0, years=None, increasing=False):
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
        Liste d'années à prendre en compte.
        Si None, toutes les années sont prises en compte. Par défaut None.
    increasing : bool
        Si True, trie les sports par nombre croissant de médailles
        Sinon, décroissant. Par défaut False.

    Returns
    -------
    pandas.DataFrame
        Un DataFrame contenant les colonnes nom du sport et nombre de médailles,
        trié par le nombre de médailles selon le paramètre increasing.
    """
    noc_values = BDD_REGIONS.loc[BDD_REGIONS["region"] == region, "NOC"].values
    if len(noc_values) == 0:
        raise ValueError(f"Le pays '{region}' n'existe pas dans la base de donnée.")
    noc = noc_values[0]
    if years is not None:
        bdd_e = BDD_EVENTS[BDD_EVENTS["Year"].isin(years)]
    else:
        bdd_e = BDD_EVENTS
    med_region = bdd_e[(bdd_e["NOC"] == noc) & (bdd_e["Medal"].notna())]
    nb_med_region = med_region.groupby(["Sport"]).size()
    nb_med_region_sorted = nb_med_region.sort_values(ascending=increasing)[
                           offset:offset+limit]
    return nb_med_region_sorted.reset_index(name="Nombre de médailles")


# réponse à la question
print(plus_medailles())
