# fruits=["Apple","Banana","Orange"]
# i=0
# n=len(fruits)
# while i<n:
#     print(fruits[i])
#     i+=1

# #break
# lst=[30,20,40,10,60,70,80]
# total=0
# for item in lst:
#     total+=item
#     if total>100:
#         break
#     print(total)

#continue
# a=[5,-3,2,4,-5,0,-6,9]
# for item in a:
#     if item<0:
#         continue
#     print(item)

# #pass 
# l1=[10,20,30,40,50]
# for a in l1:
#     if a>30:
#         pass #empty statement
#     print(a)

# else in loops 
l2=[10,20,30,40]
for item in l2:
    if item>40:
        break
    print(item)
else:
    print("Else block")