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


#pop() method
s1={1,2,3}
s1.pop() 
#delete random value from set because set is unordered


#copy method
a={1,2,4}
b=a.copy()
b.add(3)
print(b)
print(a)

#union() method
a={1,2,4}
b={3,5,4}
c=a.union(b) #c={1,2,3,4,5}
print(c)
#len(c)<=len(a)+len(b)


#intersection() method
c=a.intersection(b) #c=a&b
print(c) #{4}


#intersection_update() method
a={1,2,3}
b={2,3,4}
a.intersection_update(b) 
# update a by removing uncommon elements between a and b
print(a)

#difference() method
a={1,2,3}
b={2,3,4}
c=a.difference(b) #a-b
print(c) #{1}


#difference_update() method
a={1,2,3}
b={2,3,4}
a.difference_update(b) #a=a-b
print(a) #{1}

#symmetric_difference() method
a={1,2,3}
b={2,3,4}
c=a.symmetric_difference(b) #a-b U b-a
print(c) #{1,4}