def fun(a,b):
    '''fun method is used to sum of 2 values'''
    return a+b
help(fun)

#local variables
'''the variables which are defined inside any function 
and they belong to that funtion. they can not be 
accessed outside funtion'''

def fun():
    a=100
    print(a)
fun()
#print(a) error

#global variables
'''global variables are the variables which are defined outside the funtion 
and can be accessed anywhere inthe program(inside and outside the funtion)'''
a=10
def fun():
    print(a)
fun() #10
print(a) #10

b=50 #global variables
def fun():
    b=60 #local variables
    print(b)
fun()
print(b)

d=500
def fun():
    # d=d+100 #error
    '''bydefault function can access the global varible 
    but can't modify it'''
    print(d)
fun() #500
print(d) #500

e=200
def fun():
    global e
    e=e+100
    print(e)
print(e) #200
fun() #300
print(e) #300

def func():
    global g #global variable created inside function
    g=300
    print(g)
func()
print(g)


#Nested Function
def outer():
    a=10
    b=30
    def inner():
        print(a,b) #inner func can access outer func variables
    inner()

outer()
#inner() #only access inside outer functions

def outerfunc():
    x=5
    def innerfunc():
        print(x)
    return innerfunc

a=outerfunc() #a=innerfunc
a() #a()=innerfunc()

def multiplier(factor):
    def multify_by(x):
        return x*factor
    return multify_by
a=multiplier(2)
print(a(6))


#recursion function
'''whenever the function calls itself,it is called recursion
and the function is called recursive funtion'''

def fun(n):
    if n>0:
        print(n)
        fun(n-1)
fun(10)

def func(n):
    if n>0:
        print(n,end=" ")
        func(n-1)
        print(n,end=" ")
        #5 4 3 2 1 1 2 3 4 5
func(5)
print()

#sum upto nth integer
def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)
print(fun(5)) #15

#factorier
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
print(fact(4)) #24