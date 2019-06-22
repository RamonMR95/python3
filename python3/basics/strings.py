# STRINGS
my_str = "My string"

print(my_str)
print(my_str[0])
print(my_str * 3)
print(len(my_str))

s1 = """str
comp"""

print(s1)

# SLICING
print(my_str[0:5])
print(my_str[0:])
print(my_str[:5])
print(my_str[-3:-1])
print(my_str[0:9:2])  # Jump = 2
print(my_str[15::-1])
print(my_str[::-1])

# TRIM
print(my_str.strip())  # Removes spacing from the left and right side
print(my_str.lstrip())  # Removes spacing from the left
print(my_str.rstrip())  # Removes spacing from the right
print(my_str.replace(" ", ""))  # Removing all the spaces

# SUBSTRING
print(my_str.find("str"))
print(my_str.find("str", 0, len(my_str)))
print(my_str.count("s"))

print(my_str.upper())
print(my_str.lower())
print(my_str.title())

