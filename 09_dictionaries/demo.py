# Working With Dictionaries 

# empty dict 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# empty dict 
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# dict with numeric data 
# data = {10,20,30,40,50} this is set, as there are no keys
# print(type(data))
# print(data)

# dict with numeric data 
data = {1:10,2:20,3:30,4:40,5:50} 
print(type(data))
print(data)

data = dict({1:10,2:20,3:30,4:40,5:50})
print(data)

# dict with text data 
data = {"c1":"python","c2":"django","c3":"sql"}
print(data)

# dict with mixed data 
data = {1:10,2:20,3:30,"c1":"python","c2":"django","c3":"sql","avg":3.5,"passed":True}
print(data)

# Accessing Data is done via keys not index 
data = {1:10,2:20,3:30,4:40,5:50} 
print(data)

# first_element = data[0]
first_element = data[1]
last_element = data[5]
print(data)
print(first_element)
print(last_element)

# access individual elements i.e looping data by default we get keys 
data = {1:10,2:20,3:30,4:40,5:50} 
for num in data:
    print(num)
    
# for k, v in iterable:
#     d[k] = v

for key in data:
    print(key)

# access individual elements i.e now values we want 
data = {1:10,2:20,3:30,4:40,5:50} 
for key in data:
    print(data[key])
    
# apply operators 
data = {1:10,2:20,3:30,4:40,5:50} 
for key in data:
    print(data[key] * 10)

    
# apply conditionals 
data = {1:10,2:20,3:35,4:40,5:55} 
for key in data:
    if data[key] % 2 == 0:
        print(data[key])

# we can work with any type of data and apply appropriate methods
data = {"c1":"python","c2":"django","c3":"sql"}
print(data)
for key in data:
    print(data[key].upper())
    
# Behavior of duplicates 
data = {1:10,2:20,3:30,4:40,5:50,6:50,7:50} 
print(data)

# when duplicates keys are given, it will override 
data = {1:10,2:20,3:30,4:40,5:50,1:10.0,2:20.0} 
print(data)

# real world dictionary (JSON Data representation)
students = {
    "101": {
       "name": "Ravi",
       "email": "ravi2krishna@gmail.com",
       "courses": ["python","django","ai"],
       "course_prices": (10000,25000,50000)
    },
    "102": {
       "name": "John",
       "email": "john@yahoo.com",
       "courses": ["java","spring","ai"],
       "course_prices": (10000,25000,50000)
    } 
}

print(type(students))
print(students)

print(students["101"])
print("Name: ",students["101"]["name"])
print("Courses: ",students["101"]["courses"])
print("1st Courses: ",students["101"]["courses"][0])

id = "102"
if students[id]["email"].endswith("@gmail.com"):
    print("Google Customer")
else:
    print("Not Google Customer")

# dict methods 
print(dir(data))