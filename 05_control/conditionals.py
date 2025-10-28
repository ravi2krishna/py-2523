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
    
# ternary operator / conditional expression
# value_if_true if condition else value_if_false
age = int(input("Enter Your Age: "))
status = "You can vote" if age >=18 else "You cannot vote"
print(status)

# elif ladder
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("Passed")
else:
    print("FAILED")
    
# elif ladder
marks = int(input("Enter Your Marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")   
elif marks >= 60:
    print("C")   
elif marks >= 50:
    print("D")   
elif marks >= 35:
    print("E")   
else:
    print("F")

# match-case
choice = int(input("Enter Your Choice: "))
match choice:
    case 1:
        print("Option 1 Selected")
    case 2:
        print("Option 2 Selected")
    case 3:
        print("Option 3 Selected")
    case 4:
        print("Option 4 Selected")
    case _:
        print("Default Option Selected")

# Voting app with identity verification -> incorrect approach
age = int(input("Enter Your Age: "))
has_id = input("Do You Have ID (yes/no): ")
if age >=18 :
    print("You can vote")
elif has_id == "yes":
    print("You can vote as you have ID")
else:
    print("You cannot vote")

# Voting app with identity verification using nested conditionals 
age = int(input("Enter Your Age: "))
if age >=18 :
    has_id = input("Do You Have ID (yes/no): ")
    if has_id == "yes":
       print("You can vote")
    else:
        print("You need an ID to vote") 
else:
    print("You cannot vote")