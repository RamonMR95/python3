# DECLARING A TUPLE, CANNOT BE MODIFIED
tup = (1, 2, 3, "XYZ")
print(type(tup))
print(tup)
print(tup[1])
print(tup.count(1))
print(tup.index(1))


lst = [67, 23]
print(type(lst))
tup2 = tuple(lst)
print(tup2)


tup = (1, 2)
print(tup)

tup2 = ((1, 2), (3, 4))
print(tup2[0])
print(tup2[0][0])

tup2 += (2, 2)
print(tup2)