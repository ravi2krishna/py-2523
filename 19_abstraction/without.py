# Laptop Contract: Govt Said these are must For Building Laptops 

# Without Abstraction

# Concrete Classes (Normal Classes)
class Laptop:
    
    # Concrete Methods(Normal Methods)
    def processor(self):
        print("Laptop Processor Working")
    
    def ram(self):
        print("Laptop RAM Working")
        
    def hdd(self):
        print("Laptop HDD Working")
        
    def nw(self):
        print("Laptop Network Working")
        
# Implementations: -> Companies who wants to manufacture laptops
class Dell(Laptop):
    
    def processor(self):
        print("Dell Processor Working")
    
    def ram(self):
        print("Dell RAM Working")

class Lenovo(Laptop):
    
    def hdd(self):
        print("Lenovo HDD Working")
        
    def nw(self):
        print("Lenovo Network Working")

# End Users 
print("Customer Buying Dell Laptop")
dell = Dell()
dell.processor()
dell.ram()

print("Customer Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.hdd()
lenovo.nw()