import matplotlib.pyplot as plt
import pandas as pd
from question7 import compter_medailles_par_continent
from question3 import top_nations_par_sport
from base_dd import BDD_EVENTS

#Question 1 
print(top_nations_par_sport("Athletics Men's Long Jump", 1700, 2016, 5))
#print(top_nations_par_sport("Athletics men's Jump", 90, 2300, 5))

#Question 7

# Obtenir la liste des années disponibles
annees = sorted(BDD_EVENTS["Year"].dropna().unique())

# Créer une DataFrame vide pour stocker les résultats
resultats = pd.DataFrame()

# Remplir le tableau pour chaque année
for annee in annees:
    data = compter_medailles_par_continent(annee, BDD_EVENTS)
    resultats[annee] = data

# Transposer pour avoir les années en lignes
resultats = resultats.T.fillna(0)

# Tracer le graphique
plt.figure(figsize=(14, 7))
resultats.plot(kind='bar', stacked=True, colormap='tab20', figsize=(15, 7))

plt.title("Répartition des médailles par continent au fil des années")
plt.xlabel("Année")
plt.ylabel("Nombre de médailles")
plt.legend(title="Continent", bbox_to_anchor=(0.99, 1), loc='upper left')
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.6)
#plt.show()


print(BDD_EVENTS.sort_values(by="Year").head(10)['Year'])