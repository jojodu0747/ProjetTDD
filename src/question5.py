from base_dd import BDD_EVENTS
from modalite import YEAR


def question5(medaille=['Gold'], annee=None):
    """Cette fonction répond à la question 5.
    Il est donne les personnes la plus et la moin agée ayant une médaille selon une
    période donnée

    Parameters
    __________

    medaille list[str]
        Liste des medailles prises en compte

    annee: list[int] | None
        Liste des années prises en compte,
        si None alors toutes les années sont prises en compte

    Returns
    _______

    str
        Tableau en string donnant les personnes les plus et moin
        agées ayant eu une médaille
    """
    if annee is None:
        annee = YEAR
    df = BDD_EVENTS.loc[
        BDD_EVENTS["Medal"].isin(medaille) &
        BDD_EVENTS["Year"].isin(annee),
        ["Name", "Age", "Medal"]]
    max = df[df["Age"] == df["Age"].max()]
    min = df[df["Age"] == df["Age"].min()]
    res = f"{'':<5}|{'Nom':<90}|{'Age':>4}|{'Medal':>10}\n" + "-" * 112 + "\n"
    res += (
        f"{'max':<5}|{max["Name"].iloc[0]:<90}|"
        f"{int(max["Age"].iloc[0]):>4}|{max["Medal"].iloc[0]:>10}\n"
        )
    res += (
        f"{'min':<5}|{min["Name"].iloc[0]:<90}|"
        f"{int(min["Age"].iloc[0]):>4}|{min["Medal"].iloc[0]:>10}\n"
        )
    return res
