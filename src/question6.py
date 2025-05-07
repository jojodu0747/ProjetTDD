from base_dd import BDD_EVENTS


def calculate_grouped_mean(
        df=BDD_EVENTS, filter_column="Medal", group_column="Sex", target_column="Age"
        ):
    """
    Calcule la moyenne d'une colonne (target_column) pour les lignes où
    filter_column n'est pas NaN, groupée par group_column.

    Parameters
    ----------
    df : pandas.DataFrame
        Le DataFrame sur lequel effectuer le calcul.
    filter_column : str
        Le nom de la colonne à filtrer (non NaN).
    group_column : str
        Le nom de la colonne par laquelle grouper les données.
    target_column : str
        Le nom de la colonne pour laquelle calculer la moyenne.

    returns
    -------
    {'M': float, 'F': float}
        Une série contenant la moyenne de target_column, groupée par group_column.
    """
    filtered_df = df[df[filter_column].notna()]
    grouped_mean = filtered_df.groupby(group_column)[target_column].mean()
    return {'M': round(float(grouped_mean['M']), 2),
            'F': round(float(grouped_mean['F']), 2)}
