# Working With Lists 

# empty list 
empty_list = []
print(empty_list)
print(type(empty_list))

# empty list 
empty_list = list()
print(empty_list)
print(type(empty_list))

# list with numeric data 
data = [10,20,30,40,50]
print(data)

data = list([10,20,30,40,50])
print(data)

# list with text data 
data = ["python","django","sql"]
print(data)

# list with mixed data 
data = [10,20,30,"python","django","sql",3.5,True]
print(data)

# Accessing Data 
data = [10,20,30,40,50]
print(data)

first_element = data[0]
last_element = data[-1]
print(data)
print(first_element)
print(last_element)

# accessing index error
# print(data[10]) # IndexError: list index out of range

# access range of values 
data = [10,20,30,40,50]
print(data[::])
print(data[1:3:1])
print(data[0:5:2])

# access individual elements 
for num in data:
    print(num)
    
# apply operators 
data = [10,20,30,40,50]
for num in data:
    print(num * 10)
    
# apply conditionals 
data = [10,25,30,45,55]
print(data)
for num in data:
    if num % 2 == 0:
        print(num)

# we can work with any type of data and apply appropriate methods
data = ["python","django","sql"]
print(data)
for course in data:
    print(course.upper())
    
# Behavior of duplicates 
data = [10,20,10,30,20,40,10,50]
print(data)

# list methods 
print(dir(data))