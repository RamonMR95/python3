import re

s = "Take up one idea.One idea only"

# FINDING THE FIRST SUBSTRING THAT MATCHES THE REGEX
res = re.search(r'o\w\w', s)
print(res.group())


# FINDING ALL THE SUBSTRINGS THAT MATCH THE REGEX
res2 = re.findall(r'o\w\w', s)
print(res2)


# TESTING IF THE STRING MATCHES THE REGEX
res3 = re.match(r'T\w\w', s)
print(res3.group())


# SPLITTING
res4 = re.split(r'\.', s)
print(res4)


# REPLACING ONE STRING FOR ANOTHER
res5 = re.sub(r'one', 'two', s)
print(res5)


# QUANTIFIERS
res6 = re.findall(r'O\w{2,}', s)
print(res6)

