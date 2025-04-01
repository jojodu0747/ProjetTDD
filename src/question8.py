# Identifier les pays qui ont le ratio nombre de médailles
# gagnées par des femmes sur nombre de médailles gagnées
# par des hommes le plus haut/le plus bas ?

from base_dd import BDD_EVENTS, BDD_REGIONS
BDD_EVENTS_filtre = BDD_EVENTS[BDD_EVENTS["NOC"] != "UNK"]  #supprime pays inconnus
#unstack sert à mettre F et M en variables et non en valeurs de Sex:
bdd_pays_sexes = BDD_EVENTS_filtre.groupby(["NOC", "Sex"]).size().unstack(fill_value=0)

if len(bdd_pays_sexes[(bdd_pays_sexes["M"] == 0)]) != 0:
    print("Dans ces pays, seules des femmes ont gagné des médailles:", bdd_pays_sexes[(bdd_pays_sexes["M"] == 0)])
    bdd_pays_sexes = bdd_pays_sexes[(bdd_pays_sexes["M"] != 0)]

bdd_pays_sexes["Ratio_F_H"] = bdd_pays_sexes["F"] / bdd_pays_sexes["M"]  #creation ratio
bdd_pays_sexes.sort_values(by="Ratio_F_H", ascending=False, inplace=True)

bdd_pays_sexes = bdd_pays_sexes.merge(BDD_REGIONS[['NOC', 'region', 'notes']], on='NOC', how='left')
bdd_pays_sexes.rename(columns={'region': 'Pays'}, inplace=True)
bdd_pays_sexes.drop(columns=['NOC'], inplace=True)
bdd_pays_sexes = bdd_pays_sexes.reindex(["Pays", "notes", "Ratio_F_H", "F", "M"], axis=1)

print("Ces pays ont le ratio F/H le plus haut : \n", bdd_pays_sexes.head(10))
print("Ces pays ont le ratio F/H le plus bas : \n", bdd_pays_sexes.tail(10))

#idee 2 : choisir le nombre medailles min (notion de représentativité)
#idee 3 : periode (f(x1,x2,...,periode=None))
