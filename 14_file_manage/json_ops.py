# Working With JSON Data / Files 

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","ai"],
    "gpa": 9.5
}

print(type(student))
print(student)

# Writing data to JSON File 
import json
with open("14_file_manage/student.json","w") as file_data: 
    json.dump(student,file_data)

# Writing data to JSON File With Indentation 
with open("14_file_manage/stu.json","w") as file_data: 
    json.dump(student,file_data,indent=4)

print("=" * 50)

# Reading data from JSON File 
with open("14_file_manage/stu.json","r") as file_data: 
    json_reader = json.load(file_data)
print(json_reader)
print(type(json_reader))

print("=" * 50)

# Requirement: Get Student Name & Number Of Courses from stu.json 
with open("14_file_manage/stu.json","r") as file_data: 
    json_reader = json.load(file_data)
print("Student Name: ",json_reader["name"])
print("No Of Courses Enrolled: ",len(json_reader["courses"]))

# Requirement: Check If Student Passes or Not, Based On GPA i.e above 7 
with open("14_file_manage/stu.json","r") as file_data: 
    json_reader = json.load(file_data)

if json_reader["gpa"] > 7:
    print(f"{json_reader["name"]} Passed")
else:
    print(f"{json_reader["name"]} Failed")

print("=" * 50)

# File Based (dump & load)    
# Object Based, rather than files (dumps & loads)

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","ai"],
    "gpa": 9.5
}

json_data = json.dumps(student)
print(json_data)
print(type(json_data))

string_data = '{"id": 101, "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "django", "ai"], "gpa": 9.5}'
dict_data = json.loads(string_data)
print(dict_data)
print(type(dict_data))

print("=" * 50)

# Building Full Stack Application - JSON use case
import urllib.request

# Assume as API, URL where we get data from
url = "https://dummyjson.com/users"  # Replace with your desired URL

response = urllib.request.urlopen(url)
print(response)

# Reading data from API response 
api_data = response.read()
print(api_data)
print(type(api_data))

# Convert Data 
api_data = json.loads(api_data)
print(api_data)
print(type(api_data))

# Customer Requirement: List me Users 
users = api_data["users"]
print(users)

# Customer Requirement: List me Users usernames & number of users 
for user in users:
    print(user["username"])

print("Number Of Users: ",len(users))

# Customer Requirement: List me users with age below 30 
for user in users:
    if user["age"] < 30:
        print(user["username"], user["age"])