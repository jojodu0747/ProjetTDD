from base_dd import BDD_EVENTS
from modalite import YEAR


def evolution_femmes(annee=None):
    """Cette fonction répond à la question 9.
    Elle donne le pourcentage de femmes durant les épreuves de JO selon les années

    Parameters
    __________

    annee: list[int] | None
        Liste des années prises en compte,
        si None alors toutes les années sont prises en compte

    Returns
    _______

    str
        Tableau en string donnant le taux par année
    """
    if annee is None:
        annee = YEAR
    dfM = BDD_EVENTS.loc[
        BDD_EVENTS["Sex"].isin(["M"]) &
        BDD_EVENTS["Year"].isin(annee),
        ["ID", "Year"]].drop_duplicates()
    dfM = dfM.groupby("Year").count()
    dfF = BDD_EVENTS.loc[
        BDD_EVENTS["Sex"].isin(["F"]) &
        BDD_EVENTS["Year"].isin(annee),
        ["ID", "Year"]].drop_duplicates()
    dfF = dfF.groupby("Year").count()
    for x in annee:
        if x not in dfF.index:
            dfF.loc[x] = 0
        if x not in dfM.index:
            dfM.loc[x] = 0
    dfT = round(dfF/(dfF+dfM) * 100, 2)
    res = (
        f"{'Année':<10}|{'Proportion de Femmes':>30}\n" + "-" * 41 + "\n"
    )
    for x in annee:
        res += f"{x:<10}|{dfT.loc[x][0]:>30}\n"
    return res
