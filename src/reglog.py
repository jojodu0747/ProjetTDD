from base_dd import BDD_EVENTS
from modalite import SPORT
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


def modelerl(Sport=None):
    if Sport is None:
        Sport = SPORT
    variable_qanti = ['Age', 'Height', 'Weight']
    variable_quali = ['NOC', 'Sex']
    variable = variable_quali + variable_qanti
    df = BDD_EVENTS.loc[:, variable + ['Medal']]
    df = pd.get_dummies(df, columns=variable_quali, drop_first=True, dtype=int)
    df.loc[df['Medal'].isna(), 'Medal'] = 0
    df.loc[df['Medal'] != 0, 'Medal'] = 1

    # Filtrage
    df = df[BDD_EVENTS['Sport'].isin(Sport)]
    df = df.dropna(axis=0, how='any')

    # Eq
    df = df.copy()
    df_1 = df[df["Medal"] == 1]
    df_0 = df[df["Medal"] == 0]
    dfa_0_sampled = df_0.sample(n=len(df_1), random_state=42)
    df = pd.concat([df_1, dfa_0_sampled], axis=0).sample(
        frac=1, random_state=42).reset_index(drop=True)
    X = df.drop(columns='Medal')
    Y = df['Medal']
    Y = np.round(Y).astype(int)
    YG = Y[df['Medal'] == 1]
    XG = X[df['Medal'] == 1]


    model = LogisticRegression(solver='newton-cg')
    model.fit(X, Y)

    return model.score(X, Y), model.score(XG, YG)

print(modelerl(Sport=["Basketball"]))
