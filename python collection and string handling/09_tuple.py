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

#accessing elements in tuple
t1=(1,2,3,4)
print(t1[1])
print(t1[-2])
print(t1[1:3]) #(2, 3)

list=[10,20,30,40,50]
t2=(1,2,list)
print(t2)
list[0]=30
print(t2) #(1, 2, [30, 20, 30, 40, 50])
#tuple can store mutable values
t2[2][1]=60
print(t2) #(1, 2, [30, 60, 30, 40, 50])
# t2[2]=[30,80] #error\
