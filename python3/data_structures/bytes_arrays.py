lst = [1, 2, 3, 4]
print(type(lst))

b = bytes(lst)
print(type(b))
print(b)

b1 = bytearray(lst)
print(type(b1))
print(b1)

b1[2] = 33
print(b1)
