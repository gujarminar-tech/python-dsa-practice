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

#slicing
lst1=["a","b","c","d","e","f","g","h","i","j"]
print(lst1[0:5])#['a', 'b', 'c', 'd', 'e']
print(lst1[2:9:2])#['c', 'e', 'g', 'i']
print(lst1[-4:9])#['g', 'h', 'i']