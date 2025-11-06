# List Operations / Methods 

# append() : add an element to end of list
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

data.append([70,80,90])
print(data)

# extend() : add an iterable to list 
data = [10,20,30,40,50]
print(data)
# data.extend(60) TypeError: 'int' object is not iterable
data.extend([60,70,80,90])
print(data)