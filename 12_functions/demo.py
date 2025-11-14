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