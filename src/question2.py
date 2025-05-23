from base_dd import BDD_EVENTS
from modalite import REGION, NOC


def bornes(liste_sessions, type_medaille, combine):
    """Cette fonction répond à la question 2.
    Elle donne les bornes inférieures et supérieures du nombre de médailles obtenues
    parmi les nations, selon les types de médailles pris en compte, et selon les
    sessions prises en compte.

    Parameters
    __________

    liste_sessions : list[str]
        Liste des sessions prises en compte par la fonction

    type_medaille : list[str]
        Liste des médailles prises en compte

    combine : bool
        Si True le calcul est fait sur l'ensemble des sessions sinon il est fait
        par session

    Returns
    _______

    str
        La liste des couples ((argmin, min), (argmax, max)) pour chaque session ou pour
        l'ensemble des sessions selon combine.
    """
    df = BDD_EVENTS.loc[
        BDD_EVENTS['Medal'].isin(type_medaille)
        & BDD_EVENTS['Games'].isin(liste_sessions),
        ['ID', 'NOC', 'Games', 'Event', 'Medal']
        ]
    ag = df.groupby(['Event', 'Games', 'NOC', 'Medal']).count()
    if combine:
        ag = ag.groupby(['Games', 'NOC']).count()
        ag = (ag.groupby('NOC').sum())['ID']
        mini = (list(ag.iloc[[ag.argmin()]].index)[0], int(ag.min()))
        maxi = (list(ag.iloc[[ag.argmax()]].index)[0], int(ag.max()))
        res = [(mini, maxi)]
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
        ag = (ag.groupby(['Games', 'NOC']).count())['ID']
        res = []
        for session in liste_sessions:
            ag_s = ag[session]
            mini = (list(ag_s.iloc[[ag_s.argmin()]].index)[0], int(ag_s.min()))
            maxi = (list(ag_s.iloc[[ag_s.argmax()]].index)[0], int(ag_s.max()))
            res.append((mini, maxi))
        string = (
            f"{'Session':<11}|{'min/max':^7}|{'Region':<50}|{'Médailles':>9}\n" +
            "-"*80 + "\n"
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
