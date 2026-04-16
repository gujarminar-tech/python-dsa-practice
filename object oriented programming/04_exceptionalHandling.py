#exception handling

# a= 10
# b= 0
# print(a+b) #10
# print(a/b) #zero divison error
# # python stops when error occuors 
# print(a-b) 

'''
try : the try block is used to enclose the code 
      in which error may occur. It is like a safety 
      net that is used t catch the error.

except : the except block used to handle the exception 
         raised in try block. You can specify the type
         of exception you want to catch
'''

a=10
b=0
try: 
    print(a/b)
except Exception as e:
    print("Exception is :",e)

print(a+b)

try :
    l1=[10,20,30,40,50]
    a=int(input("Enter a value: "))
    i=l1.index(a)
    print(i)
    print(a/i)
except ZeroDivisionError:
    print("can not divide by zero")
except ValueError:
    print("this value is not in list")
except Exception as e:
    print(e)
'''
Enter a value: 100
this value is not in list

Enter a value: 10
0
can not divide by zero'''

#finally : get execute irrespective of whether the 
#          exception came or not

try :
    a=10
    b=int(input("Enter a number: "))
    c=a/b
    print(c)
except Exception as e:
    print(e)
finally :
    print("Hello")

'''
Enter a number: 0
division by zero
Hello

Enter a number: 2
5.0
Hello
'''

#Else : executed when there is no exception.
try : 
    a=5
    d=1
    c=a/d
    print(c)
except Exception as e:
    print(e)
else :
    print("no error")
finally :
    print("Hello")

#5.0
#no error
#Hello