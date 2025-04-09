from base_dd import BDD_EVENTS

Q1 = BDD_EVENTS[
    (BDD_EVENTS["Name"].str.contains("Michael Fred Phelps, II", case=False))
].dropna()
print(len(Q1))


# #en python base

# medal_count = 0
# for ligne in BDD_EVENTS:
#     a,b = ligne['Name'], ligne['Medal']
#     if "Michael Fred Phelps, II" == a and b != 'Na' :
#         medal_count += 1

# print(medal_count)
