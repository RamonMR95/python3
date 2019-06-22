# DECLARING A SET
s = {1, 2, 3, 4}
print(type(s))
print(s)

# ADDING A VALUE
s.update([88, 90])
print(s)

# REMOVING A VALUE
s.remove(2)
print(s)

# FROZEN SET
fs = frozenset(s)
print(fs)
c1 = frozenset({'pradera', 2, 'pimiento'})
print(c1)