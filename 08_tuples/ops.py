# Tuples Are Immutable
data = (10,20,30,40,50)
print(data)
# data[2] = 300 # TypeError: 'tuple' object does not support item assignment
print(data)

# In contrast to tuples. lists are mutable 
data = [10,20,30,40,50]
print(data)
data[2] = 300
print(data)

# index() : used to get the index position of a value 
data = (10,20,30,40,50)
print(data)
print(data.index(30))
# print(data.index(100)) # ValueError: 100 is not in list

# count() : used to count number of occurrences of a value 
data = (10,20,30,10,40,50,10)
print(data)
print(data.count(10))