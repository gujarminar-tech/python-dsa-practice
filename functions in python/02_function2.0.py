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