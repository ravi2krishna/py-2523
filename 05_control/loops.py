# Looping Statements 

# while - when we don't know number of Iterations in advance 

# password authentication -> forgot password, you'll keep trying till password is matched 
# at what attempt password is matched ?? 

actual_password_db = "2345"
user_given_password = ""

while user_given_password != actual_password_db:
    user_given_password = input("Enter Password: ")

print("Password Matched, Login Success")

# while
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1

# for loop for sequence
list_numbers = [10,20,30,40,50,500]
print(list_numbers)

for num in list_numbers:
    print(num)

# result = 10 * 10    
# result = 10 * 20
# result = 10 * 30
for num in list_numbers:
    # print(f"{num} * {10}")
    print(num * 10)
    
simple_number = 12345

# for num in simple_number: # TypeError: 'int' object is not iterable
#     print(num)

# print(dir(simple_number)) # no __iter__

# print(dir(list_numbers)) # __iter__

# for - when we  know number of Iterations in advance 
print("Hi")

# Say Hi for 10 times
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

# range() - generates an immutable sequence of numbers
for num in range(5):
    print(num)
    
for num in range(10):
    print(num)
    
for num in range(5,11):
    print(num)

for num in range(2,11,1):
    print(num)

for num in range(2,11,2):
    print(num)
    
for num in range(5,100,5):
    print(num)
    
for num in range(10, 0, -1):
    print(num)
    
# Say Hi for 10 times
for greet in range(10):
    print("Hi")

# Nested While Loops 
outer = 1
while outer < 6:
    inner = 1 
    while inner < 6:
        print(f"{outer} * {inner} = {outer * inner}")
        inner+=1
    outer+=1

# simple read world use case -> ecommerce 
colors = ["red","black","green"]
sizes = ["XS","S","M","L","XL","XXL"]
print(len(colors))
print(len(sizes))
# print("red XS")
# print("red S")
# print("red M")
i = 0
while i < 3:
    j = 0
    while j < 6:
        print(colors[i] +" "+ sizes[j])
        j+=1
    i+=1
     
i = 0
while i < len(colors):
    j = 0
    while j < len(sizes):
        print(colors[i] +" "+ sizes[j])
        j+=1
    i+=1   
    
# Nested for loop
for outer in range(1,4):
    for inner in range(1,4):
        print(f"{outer} * {inner} = {outer * inner}")

# simple read world use case -> ecommerce 
colors = ["red","black","green"]
sizes = ["XS","S","M","L","XL","XXL"]

for color in colors:
    for size in sizes:
        print(color, size)         