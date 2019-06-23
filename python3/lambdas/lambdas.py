from functools import reduce

f = lambda n: n**3
print(f(2))


l = lambda x: 'YES' if x % 2 == 0 else 'NO'
print(l(10))
print(l(9))


l2 = lambda a, b: a + b
print(l2(10, 20))


# FILTER
lst = [1, 2, 3, 4, 5]
res = list(filter(lambda x: x % 2 == 0, lst))
print(res)


# MAP
lst2 = [1, 2, 3, 4, 5]
res2 = list(map(lambda n: n * 2, lst2))
print(res2)


# REDUCE
lst3 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, lst3)
print(result)
