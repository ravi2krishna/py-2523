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

# Menu Based System 
while True:
    print("Choose An Option: ")
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
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
            
        
    elif choice == "2":
        print("Updating Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter Name: ").title()
            students[student_id]["name"] = new_name
            print("Student Updated")
        else:
            print("Student ID Doesn't Exist")
        
        print(students)    
        
        
    elif choice == "3":
        print("Deleting Student")
        student_id = input("Enter ID: ")
        if student_id in students:
            removed_student = students.pop(student_id)
            print("Removed Student Details: ",removed_student)
        else:
            print("Student ID Doesn't Exist")
        
        print(students) 
        
    elif choice == "4":
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
        
    elif choice == "5":
        print("Exiting System")
        print("=" * 50)
        print(f"Call Admin On {ADMIN_INFO[0]}")
        print(f"Email Admin On: {ADMIN_INFO[1]}")
        print("=" * 50)    
        break
    else:
        print("Invalid Choice, Only (1-5) are valid")