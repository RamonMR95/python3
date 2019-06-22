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

# REMOVING ALL ELEMENTS
my_list.clear()

# FUNCTIONS
my_list2 = [10, 23, 30.5]
print(max(my_list2))
print(min(my_list2))
my_list2.sort()
print(my_list2)
my_list2.sort(reverse=True)
print(my_list2)


list_var = [12, 24]
print(list_var)

list_var.append(5)
print(list_var)

list_var.pop()
list_var.pop(1)
print(list_var)





