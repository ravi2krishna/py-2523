# OOP Basics 

# Class 
class Employee():
    pass 

# Object 
emp_obj = Employee()
print(type(emp_obj))

# Student Management System 
# Student -> Real World Entity 
class Student:
    # Characteristics / attributes / variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
    
    # statements 
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)
    
# function (outside the class)    
def student_fun():
    student_name = "John"
    student_email = "john@gmail.com"
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

student_fun() 

# Student -> Real World Entity 
class Student:
    # Characteristics / attributes / variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"

    # Method 
    # def showInfo():
    #     print("Showing Info")
        
    # Method 
    def showInfo(self):
        print("Showing Info")    
        
    # statements 
    print("Student Name: ",student_name)
    print("Student Email: ",student_email)

# Object Creation 
student_obj = Student()
student_obj.showInfo() # TypeError: Student.showInfo() takes 0 positional arguments but 1 was given

print("=" * 20)

# Student -> Real World Entity 
class Student:
    # Characteristics / attributes / variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
        
    # Method 
    def showInfo(self):
        print("Showing Info") 
        print("Student Name: ",student_obj.student_name)
        print("Student Email: ",self.student_email) # this is recommended style   
                
# Object Creation 
student_obj = Student()
student_obj.showInfo()

print("=" * 20)

# Student -> Real World Entity 
# Issue with no constructor 
class Student:
    # Characteristics / attributes / variables 
    student_name = "Ravi"
    student_email = "ravi@gmail.com"
        
    # Method 
    def showInfo(self):
        print("Showing Info") 
        print("Student Name: ",student_obj.student_name)
        print("Student Email: ",self.student_email) # this is recommended style   
                
# Object Creation 
student_ravi = Student()
student_ravi.showInfo()

student_john = Student()
student_john.showInfo()

student_mike = Student()
student_mike.showInfo()

print("=" * 20)

# Student -> Real World Entity 
# with constructor 
class Student:
    
    # special method i.e constructor 
    def __init__(self, student_name, student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # Method 
    def showInfo(self):
        print("Showing Info") 
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) # this is recommended style   
                
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo()

student_john = Student("john","john@gmail.com")
student_john.showInfo()

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo()

print("=" * 20)
