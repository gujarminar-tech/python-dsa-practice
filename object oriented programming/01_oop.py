class Car:
    def __init__(self,color,model,brand):
        self.brand=brand
        self.color=color
        self.model=model

car1=Car("Red","Nexon","Tata")

class student:
    def __init__(self,name,rollno,x):
        self.name=name
        self.rollno=rollno
        self.cls=x
stud1=student("Minar",2,"8th")


#Core Principles of OOP
'''
Encapsulation
Inheritance
Polymorphism
Abstraction
'''

#Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def display(self):
        print(self.balance)

b1=BankAccount(1000)
b1.deposit(500)
b1.display() #1500
b1.withdraw(200)
b1.display() #1300


#Inheritance
'''
when one class wants to inherit the properties or methods 
of another class, it is called inheritance.
'''
class A:
    def eat(self):
        print("Eating")
class B:
    def sleep(self):
        print("sleeping")

obj1=A()
obj2=B()

obj1.eat() #Eating
# obj2.eat() #error
# obj1.sleep() #error

class C:
    def playing(self):
        print("Football")
class D(C):
    def studing(self):
        print("Maths")

ob3=D()
obj4=C()

ob3.playing()
# obj4.studing() #error
#


#types of inheritance
'''
simple 
multiple
multilevel
hierarchical
hybrid
'''

#simple inheritance
class S1():
    def fun1(self):
        print("parent class")
class S2(S1):
    def fun2(self):
        print("child class")
a1=S2()
a1.fun1() #parent class

#multiple inheritance
class MP1():
    def funMP1(self):
        print("Parent Class 1")
class MP2():
    def funMP2(self):
        print("Parent Class 2")
class MP3(MP1,MP2):
    def funMP3(self):
        print("Child class with 2 parents")

obj5=MP3()
obj5.funMP1()
obj5.funMP2()
obj5.funMP3()

#multilevel Inheritance
class ML1():
    def funML1(self):
        print("One")
class ML2(ML1):
    def funML2(self):
        print("Two")
class ML3(ML2):
    def funML3(self):
        print("Three")

obj6=ML3()
obj6.funML1() #One
obj7=ML2()
# obj7.funML3() #error
