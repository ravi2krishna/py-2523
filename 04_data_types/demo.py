# Data Types 

# Numeric Types 
data = 10
print(type(data))

data = -10
print(type(data))

data = 10.5
print(type(data))

data = -10.5
print(type(data))

# data = 3+i5 # NameError
# print(type(data))

data = 3 + 5j
print(type(data))

# String Type
data = "good morning"
print(type(data))

# Boolean Type
data = True 
print(type(data))
data = False 
print(type(data))

# None Type
data = None 
print(type(data))

# List Type
data = [10,20,30,40,50,10]
# data = ["hello","hey","hi",True,10.5,None]
# print(data)
print(type(data))
print(data)
print(len(data))

# Tuple Type
data = (10,20,30,40,50,10)
print(type(data))
print(data)
print(len(data))

# Set Type 
data = {10,20,30,40,50,10}
print(type(data))
print(data)
print(len(data))

# FrozenSet Type
data = frozenset({10,20,30,40,50,10})
print(type(data))

# Dictionary Type
data = {"name":"ravi","age":25,"city":"hyd"}
print(type(data))

# Custom Data Type : Store Student Info 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_gpa = 9.5
    
data = Student() # object 
print(type(data))

# Type Conversion -> automatically done 
n1 = 10
n2 = 5.5
sum = n1 + n2
print(sum)
print(type(sum))

# Type Casting 
final_price = 1256.3 # float 
print(final_price)
print(type(final_price))
final_price_int = int(final_price)
print(final_price_int)
print(type(final_price_int))

# some user in a web page was filling a form which has some rating (form data strings)
rating = "4"
rating = int(rating)

if rating < 5: # TypeError: '<' not supported between instances of 'str' and 'int'
    print("Customer Not Satisfied")
else:
    print("Customer Satisfied")