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


# Student -> Real World Entity 
# Instance Members 
class Student:
    
    # special method i.e constructor 
    def __init__(self, student_name, student_email):
        # instance variables 
        # self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Instance Method 
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

# Student -> Real World Entity 
# Class Members 
class Student:
    # class variable
    institute_name = "Edify"
    
    # special method i.e constructor 
    def __init__(self, student_name, student_email):
        # instance variables 
        # self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Instance Method 
    def showInfo(self):
        print("Showing Info") 
        # accessing class variable 
        print("Institute Name: ",Student.institute_name) # this is recommended style   
        # print("Institute Name: ",self.institute_name) # this is not recommended style   
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) # this is recommended style   
    
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
              
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo()

student_john = Student("john","john@gmail.com")
student_john.showInfo()

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo()
# student_mike.change_institute_name("Lync") # this is not recommended style   
Student.change_institute_name("Lync") # this is recommended style   

# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo()

student_john = Student("john","john@gmail.com")
student_john.showInfo()

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo()

print("=" * 20)

# Student -> Real World Entity 
# Instances Members, Class Members & Static Members 
class Student:
    # class variable
    institute_name = "Edify"
    
    # special method i.e constructor 
    def __init__(self, student_name, student_email):
        # instance variables 
        # self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
    
    # Instance Method 
    def showInfo(self):
        print("Showing Info") 
        # accessing class variable 
        print("Institute Name: ",Student.institute_name) # this is recommended style   
        # print("Institute Name: ",self.institute_name) # this is not recommended style   
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) # this is recommended style   
    
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_name):
        cls.institute_name = new_name
        
    # Static Method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email # T and T -> T
              
# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo()

student_john = Student("john","john@gmail.com")
student_john.showInfo()

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo()
# student_mike.change_institute_name("Lync") # this is not recommended style   
Student.change_institute_name("Lync") # this is recommended style   

# Object Creation 
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.showInfo()

student_john = Student("john","john@gmail.com")
student_john.showInfo()

student_mike = Student("mike","mike@gmail.com")
student_mike.showInfo()

# Validate Email -> calling static method 
print(Student.validate_email("ravi"))
print(Student.validate_email("ravi@gmailcom"))
print(Student.validate_email("ravi@gmail.com"))

print("=" * 20)
