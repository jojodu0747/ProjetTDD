from base_dd import BDD_EVENTS
from modalite import SPORT
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


def modelerl(Sport=None):
    """Cette fonction répond à la Partie 2.
    Il renvoie un modèle de regression linéaire

    Parameters
    __________

    Sport: lis[str] | None
        Liste des sports pris en compte dans l'entrainement
        None = Tout les sports

    Returns
    _______

    LogisticRegression
        Un modèle entrainé sur la base de donnée
    """
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

    # Equilibre
    df = df.copy()
    df_1 = df[df["Medal"] == 1]
    df_0 = df[df["Medal"] == 0]
    if df_0.shape[0] > df_1.shape[0]:
        df_0_sampled = df_0.sample(n=len(df_1))
        df_1_sampled = df_1.copy()
    else:
        df_1_sampled = df_1.sample(n=len(df_0))
        df_0_sampled = df_0.copy()
    df = pd.concat([df_1_sampled, df_0_sampled], axis=0)
    X = df.drop(columns='Medal')
    Y = df['Medal']
    Y = np.round(Y).astype(int)

    # Apprentissage
    model = LogisticRegression(solver='newton-cg')
    model.fit(X, Y)

    return model


def prevision(modele, Age, Height, Weight, NOC, Sex):
    """Cette fonction prédit les résultat de x selon le modèle

    Parameters
    __________

    modele: LogisticRegression

    Age: int

    Height: int

    Weight: int

    NOC: str

    Sex: str

    Returns
    _______

    int
        0 si non medaillé, 1 sinon
    """
    x = {"Age": Age,
         "Height": Height,
         "Weight": Weight,
         "NOC": NOC,
         "Sex": Sex
         }
    variable_quali = ['NOC', 'Sex']
    df = BDD_EVENTS.loc[:, ["Age", "Height", "Weight", "NOC", "Sex"]]
    x = {"Age": Age,
         "Height": Height,
         "Weight": Weight,
         "NOC": NOC,
         "Sex": Sex
         }
    df = pd.concat([df, pd.DataFrame([x])], ignore_index=True)
    df = pd.get_dummies(df, columns=variable_quali, drop_first=True, dtype=int)
    x = df.tail(1)
    return int(modele.predict(x)[0])
