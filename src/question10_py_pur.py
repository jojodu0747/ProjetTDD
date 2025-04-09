import time
import csv
from base_dd import adresse

with open(adresse + "athlete_events.csv", 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        pass
