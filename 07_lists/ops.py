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

# insert() : insert data at specific position (index)
data = [10,20,40,50]
print(data)
data.insert(2,30)
print(data)

data.insert(10,100) # if index is given out of range, adds at end of list 
print(data)

# pop() : removes an element, by default last or based on index
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)
data.pop(0)
print(data)
# data.pop(10) # IndexError: pop index out of range
print(data)

# remove() : remove element based on value
data = [10,20,30,40,50]
print(data)
data.remove(30)
print(data)
# data.remove(100) # ValueError: list.remove(x): x not in list
print(data)

data = [10,20,30,10,40,50,10]
print(data)
data.remove(10)
print(data)

# logic for custom removal of all occurrences 
data = [10,20,30,10,40,50,10]
print(data)

while 10 in data:
    data.remove(10)
print(data)

# clear() : removes all elements and empties the list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index() : used to get the index position of a value 
data = [10,20,30,40,50]
print(data)
print(data.index(30))
# print(data.index(100)) # ValueError: 100 is not in list

# count() : used to count number of occurrences of a value 
data = [10,20,30,10,40,50,10]
print(data)
print(data.count(10))

# reverse(): reverse the list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): sort the list, default is ascending order 
data = [40,20,30,10,50]
print(data)
data.sort()
print(data)
data.sort(reverse=True) # descending order 
print(data)

data = ["a","d","e","c"]
print(data)
data.sort()
print(data)

data = ["a",10,"d",20,"e","c"]
print(data) 
# data.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
print(data)

# copy() : create a copy of list 
data = [10,20,30,40,50]
print(data)
backup = data.copy()
print(backup)
