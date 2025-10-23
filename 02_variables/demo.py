# Variables 
# variable_name = value 

# Assign Data (Storing Data)
student_name = "Ravi" # string 
student_age = 25 # int 
student_gpa = 9.5 # float 
student_passed = True # boolean True/False
student_unknown_data = None # represents no value 

# Retrieve Data -> print()
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_unknown_data)

# Retrieve Data with statements -> concatenation
# print("Student Name" student_name) # SyntaxError: invalid syntax
print("Student Name: " +student_name)
# print("Student Age: " +student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ", student_age)
print("Student GPA: ",student_gpa)
print("Student Passed: " ,student_passed)
print("Student Unknown: ",student_unknown_data)
print("Student Name: " ,student_name)

print("=================")

# Get identity / memory address 
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))
print(id(student_unknown_data))

print("=================")

# Memory Model Of Python
value_x = 10
print(id(value_x))

value_y = 20
print(id(value_y))

value_z = 10
print(id(value_z))

print("=================")

list_data_x = [10,20,30,40,50]
print(id(list_data_x))

list_data_z = [10,20,30,40,50]
print(id(list_data_z))

print("=================")

print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(student_unknown_data))
print(type(list_data_z))