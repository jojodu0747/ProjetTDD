from base_dd import BDD_EVENTS


def question2(liste_sessions, type_medaille, combine):
    """Cette fonction répond à la question 2.
    Il donne les bornes inférieur et supérieur du nombre de médailles obtenue par chaque
    nation, selon les types de médailles pris en compte, et selon les sessions pris en
    compte.

    Parameters
    __________

    liste_sessions: list[tuple]
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
        ['ID', 'Team', 'Games', 'Medal']
        ]
    if combine:
        ag = df.groupby('Team')['Medal'].count()
        min = (list(ag.iloc[[ag.argmin()]].index)[0], int(ag.min()))
        max = (list(ag.iloc[[ag.argmax()]].index)[0], int(ag.max()))
        res = [(min, max)]
    else:
        res = []
        for session in liste_sessions:
            ag = (df.loc[df['Games']
                         == session].groupby(['Team', 'Games'])['Medal'].count())
            min = (list(ag.iloc[[ag.argmin()]].index)[0][0], int(ag.min()))
            max = (list(ag.iloc[[ag.argmax()]].index)[0][0], int(ag.max()))
            res.append((min, max))
    return res
