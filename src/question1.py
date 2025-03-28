from base_dd import BDD_EVENTS

Q1 = BDD_EVENTS[
    (BDD_EVENTS["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
print(len(Q1))
