# Operators 

# Arithmetic Operators -> Mathematical Calculations
num1 = 10
num2 = 5

print("The Sum of Two Numbers: ",num1+num2)
print("The Sum of {num1} and {num2} is {num1+num2}") # without f 
print(f"The Sum of {num1} and {num2} is {num1+num2}")# with f 
print(f"The Difference of {num1} and {num2} is {num1-num2}")
print(f"The Product of {num1} and {num2} is {num1*num2}")
print(f"The Division of {num1} and {num2} is {num1/num2}")
print(f"The Modulus/Remainder of {num1} and {num2} is {num1%num2}")
print(f"The Floor Division of {num1} and {num2} is {num1//num2}")

num1 = 3
num2 = 2

print(f"The Division of {num1} and {num2} is {num1/num2}")
print(f"The Floor Division of {num1} and {num2} is {num1//num2}")

print(f"Exponentiation of {num1} and {num2} is {num1 ** num2}") # 3 ^ 2

print("===============")

# Compound Assignment Operators -> Used for increment / decrements 
# without Compound Assignment Operators
num = 10
num = num + 5
print(num)

# with Compound Assignment Operators
num = 10
num += 5
print(num)

num = 10
num *= 5
print(num)

# increment 
count = 1
count += 1
print(count)

# decrement 
count = 10
count -= 1
print(count)

print("===============")

# Comparison Operators  
num1 = 10
num2 = 5

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

print("===============")

# Logical Operators  
num1 = 10
num2 = 5
num3 = 1
num4 = 2

print(num1 > num2 )
print(num3 > num4 )
print(num1 > num2 and num3 > num4)
print(num1 > num2 and num3 < num4)

print(num1 > num2 or num3 > num4)
print(num1 < num2 or num3 > num4)

print(num1 > num2 )
print( not num1 > num2 )

print("===============")

# Membership Operators
data = "python is programming language"
find_word = "java"
# find_word = "python"
found = find_word in data
print(found)

data = "python is programming language"
find_word = "java"
# find_word = "python"
found = find_word not in data
print(found)

print("===============")

# Identity Operators  
n1 = 10
n2 = 10
n3 = 1

print(n1 is n2)
print(n1 is n3)

l1 = [10,20]
l2 = [10,20]

print(l1 is l2)

print("===============")

# Bitwise Operators  
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
       # 0000000000000001

print(n1 & n2) # 1
print(n1 | n2) # 7