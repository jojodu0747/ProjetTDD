from base_dd import BDD_EVENTS

BDD_EVENTS_ETE_OR = BDD_EVENTS[
    (BDD_EVENTS["Games"].str.contains("Summer")) & (BDD_EVENTS["Medal"] == "Gold")
]

BDD_EVENTS_HIVER_OR = BDD_EVENTS[
    (BDD_EVENTS["Games"].str.contains("Winter")) & (BDD_EVENTS["Medal"] == "Gold")
]

print(BDD_EVENTS_ETE_OR["Age"].mean())
print(BDD_EVENTS_HIVER_OR["Age"].mean())
