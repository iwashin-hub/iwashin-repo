#Pythonのリスト応用編

list_org=[['a',45],['b',78],['c',5],['d',69],['e',97]]

list_srted=sorted(list_org,key=lambda x: x[1])

print(list_srted)

list_comp=[x for x in list_org if x[1] > 70]

print(list_comp)

list_compandsort=sorted([x for x in list_org if x[1] < 70],key=lambda x: x[1],reverse=True)

print(list_compandsort)
