from base_dd import BDD_EVENTS


def calculate_grouped_mean(df, filter_column, group_column, target_column):
    """
    Calcule la moyenne d'une colonne (target_column) pour les lignes où
    filter_column n'est pas NaN, groupée par group_column.

    Parameters:
    - df: DataFrame à analyser
    - filter_column: colonne sur laquelle appliquer la condition de
    non-nullité
    - group_column: colonne utilisée pour le regroupement
    - target_column: colonne dont on veut la moyenne

    Returns:
    - Serie pandas avec la moyenne par groupe
    """
    filtered_df = df[df[filter_column].notna()]
    grouped_mean = filtered_df.groupby(group_column)[target_column].mean()
    return grouped_mean


avg_by_sexe = calculate_grouped_mean(BDD_EVENTS, "Medal", "Sex", "Age")
print(avg_by_sexe)
