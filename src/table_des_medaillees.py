from base_dd import BDD_EVENTS
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# création de la fonction qui restreint une table auX sport

# affichage des différents sports (dans la doc et peut être utile dans les condtions
# de succès de la fonction)
print(BDD_EVENTS["Sport"].drop_duplicates().tolist())
print(BDD_EVENTS.columns)
L = ["a", "b", "c"]
"|".join(L)


def table_par_sport(L):
    return BDD_EVENTS[BDD_EVENTS["Sport"].isin(L)]


X = table_par_sport(
    ["Judo", "Football", "Badminton", "Gymnastics", "Fencing", "Basketball"]
)[["Height","Sport"]].dropna()
X = pd.DataFrame(X)

print(X)

df = pd.DataFrame(X)

# Transformer la variable qualitative 'Sport' en variable numérique
label_encoder = LabelEncoder()
df["Sport"] = label_encoder.fit_transform(df["Sport"])

# Appliquer l'algorithme des K-means
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(df[["Height", "Sport"]])

# Visualiser les résultats
plt.scatter(df["Height"], df["Sport"], c=df["Cluster"], cmap="viridis")
plt.xlabel("Height")
plt.ylabel("Sport")
plt.title("K-means Clustering")
plt.show()
