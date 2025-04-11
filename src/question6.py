from base_dd import BDD_EVENTS

BDD_EVENTS_medalists = BDD_EVENTS[BDD_EVENTS["Medal"].notna()]

# Calculer la moyenne d'âge par sexe
average_age_by_sex = BDD_EVENTS_medalists.groupby("Sex")["Age"].mean()

print(average_age_by_sex)
