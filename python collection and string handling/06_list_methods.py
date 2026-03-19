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

lst1=[10,20,30]
a,b,c=lst1
print(a)
print(b) 
print(c)

a,*b,c=[10,20,30,40,50]
print(a)
print(b)
print(c)


#list comprehension
# list comprehention tells that ,without using 
lst1=[]
for i in range(1,1001):
    lst1.append(i)
#use 
lst1=[i for i in range(1,1001)]
#print(lst1) #[1,2,3,....,1000]
lst2=[i*2 for i in range(1,11)]
print(lst2)
l1=[i+5 for i in range(1,6)]
print(l1)
l1=[i for i in range(1,11) if i%2==0]
print(l1) #[2,4,6,8,10]
l2=[i+5 if i%2==0 else i+10 for i in range(1,5)]
print(l2) #[11, 7, 13, 9]
l3=[(i,j) for i in range(1,3) for j in range(1,3)] 
#works like nested loop
print(l3)


#sort() & sorted() method
l1=[9,2,3,8,4,6,0,11]
l1.sort() #inplace changes
print(l1)
l1.sort(reverse=True)
print(l1)
l2=[3,4,15,7,3,2,9,0]
a=sorted(l2) #create a copy and store into diff variable
print(a)
b=sorted(l2,reverse=True)
print(b)

