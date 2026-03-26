#immutable
#ordered 
#indexing
#slicing

#tuple Initialization
t1=()
t1=tuple()
t2=(1)
print(type(t2)) #<class 'int'>
t3=1,
print(type(t3)) #<class 'tuple'>
t4=(1,)
print(type(t4)) #<class 'tuple'>
t5=1,2,3,4
print(type(t5)) #<class 'tuple'>


#tuple Unpacking
a,b,c=(1,2,3)
print(a)
print(b)
print(c)
a,*b,c=(1,3,4,5,6)
print(b) #[3,4,5]
print(a) #1
print(c) #6