# Identifier les pays qui ont le ratio nombre de médailles
# gagnées par des femmes sur nombre de médailles gagnées
# par des hommes le plus haut/le plus bas ?

from base_dd import BDD_EVENTS
bdd_pays_sexes = BDD_EVENTS.groupby(["NOC", "Sex"]).size()
print(bdd_pays_sexes)