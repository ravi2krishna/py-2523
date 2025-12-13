# Laptop Contract: Govt Said these are must For Building Laptops 

# With Abstraction (With Abstract Class)

# Abstract Class
from abc import ABC, abstractmethod
class Laptop(ABC):
    
    # Abstract Methods 
    @abstractmethod
    def processor(self):
        pass
    
    @abstractmethod    
    def ram(self):
        pass
    
    @abstractmethod    
    def hdd(self):
        pass
    
    @abstractmethod    
    def nw(self):
        pass
        
# Implementations: -> Companies who wants to manufacture laptops
class Dell(Laptop):
    
    def processor(self):
        print("Dell Processor Working")
    
    def ram(self):
        print("Dell RAM Working")
    
    def hdd(self):
        print("Dell HDD Working")
        
    def nw(self):
        print("Dell Network Working")

class Lenovo(Laptop):
    
    def processor(self):
        print("Lenovo Processor Working")
    
    def ram(self):
        print("Lenovo RAM Working")
    
    def hdd(self):
        print("Lenovo HDD Working")
        
    def nw(self):
        print("Lenovo Network Working")

# End Users 
print("Customer Buying Dell Laptop")
dell = Dell()
# TypeError: Can't instantiate abstract class Dell without an implementation for abstract methods 'hdd', 'nw'
dell.processor()
dell.ram()

print("Customer Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.hdd()
lenovo.nw()

# laptop = Laptop() # Can't instantiate abstract class