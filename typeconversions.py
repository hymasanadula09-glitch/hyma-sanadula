#list-tuple
my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

 #tuple-list
my_tuple = (5,6,7,)
my_list = list(my_tuple)
print(my_list)
print(type(my_list))

 #list-set
my_list = [1,2,2,3,3,4]
my_set = set(my_list)
print(my_set)
print(type(my_set))

#set-list
my_set = {10,20,30} 
my_list = list(my_set)
print(my_list)

#dictinary-list of keys
student = {'name':'john', 'age':20, 'grade':'A'}
keys_list = list(student.keys())
print(keys_list)

#dictionary-list of values
student = {'name':'john','age':20,'grade':'A'}
values_list = list(student.values())
print(values_list)

#dictionary-list of items
student = {'name':'john','age':20}
items_list = list(student.items())
print(items_list)