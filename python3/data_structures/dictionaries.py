# DECLARING A DICTIONARY
my_dict = {1: "One", 2: "Two"}
print(my_dict)

print(my_dict.items())
print(my_dict.keys())

# GETTING ALL THE KEYS
k = my_dict.keys()
for i in k:
    print(i)

# GETTING ALL THE VALUES
v = my_dict.values()
for i in v:
    print(i)

print(my_dict[1])

# REMOVING AN ELEMENT
del my_dict[1]
print(my_dict)

# COPYING THE DICT
my_dict2 = my_dict.copy()

# ADDING AN ENTRY
my_dict[3] = "Three"
print(my_dict)

# UPDATING AN ENTRY
my_dict[3] = "TTTTHREE"
print(my_dict)


my_dict = {'One': 1, 1: 'One'}
print(my_dict)

print(my_dict.get('One'))

my_dict['One'] = '2'
print(my_dict)

my_dict['Three'] = 3;
print(my_dict)
