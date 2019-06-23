list1 = [100, 200, 300]

for i in list1:
    print(i)

for i in range(0, 3):
    print(i)

for i in range(0, 5, 2):
    print(i)

res = 0
for i in range(1, 4):
    for j in range(1, 4):
        res += i * j

print(f'Result : {res}')


myList = [1, 2]
anotherList = [9, 7]


for i in range(0, len(myList)):
    print(i)

for item in myList:
    print(item)

for x in myList:
    for y in anotherList:
        print(x, y)

for i in range(0, 3):
    print(i)

for i in range(0, 5, 2):
    print(i)
