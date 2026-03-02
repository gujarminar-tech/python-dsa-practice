#adding the element in the list
#append() method
lst1=[1,2,3,4]
lst1.append("Hello")
print(lst1)

#insert method
lst1.insert(2,[5,6])
print(lst1)

#extend() methiod 
#it append each element of iterable obj. at end
lst2=[1,2,3]
lst2.extend("Hey")
print(lst2)#[1, 2, 3, 'H', 'e', 'y']
lst2.extend([4,5,6])
print(lst2)#[1, 2, 3, 'H', 'e', 'y', 4, 5, 6]


#list as input from user
lst1=input("Enter values : ").split()
print(lst1) 
#but the only problem is each element is in string form

lst2=[]
count=int(input("Enter number of values: "))
for i in range(count):
    lst2.append(int(input("enter value: ")))
print(lst2)
