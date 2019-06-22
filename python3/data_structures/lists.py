# DECLARING A LIST
my_list = [10, 23, 'Ramón', 30.5]
print(my_list)
print(my_list[2])
print(my_list[0:2])
print(my_list[-3:-1])
print(my_list * 4)
print(len(my_list))

# ADDING AN ELEMENT
my_list.append(40)
print(my_list)
my_list.insert(0, "First")
print(my_list)


# REMOVING AN ELEMENT
my_list.remove(10)
del(my_list[2])
print(my_list)

