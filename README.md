# ProjetTDD

Projet traitement de données Ensai 1a

## Table des matières

- [Introduction](#introduction)
- [Utilisation](#utilisation)

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
(au dessus de src) et ces dernières apparaissent dans des fichier textes.
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

Pour obtenir une réponse aux questions il suffit de submit puis d'exectuter et le
résultat apparait.
pour sauvegarder nos résultats il suffit de cliquer sur sauvegarder  **après**
avoir executer.

Pour la **régression logistique** : la méthode est comme suit:

    1. D'abord on choisit un ou plusieurs sport avec la rubrique **choix des sports**

    2. Ensuite on entraine notre modèle en cliquant sur **Entrainer**

    3. Choisir les charactéristique de son athlète et les **submit** unes à unes

    4. **Excecuter** et on obtient le resultat
