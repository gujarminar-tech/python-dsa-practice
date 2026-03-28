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
