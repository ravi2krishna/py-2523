# Exception Handling 

# When No Error -> Nothing To Handle 

print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")

print("=" * 50)

# When There Is Error -> Python Handles by stopping the program
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)

# When There Is Error -> User Handles Errors by try & catch, with meaningful info
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! You cannot divide number by zero - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When There Is NO Error -> User Handles Errors by try & catch, with meaningful info
print("Program Execution Started")
num1 = 10
num2 = 5
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! You cannot divide number by zero - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
# data = [1,2,'python',0,5]
# data = [1,2,0,5]
data = [1,2,5]
for num in data:
    print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str' 
    # ZeroDivisionError: division by zero
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str' 
    # ZeroDivisionError: division by zero
    except:
        print("OOPS! Something Went Wrong")
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str' 
    # ZeroDivisionError: division by zero
    except:
        print("OOPS! Dividing String With Number is not supported")
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num)
    # TypeError: unsupported operand type(s) for /: 'int' and 'str' 
    # ZeroDivisionError: division by zero
    except TypeError:
        print("OOPS! Dividing String With Number is not supported")
    except ZeroDivisionError:
        print("OOPS! You cannot divide number by zero - Check Below Link")
        print("https://en.wikipedia.org/wiki/Division_by_zero")
print("Program Execution Completed")

print("=" * 50)

# When There Is NO Error -> User Handles Errors by try & catch, with meaningful info
# else use case
print("Program Execution Started")
num1 = 10
num2 = 5
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2)
except:
    print("OOPS! You cannot divide number by zero - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful")
print("Program Execution Completed")
print("=" * 50)


# When There Is NO Error -> User Handles Errors by try & catch, with meaningful info
# else use case
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2) # Login Success 
except:
    print("OOPS! You cannot divide number by zero - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful") # Then Check for OTP
print("Program Execution Completed")
print("=" * 50)

# When There Is NO Error -> User Handles Errors by try & catch, with meaningful info
# finally use case
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
try:
    print(num1/num2) # Login Success 
except:
    print("OOPS! You cannot divide number by zero - Check Below Link")
    print("https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful") # Then Check for OTP
finally:
    print("Program Execution Completed") # file.close() 
print("=" * 50)

# Check Inbuilt Exceptions
# print(help(Exception))

# Create Custom Exception 
class MyCustomError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    print("You Cannot Vote")
else:
    print("You Can Vote")

# Custom Age Exception 
class AgeError(Exception):
    pass

age = int(input("Enter Age: "))
if age < 18:
    raise AgeError("Your Age Must be at least 18 years to register")
else:
    print("Registration Success")

# Custom Exception For ID 
class IDError(Exception):
    pass 

age = int(input("Enter Age: "))
if age < 18:
    raise AgeError("Your Age Must be at least 18 years to register")
else:
    has_id = input("Do You Have ID ? (yes/no) ")
    if has_id != "yes":
        raise IDError("You Must Have ID To Register")
print("Registration Success")

# Handle Multiple Exceptions 
age = int(input("Enter Age: "))
try:
    if age < 18:
        raise AgeError
    else:
        has_id = input("Do You Have ID ? (yes/no) ")
        if has_id != "yes":
            raise IDError
except AgeError:
    print("You are not 18 Yet")
except IDError:
    print("ID is mandatory")
else:    
    print("Registration Success")