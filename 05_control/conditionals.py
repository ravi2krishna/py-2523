# Conditionals 

# Indentation 
print("Hello")
 
#  print("Hello") # IndentationError: unexpected indent

# if condition 
if 5 > 2:
# print("yes that is correct") # IndentationError: expected an indented block after 'if' statement on line 9
    print("yes 5 > 2 that is correct")
#  print("i want to print this too") # IndentationError: unindent does not match any outer indentation level
    print("i want to print this too")
    
if 5 > 10:
 print("yes 5 > 10 that is correct")
 
if 10 > 5:
  print("yes 10 > 5 that is correct")
  
num = -10  
if num > 0:
    print(f"Number {num} is positive")
if num < 0:
    print(f"Number {num} is negative")
    
# if else condition
num = 10  
if num > 0:
    print(f"Number {num} is positive")
else:
    print(f"Number {num} is negative")
    
# check voting eligibility 
age = 21
if age >=18 :
    print("You can vote")
else:
    print("You cannot vote")
    
# input() - reads from user 
name = input("Enter Your Name: ")
print(f"Welcome {name}")
session = input("Enter Course Name: ")
print(f"You are attending {session} course")

num1 = input("Enter Number: ")
num2 = input("Enter Number: ")
sum = num1 + num2 # concatenation 
print(sum) 

num1 = input("Enter Number: ")
num1 = int(num1)
num2 = int(input("Enter Number: "))
sum = num1 + num2 # adding numbers 
print(sum) 

# age = input("Enter Your Age: ") # TypeError: '>=' not supported between instances of 'str' and 'int'
age = int(input("Enter Your Age: "))
if age >=18 :
    print("You can vote")
else:
    print("You cannot vote")