a=[4,"hello",10.4,[1,2]]
print(id(a))
print(id(a[0]))
# print(type(a))#list

a[0]=6
print(id(a[0]))
print(id(a))
print(a)# [6,"hello",...]
# elements in the list are mutable 
 
# a=[5,6,7,"hello"]
# print(id(a)) #address will change 
# list is immutable but elements in list are mutable