# ProjetTDD

Projet traitement de données Ensai 1a

## Table des matières

- [Prérequis](#prérequis)
- [Introduction](#introduction)
- [Utilisation](#utilisation)

## Prérequis

- Écran d'au minimum 1680x1050pixels
- Python 3.13.1
- Installer Numpy, Pandas, Matplotlib.pyplot, Levenshtein et sklearn
- Posséder les bases de données et les mettre dans un dossier du même niveau que source et qui se nomme “donnees_jeux_olympiques”

## Introduction

Notre projet de traitement de données se décompose en trois parties:

- la réponse aux questions
- la regression logistique
- l'interface graphique

## Utilisation

### la réponse aux questions

les questions sont numérotés de 1 à 10 dans le dossier src. Nous avons généralisés
toutes nos réponses en des questions à partir de ces dernières. d'où les noms des
fichiers en question et pas en réponse.
Certaines fonctions ont été faites en doublons en utilisant pandas et python_pur.

Pour obtenir les réponses aux questions il faut se rendre dans le dossier sauvegarde
et ces dernières apparaissent dans des fichier textes, les réponses à la question
de base est affiché tout en haut du fichier.
Les questions explicites sont présentes dans l'interface (cf suite)

### La regression logistique

La régression logistique se retrouve dans les fichiers pythons commançant pas reg.

Pour utiliser la regression logistique on peut se servir de l'interface (cf suite).

Un exemple d'utilisation de la regression logistique a été repertorié dans le fichier
**reglog.txt** dans le dossier **sauvegarde**.
On y a entrainé le jeux de données du basket, et pour un joueur américain d'1m99, de 89
kilos et de 25ans, le modèle de régression le donne gagnant.

### L'interface

L'interface se lance via 'run' dans le fichier main.
Point important pour avoir pleinemement accès à l'interface il est d'avoir une
résolution de 1680x1050.

Choisissez la question à laquel vous voulez une réponse et cochez les cases concernant
les codes en python pur ou la personnalisation des arguments si vous le souhaitez.
Si vous décidez de personnaliser les arguments, de nouveaux widgets apparaitront et
vous devez entrer les valeurs, pour obtenir une réponse aux questions il suffit de
submit puis d'exectuter et le résultat apparait, sinon si vous utilisez les arguments
de base il suffit d'éxecuter (sauf pour la page de la regression).
pour sauvegarder nos résultats il suffit de cliquer sur sauvegarder  **après**
avoir executer.

Pour la **régression logistique** : la méthode est comme suit:

    1. D'abord on choisit un ou plusieurs sport avec la rubrique **choix des sports**

    2. Ensuite on entraine notre modèle en cliquant sur **Entrainer**

    3. Choisir les charactéristique de son athlète et les **submit** unes à unes

    4. **Excecuter** et on obtient le resultat

**ATTENTION**: Certaines boîtes de sélections, malgré que l’on puisse choisir autant
de valeurs que l’on souhaite, ne devraient pas dépasser 2 sélections. (Q3 et
4 concernant les boites d'année de début et de fin)
