param_d = [False, "Athletics Men's Long Jump", [1896, 2016], 5]
param = param_d.copy()
l_param = [param_d, param]
def transforme(l_param):
    l1, l2 = l_param[0], l_param[1]
    l1a = [*l1[:2], *l1[2], l1[3]]
    l2a = [*l2[:2], *l2[2], l2[3]]
    return [l1a, l2a]

print(transforme(l_param))
