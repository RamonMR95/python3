"""""
lst = []

for x in range(1, 11):
    lst.append(x**3)
print(lst)
"""""


lst2 = [x**3 for x in range(1, 11)]
print(lst2)


lst3 = [x for x in range(2, 21, 2)]
print(lst3)


lst4 = [x for x in range(2, 21) if x % 2 == 0]
print(lst4)


lst5 = [1, 2, 3, 4, 5]
lst6 = [6, 7, 8, 9, 10]
z = []

'''for i in range(len(lst5)):
    z.append(lst5[i] * lst6[i])'''

z = [lst5[i] * lst6[i] for i in range(len(lst5))]

print(z)


# FIND ELEMENTS IN COMMON
a = [2, 4, 6, 8]
b = [1, 2, 3, 4]

'''result = []
for i in a:
    if i in b:
        result.append(i)'''

result = [i for i in a if i in b]
print(result)

