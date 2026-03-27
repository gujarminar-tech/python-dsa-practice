def pythonfuntion():
    print("Hello")
    l1=[1,3,4,5,6]
    return(l1)
a=pythonfuntion() #when we call funtion it print hello 
print(a) # it print only the rerturn value

#positional argument
def employee_info(age,name):
    print("name :",name)
    print("age :",age)
    # this funtion bydefault return none.

a=employee_info(21,"Minar")
print(a) #None

#to pass any no. of positinal argument
def fun(*args): #it consider multiple input as one tuple
    print(args)
    print(type(args))

fun(1,10.5,"Hello",[1,2,3])
# (1, 10.5, 'Hello', [1, 2, 3])
# <class 'tuple'>