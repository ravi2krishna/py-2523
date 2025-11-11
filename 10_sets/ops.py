# Set Methods / Operations 

# add(): add element to the set 
data = {10,20,30,40,50}
data.add(60)
print(data)

# update(): add multiple elements to the set (iterables)
data = {10,20,30,40,50}
data.update([60,70,80])
print(data)

# pop(): Removes a random element from the set
data = {10,20,30,40,50}
data.pop()
print(data)

# remove(): remove an element from the set, if element doesn't exist we get error
data = {10,20,30,40,50}
# data.remove(100)
data.remove(10)
print(data)

# discard(): remove an element from the set, if element doesn't exist we don't get error
data = {10,20,30,40,50}
data.discard(100)
data.discard(10)
print(data)

# clear(): removes all elements and empties the list 
data = {10,20,30,40,50}
data.clear()
print(data)

# copy(): makes a copy 
data = {10,20,30,40,50}
backup = data.copy()
print(backup)

# set specific operations 

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): combine both sets
print(s1.union(s2))
print(s1 | s2)

# intersection(): extract common elements from the sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): extract common elements from the sets, update the calling set
print(s1.intersection_update(s2))
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# difference(): remove common elements from the sets and give unique elements from calling set 
print(s1.difference(s2))
print(s1 - s2)
print(s1)
print(s2)

# difference_update(): remove common elements from the sets and give unique elements from calling set and also updates calling set 
print(s1.difference_update(s2))
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# symmetric_difference(): removes common elements and takes combined elements from both sets 
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update(): removes common elements and takes combined elements from both sets, updates the calling set 
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset(): checks if the given set is subset of another set 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}
print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): checks if the given set is superset of another set 
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint(): checks if the sets have no common elements 
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
