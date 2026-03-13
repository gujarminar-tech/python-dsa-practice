#remove() method
l1=[10,20,30,40]
l1.remove(30) #delete through value
print(l1)
#l1.remove(50) # give error if value not present


#del
l2=[10,20,30,40,50,60,70]
del l2[1] # delete through index
print(l2)
del l2[2:4]
print(l2)
del l2[:] #delete all values from list but list exists
print(l2)
del(l2)
#print(l2)#error


#clear() method
l1=[10,20,30,40]
l1.clear()
print(l1)

#pop() method
l1=[10,20,30,40]
a=l1.pop(1) #pop delete value of that index and return value
print(l1)
b=l1.pop() # by default it delete  last value 
#pop()=pop(-1)
print(b)
print(l1)
l1.pop(0)
print(l1)

