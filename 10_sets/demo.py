# Sets 

# Empty Set 

# empty set ==> by default if we use empty {} then it's a dict 
empty_set = {}
print(empty_set)
print(type(empty_set))

# empty set 
empty_set = set()
print(empty_set)
print(type(empty_set))

# set with numeric data 
data = {10,20,30,40,50} 
print(type(data))
print(data)

# set with text data 
data = {"python","django","sql"}
print(data)

# set with mixed data 
data = {10,20,30,"python","django","sql",3.5,True}
print(data)

# Accessing Data 
data = {10,20,30,40,50}
print(data)

# print(data[0])
# print(data[10])

# access individual elements 
data = {10,20,30,40,50}
for num in data:
    print(num)
    
# apply operators 
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
    
# apply conditionals 
data = {10,25,30,45,55}
print(data)
for num in data:
    if num % 2 == 0:
        print(num)

# we can work with any type of data and apply appropriate methods
data = {"python","django","sql"}
print(data)
for course in data:
    print(course.upper())
    
# Behavior of duplicates 
data = {10,20,10,30,20,40,10,50}
print(data)

# sets methods 
print(dir(data))

# Frozen Set
data = {10,20,10,30,20,40,10,50}
print(type(data))

data_fz_set =frozenset({10,20,10,30,20,40,10,50})
print(type(data_fz_set))

print(dir(data_fz_set))