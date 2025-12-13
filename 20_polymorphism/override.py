# Overriding 

class Animal:
    def sound(self):
        print("Parent Makes Sound")
        
class Dog(Animal):
    def sound(self): # override
        print("Dog Makes Woff Sound")
        
class Cat(Animal):
    def sound(self): # override
        print("Cat Makes Meow Sound")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()