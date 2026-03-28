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


#keyword argument
#order does not matter
def employee_information(name,age,designation):
    print("name:",name)
    print("age:",age)
    print("designation:",designation)

employee_information(age=21,designation="student",name="Minar")

#to pass any no. of keyword argument
def fun(**keywordargument):
    print(keywordargument)
    print(type(keywordargument))

fun(name="Ravi",age=26,salery=10000)
# {'name': 'Ravi', 'age': 26, 'salery': 10000}
# <class 'dict'>


#default parameter
def country_name(country="India"):
    print(f"my country name is {country}")

country_name() # my country name is India
country_name("Russia") #my country name is Russia

def number(a,b=1): #default arguments are comes after non derfault arg
    print(a,b)

number(1) #1 1 
number(2,3)#2 3

#positional only argument
def fun(a,/,b): #(a,/) a is only positional argument
    print(a)
    print(b)
fun("hello",b=25)
fun("Minar",21)

def function(a,b,/,c): #both a,b are positional argument only
    print(a)
    print(b)
    print(c)
function(3,"Hello",c={3,4})
function(23,"Minar",[4,5,6])
#function(c="minar",354,"Hey") #error postional arg. always first

#keyword only argument
def fun(*,a):
    print(a)
fun(a=3)
#fun(5) #error

def fun2(a,*,b,c): #both b,c are keyword only arg
    print(a,b,c)
fun2(4,c="hey",b=9)
