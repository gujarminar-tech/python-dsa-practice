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