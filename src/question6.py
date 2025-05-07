from base_dd import BDD_EVENTS


def calculate_grouped_mean():
    """
    Calcule la moyenne d'une colonne (target_column) pour les lignes où
    filter_column n'est pas NaN, groupée par group_column.

    returns
    -------
    {'M': float, 'F': float}
        Une série contenant la moyenne de target_column, groupée par group_column.
    """
    df = BDD_EVENTS
    filter_column = "Medal"
    group_column = "Sex"
    target_column = "Age"
    filtered_df = df[df[filter_column].notna()]
    grouped_mean = filtered_df.groupby(group_column)[target_column].mean()
    return {'M': round(float(grouped_mean['M']), 2),
            'F': round(float(grouped_mean['F']), 2)}
