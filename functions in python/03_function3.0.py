#nested recursive
def NR(n):
    if n>100:
        return n-10
    return NR(NR(n+11))
print(NR(95))

def func_A(n):
    if n>0:
        print(n)
        func_B(n//2)
def func_B(n):
    if n>0:
        print(n)
        func_A(n-1)
func_A(20)    

def fun(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 3
    return n + fun(n-1) +fun(n-2)
print(fun(6))

def count(dict1,i):
    if i not in dict1.keys():
        return 1
    ans=1
    for j in  dict1[i]:
        ans+=count(dict1,j)
    return ans

dict1={}
dict1[0]=[1,2]
dict1[1]=[3,4,5]
dict1[2]=[6,7,8]
print(count(dict1,0)) #9

def count(n,jumps):
    if n==0:
        return 1
    total =0
    for j in jumps:
        if n-j>=0:
            total+=count(n-j,jumps)
    return total
jumps=[1,3,5]
print(count(4,jumps)) #3

def f(n):
    if n==0:
        return 0
    return f(n-1) + g(n-1)
def g(n):
    if n==0:
        return 1
    return g(n-1) +f(n)
g(g(2))