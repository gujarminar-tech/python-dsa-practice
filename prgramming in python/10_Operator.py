a=10
# a//=3 #3
# a%=3 #1
# a**=2 #100
# print(a)

x=5 
y=10
# print(x>5 and y>8) #False
# print(x<6 and y==10) #True
# print (2 and 5 and 7) #7
# print(3 and 0 and 5) #0
# print(7 or 0 or 3) #7
# print(3 or 0 and 4) #3
# print(4 and 5 or 3) #5

#bitwise operator
# print(14 & 21) #4
# print(14 | 21) #31
# print(14 ^ 21) #27
# print(~13) #-14 
# print(15<<1) #30
# print(14>>2) #3

#membership operator
players = ["Virat","Rohit","Sachin"]
# print("Sachin" in players) #True
# print("Virat" not in players) #False
# print("Dhoni" in players) #False

#Identity operator
L1=[1,2,3]
L2=[1,2,3]
L3=L1
# print(L1 is L2) #False
# print(L1 is L3) #True
# print(L2 is L3) #False
 
#operator precedence
print(2**3**2)