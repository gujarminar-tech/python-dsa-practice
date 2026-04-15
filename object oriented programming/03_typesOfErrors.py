#types of errors
'''
Syntax error : this type of error occurs whenevers 
               there is a issue in syntax of code
               eg. if a>b  #syntax error for :
                    print("hello")

Indentation error : improper indentation 
                    eg. if a>b:
                        print("Hello") #indentation error

type error : value is not of expected type.
             eg. a="3"
                 b=7
                 print(a+b) #type error

Value error : value is not in the expected range or format
             eg. x="abcd"
                 a=int(x) #value error
                 l1=[10,20,30,40]
                 l1.index(100) #value error

Zero Division error : Whenever you try to divide by zero

Name error : try to access a varible which is not defined yet
              eg. print(a) #name error

attribute error : try t access an attribute that doesn't exists
              eg. s1="Hello"
                  s1.reverse() #attribute error

Index error : try to access an index which is out of range
              eg. l1=[10,20,30,40]
                  print(l1[6]) #Index error 
'''