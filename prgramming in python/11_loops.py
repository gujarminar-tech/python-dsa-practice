# #enumerate
# list=[10,20,30,40,50]
# for idx,val in enumerate(list):
#     print(idx,val)

# #nested list
# list1=[["Virat","Rohit"],["Sachin","Dhoni"],["Hardik","Surya"]]
# for a in list1:
#     for b in a:
#         print(b)

# #zip
# parties=["Congress","BJP","X"]
# Seats=[100,200,50]
# for a,b in zip(parties,Seats):
#     print(a,b)

# parties=["Congress","BJP","X","Y"]
# Seats=[100,200,50]
# for a,b in zip(parties,Seats):
#     print(a,b)
# # no. of loops=min{len(parties),len(Seats)}

List=[10,20,30,40]
tuple=(11,23,45)
set={10,22,34,53}
str="Minar"

for a,b,c,d in zip(List,tuple,set,str):
    print(a,b,c,d)