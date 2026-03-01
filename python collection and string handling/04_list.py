#empty list 
lst=[]
lst1=list()

lst2=list("Hello")
print(lst2)#["H","e","l","l","o"]


#indexing
lst3=[[1,2,3,[4,5]],[6,[7,8]],9,10,11]
print(len(lst3))#5
print(lst3[0][1])#2
print(lst3[0][3][1])#5
print(lst3[-4][-1][-2])#7