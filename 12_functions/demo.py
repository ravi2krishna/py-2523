# Functional Style Programming 

# Without Functions 

a = 10
b = 5

# math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

a = 20
b = 10

# Repeat math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

a = 300
b = 100

# Repeat math operations 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("=" * 10)

# With Functions 
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = 10
b = 5
math_ops()
print("=" * 10)
a = 20
b = 10
math_ops() # calling function multiple times
print("=" * 10)
a = 300
b = 100
math_ops() # calling function multiple times
# math_ops(30,10) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# Using parameters with functions 
def math_ops(a,b): # a & b are parameters 
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'

math_ops(10,5)
print("=" * 10)
math_ops(20,10)
print("=" * 10)

# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info("ravi","ravi@gmail.com","hyderabad")
employee_info("hyderabad","ravi@gmail.com","ravi")

# Keywords Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info(emp_location="hyderabad",emp_email="ravi@gmail.com",emp_name="ravi")

# No Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_email="ravi@gmail.com",emp_name="ravi",org_name="Google")
employee_info(emp_location="pune",emp_email="krishna@gmail.com",emp_name="krishna",org_name="Google")
employee_info(emp_location="bangalore",emp_email="mike@gmail.com",emp_name="mike",org_name="Google")

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="hyderabad",emp_email="ravi@gmail.com",emp_name="ravi")
employee_info(emp_location="pune",emp_email="krishna@gmail.com",emp_name="krishna")
employee_info(emp_location="bangalore",emp_email="mike@gmail.com",emp_name="mike")
employee_info(emp_location="new york",emp_email="john@gmail.com",emp_name="john",org_name="META")

# Attempting to place a non-default argument after a default argument will result in a SyntaxError.
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile): # Non-default argument follows default argumentPylance
    # print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# Default Arguments
def employee_info(emp_name,emp_email,emp_location,mobile_number,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")
    
# Arbitrary Positional Arguments
    # unknown number of positional arguments.
    # positional arguments passed to the function into a single tuple
def add_numbers(*nums):
    for num in nums:
        print(num)
add_numbers(10)
add_numbers(10,20,30)
    
# find sum of numbers passed 
def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num # total = total + num
    print(f"Total Sum: {total}")

add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30)

# Arbitrary Keyword Arguments
    # unknown number of Keyword arguments.
    # Keyword arguments passed to the function into a dictionary 

def profile(**info):
    print(info)

profile(fname="ravi")
profile(fname="ravi",lname="krishna",age=32)

def bank_transactions(**trans):
    print(trans)
    total = 0
    for transaction in trans:
        total += trans[transaction] # total = total + num
    print(f"You have done {len(trans)} Transactions which totals to: {total}")
    
bank_transactions(jan=1000,feb=3000,mar=5000)
bank_transactions(apr=6000)

# Without return
def add(a,b):
    a + b

add(10,20)    
print(add(10,20))

# With return
def add(a,b):
    return a + b

add(10,20) 
print(add(10,20)) 

# Function composition
def sub(c,d,e): # add c + d then minus e
    return add(c,d) - e
print(sub(3,4,5)) # 2

def greet():
    return "Hello "    

def morning():
    print(greet())
    return "Good Morning"

print(morning())

# With return
def add(a,b):
    return a + b
    print("Calculation Done") # Code is structurally unreachable

print(add(100,200))


def math_ops(a,b): # a & b are parameters 
    return a+b
    return a-b
    return a*b

print(add(10,20))

def math_ops(a,b,opr): # a & b are parameters 
    if opr == "+":
        return a+b
    elif opr == "-":
        return a-b
    elif opr == "*":
        return a*b
    else:
        return "Invalid Operator Given"

print(math_ops(10,20,"+"))
print(math_ops(10,20,"*"))
print(math_ops(10,20,"/"))

# Local Scope
def add():
    la = 10 # local variable
    lb = 20 # local variable
    print(la) # accessed within function
    print(lb)
    
add()

# print(la) # accessing local outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb)
    
add(100,200)

# print(la) # accessing local outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

# Global Scope

# global variable
ga = 30

def add(la,lb): # la & lb are local variable
    print(la) # accessed within function
    print(lb)
    print(ga) # global accessed within function

add(15,20)
print(ga) # global accessed outside function

# name conflicts
ga = 30
def add(la,lb,ga): # la & lb & ga are local variable
    print(la) # accessed within function
    print(lb)
    print(ga) # local accessed within function as per preference
    print(globals()['ga']) # global accessed within function

add(1,2,3)

# global variable scenario outside functions 
count = 0
print(count)
count += 1
print(count)

# global keyword scenario inside functions 
count = 0
def increment():
    global count
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    
increment()

# Built In Functions 
# type, len, max, min, dir, id, input etc 
print(type(count))
print(id(count))

# Regular Function i.e without lambda 
def add(a,b):
    return a + b
print(add(10,20))

# Above Function with lambda i.e lambda function
# lambda arguments:expression
sum = lambda a,b:a + b
print(sum(300,400))

# With lambda IILE
print((lambda a,b:a + b) (500,400))

# Without Lambda 
def is_even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False 

print(is_even_num(10))
print(is_even_num(5))

# With Lambda
print((lambda num:num % 2 == 0) (11))
print((lambda num:num % 2 == 0) (9))
print((lambda num:num % 2 == 0) (10))

# Without Lambda 
def check_num(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_num(10))
print(check_num(-10))
print(check_num(0))

# With Lambda
print((lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero") (10))
print((lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero") (-10))
print((lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero") (0))

# Without Lambda 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info(emp_location="hyderabad",emp_email="ravi@gmail.com",emp_name="ravi")

# With Lambda
# print((lambda num:num % 2 == 0) (11))
print((lambda emp_name,emp_email,emp_location: print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}"))(emp_location="pune",emp_email="mike@gmail.com",emp_name="mike"))

# Without map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]

def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

# with map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5] ==> [1,4,9,16,25]
# map(function, iterable)
map((lambda num: num * num), [1,2,3,4,5])
print(map((lambda num: num * num), [1,2,3,4,5]))
print(list(map((lambda num: num * num), [1,2,3,4,5])))

# real world use case of map 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

print(list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100), products)))
price_after_discounts = list(map((lambda p: p["price"] - p["price"] * p["discount"] / 100), products))
print("Prices After Discount: ",price_after_discounts)

# without filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]

def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# with filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10] ==> [2,4,6,8,10]

filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10])))


# real world use case of filter 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

# Find me the products which are above 10000 price 
print(list(filter((lambda p: p["price"] > 10000), products)))
costly_products = list(filter((lambda p: p["price"] > 10000), products))
print("Costly Products: ",costly_products)


# without reduce()
# Write a script/program to take a list of numbers and return the product of all numbers 
# [1,2,3,4,5] ==> [1*2*3*4*5 ==> 120]

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

print(multiply_numbers([1,2,3,4,5]))


# with reduce()
# Write a script/program to take a list of numbers and return the product of all numbers 
# [1,2,3,4,5] ==> [1*2*3*4*5 ==> 120]
from functools import reduce
print(reduce((lambda result,num: result * num ), [1,2,3,4,5]))

# real world use case of reduce 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},
]

# Data Aggregation ==> Find Total Inventory Value Of All Products 
# Like Calculating Total Cart Value 

prices = list(map((lambda p: p["price"]), products))
print(prices)
print(reduce((lambda total_cart,price: total_cart + price ), prices))
cart_value = reduce((lambda total_cart,price: total_cart + price ), prices)
print("Final Cart Value: ",cart_value)