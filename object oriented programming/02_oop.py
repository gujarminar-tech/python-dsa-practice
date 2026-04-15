#Access modifier 
'''
Type      | name    |access
Public    | name    |accessed anywhare
protected | _name   |access in class and subclass
private   | __name  |access only inside the class
'''


#Polymorphism
#function overriding is an example of polymorphism
class Animal:
    def sound(self):
        print("Hello")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("meow")

obj1=Dog()
obj1.sound() #Bark
obj2=Cat()
obj2.sound() #meow