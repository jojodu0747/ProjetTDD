from base_dd import BDD_EVENTS, BDD_REGIONS
import numpy as np
import pandas as pd

df = BDD_EVENTS.copy()

SEX = ['M', 'F']
MEDAL = ['Bronze', 'Silver', 'Gold']
SPORT = list(np.sort(df.loc[~df['Sport'].isna(), 'Sport'].unique()))
GAMES = list(np.sort(df.loc[~df['Games'].isna(), 'Games'].unique()))
YEAR = list(np.sort(df.loc[~df['Year'].isna(), 'Year'].unique()))
EVENT = list(np.sort(df.loc[~df['Event'].isna(), 'Event'].unique()))
SEASON = list(np.sort(df.loc[~df['Season'].isna(), 'Season'].unique()))
df = BDD_REGIONS.copy()

apart = ['IOA', 'ROT', 'UNK']
df.loc[df['notes'].isna(), 'notes'] = 0
df.loc[df['NOC'] == 'ROT', 'region'] = df.loc[df['NOC'] == 'ROT', 'notes']
df.loc[df['NOC'] == 'TUV', 'region'] = df.loc[df['NOC'] == 'TUV', 'notes']
df.loc[df['NOC'] == 'UNK', 'region'] = df.loc[df['NOC'] == 'UNK', 'notes']
df.loc[df['NOC'] == 'ROT', 'notes'] = 0
df.loc[df['NOC'] == 'TUV', 'notes'] = 0
df.loc[df['NOC'] == 'UNK', 'notes'] = 0
df.loc[df['NOC'] == 'IOA', 'notes'] = 0
df1 = df.loc[~df['NOC'].isin(apart)]
df2 = df.loc[df['NOC'].isin(apart)]
df1 = df1.sort_values(by='region')
df = pd.concat([df1, df2], axis=0)
noc = list(df['NOC'])
region = list(df['region'])
notes = list(df['notes'])
REGION = []
for i in range(len(noc)):
    if notes[i] == 0:
        REGION.append(region[i]+", "+noc[i])
    else:
        REGION.append(region[i]+", "+noc[i]+", "+notes[i])
del df, df1, df2, noc, region, notes
