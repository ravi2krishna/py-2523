# Student Management System

# Menu Based System ==> In Future you can replace with UI Elements like Buttons 

# System Info - READ Only (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ Only (Tuple)
ADMIN_INFO = ("9090880123","admin@edify.com")

# system startup info
print("=" * 50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Software Name: {SYSTEM_INFO[1]} {SYSTEM_INFO[2]}")
print("=" * 50)

# student -> id, name, multiple scores, multiple unique skills 
# setting student details in dictionary 
students = {}

# adding student function 
def add_student():
        print("Adding Student")
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("Student Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or Type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
            
            skills = set()
            while True:
                skill_input = input("Enter Skill or Type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input)
            
            # Save above student details to dictionary i.e students = {}
            # student -> id, name, multiple scores, multiple unique skills
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills   
            }
            
            print("Student Added")
            print(students)


# updating student function 
def update_student():
        print("Updating Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter Name: ").title()
            students[student_id]["name"] = new_name
            print("Student Updated")
        else:
            print("Student ID Doesn't Exist")
        
        print(students)    


# deleting student function 
def delete_student():
        print("Deleting Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            removed_student = students.pop(student_id)
            print("Removed Student Details: ",removed_student)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) 

# Reading student function 
def read_students():
        print("Listing Student")
        # {'102': {'name': 'John', 'scores': [80], 'skills': {'java'}}}
        for sid, data in students.items():
            name = data['name']
            scores = data['scores']
            avg_score = sum(scores) / len(scores)
            high_score = max(scores)
            least_score = min(scores)
            skills = data['skills']
            skills_count = len(skills)
            
            print(f"ID: {sid}")
            print(f"Name: {name}")
            print(f"All Scores: {scores}")
            print(f"Average Score: {avg_score}")
            print(f"Maximum Score: {high_score}")
            print(f"Minimum Score: {least_score}")
            print(f"All Skills: {skills}")
            print(f"Skills Count: {skills_count}")   
    
# search by skill 
def search_student_skill():
    skill_to_search = input("Enter Skill To Search: ")
    # filter((lambda num: num % 2 == 0), [1,2,3,4,5,6,7,8,9,10])
    # {'102': {'name': 'John', 'scores': [80], 'skills': {'java'}}}
    filtered_students = list(filter((lambda sid: skill_to_search in students[sid]['skills']), students))
    if filtered_students:
        print(f"Students With Skills {skill_to_search}")
        for sid in filtered_students:
            print(f"ID: {sid}   -   Name: {students[sid]['name']}")
    else:
        print(f"No Students Found With Skill {skill_to_search}")        

# exiting application function 
def exist_system():
        print("Exiting System")
        print("=" * 50)
        print(f"Call Admin On {ADMIN_INFO[0]}")
        print(f"Email Admin On: {ADMIN_INFO[1]}")
        print("=" * 50)  

# Menu Based System 
while True:
    print("Choose An Option: ")
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Search By Skill")
    print("6 - Exit")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        add_student()     
        
    elif choice == "2":
        update_student()
        
    elif choice == "3":
        delete_student()
        
    elif choice == "4":
        read_students()
    
    elif choice == "5":
        search_student_skill() 
        
    elif choice == "6":
        exist_system()  
        break
    else:
        print("Invalid Choice, Only (1-5) are valid")