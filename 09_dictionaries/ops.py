# Dictionary Methods / Operations 

data = {"a":"apple","b":"banana"}
print(data)

# update(): add / update item 
data.update({"c":"cherry"})
print(data)

data.update({"a":"apricot"})
print(data)

# pop(): removes an item by key
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)

# popitem(): removes last item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): removes all items and empties dict 
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): used to get a value for a key
data = {"a":"apple","b":"banana"}
print(data)
print(data.get("a"))
print(data.get("c"))

# keys(): used to get keys 
data = {"a":"apple","b":"banana"}
print(data)
print(data.keys())
for key in data.keys():
    print(key)
    
# values(): used to get values 
data = {"a":"apple","b":"banana"}
print(data)
print(data.values())
for value in data.values():
    print(value)
    
# items(): used to get both keys & values 
data = {"a":"apple","b":"banana"}
print(data)
print(data.items())
for item in data.items():
    print(item)
    print(item[0])
    print(item[1])
    
# copy(): creates a copy of dict 
data = {"a":"apple","b":"banana"}
print(data)
backup = data.copy()
print(backup)

# setdefault(): returns value of a key if present, if not present then sets 
data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("b","blueberry")
print(data)
print(out)

data = {"a":"apple","b":"banana"}
print(data)
out = data.setdefault("c","cherry")
print(data)
print(out)