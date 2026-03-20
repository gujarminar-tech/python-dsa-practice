'''mutable
unordered
duplicates are not allowed
imp* In setr only immutable objects are allowed 
mutrable objects are not allowed like (List,dist,set)
'''

s1={1,0,True,False,0,0.0}
#initialize empty set
set1=set() 
print(type(set1))

#add() method 
set1={3,9,2,4,7}
set1.add(1)
print(set1)

#update() method
set2={4,3,2}
set2.update({0,5,6})
print(set2)

set2.update("Gate")
print(set2)


#remove method
s1={1,3,2}
s1.remove(3)
print(s1)
#s1.remove(5) #error


#discard() method
s2={3,4,2}
s2.discard(3)
print(s2)
s2.discard(5) #can't give error even if element is not in set


