import os

adresse = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
           + "/donnees_jeux_olympiques/")

with open(adresse + 'athlete_events.csv', 'r', newline='') as csvfile:
  print("test")
