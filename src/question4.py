from base_dd import BDD_EVENTS


def age_moyen_medailles(type_jo, type_medaille, annee_debut, annee_fin):
    """
    Cette fonction répond à la question 4.
    Elle calcule l'âge moyen des athlètes ayant remporté une médaille d'or
    lors des Jeux Olympiques d'été ou d'hiver.

    parameters
    __________

    type_jo : str
        Le type de Jeux Olympiques ("Summer" ou "Winter").

    type_medaille : str
        Le type de médaille ("Gold").

    annee_debut : int
        L'année de début de la période à considérer.

    annee_fin : int
        L'année de fin de la période à considérer.

    returns
    _______

    float
        L'âge moyen des athlètes ayant remporté une médaille d'or
        lors des Jeux Olympiques spécifiés.

    """
    # Filtrer les données en fonction du type de Jeux Olympiques et de la médaille
    BDD_EVENTS_FILTRE = BDD_EVENTS[
        (BDD_EVENTS["Games"].str.contains(type_jo, case= False)) & (BDD_EVENTS["Medal"] == type_medaille) &
        (BDD_EVENTS["Year"].between(annee_debut, annee_fin))
    ]

    # Calculer et retourner l'âge moyen
    return BDD_EVENTS_FILTRE["Age"].mean()

print("Âge moyen des médaillés d'or aux JO d'été :",age_moyen_medailles("Summer", "Gold", 1896, 2016))
print("Âge moyen des médaillés d'hiver aux JO d'hiver :", age_moyen_medailles("Winter", "Gold", 1896, 2016))
