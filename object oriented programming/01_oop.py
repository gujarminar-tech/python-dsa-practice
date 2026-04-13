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