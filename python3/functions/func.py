def average(a, b):
    return (a + b) / 2


print(average(2, 5))


def calc(a, b):
    x = a + b
    y = a - b
    z = a * b
    u = a / b

    return x, y, z, u


print(calc(1, 2))

for i in calc(1, 2):
    print(i)


# KEYWORD ARGS
def avg(a, b):
    return (a * b) / 2


print(avg(b=2, a=3))


# OPTIONAL ARGS
def avg2(a=10, b=20):
    return (a * b) / 2


print(avg2(a=30))

