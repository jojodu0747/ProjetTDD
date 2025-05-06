from base_dd import BDD_EVENTS


def question2(liste_sessions, type_medaille, combine=False):
    """Cette fonction répond à la question 2.
    Il donne les bornes inférieur et supérieur du nombre de médailles obtenue
    par chaque nation, selon les types de médailles pris en compte, et selon
    les sessions pris en compte.

    Parameters
    __________

    liste_sessions: list[str]
        Liste des sessions prises en compte par la fonction

    type_medaille: list[str]
        Liste des médailles pris en compte

    combine : bool
        Si le calcul est fait sur l'ensemble des sessions ou par session

    Returns
    _______

    list[tuple[tuple]]
        La liste des couple ((argmin, min), (argmax, max)) pour chaque session ou pour
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
        min = (list(ag.iloc[[ag.argmin()]].index)[0], int(ag.min()))
        max = (list(ag.iloc[[ag.argmax()]].index)[0], int(ag.max()))
        res = [(min, max)]
    else:
        ag = (ag.groupby(['Games', 'NOC']).count())['ID']
        res = []
        for session in liste_sessions:
            ag_s = ag[session]
            min = (list(ag_s.iloc[[ag_s.argmin()]].index)[0], int(ag_s.min()))
            max = (list(ag_s.iloc[[ag_s.argmax()]].index)[0], int(ag_s.max()))
            res.append((min, max))
    return res
