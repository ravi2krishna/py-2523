# Student Management System

# Menu Based System ==> In Future you can replace with UI Elements like Buttons 

# System Info - READ Only (Tuple)
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info - READ Only (Tuple)
ADMIN_INFO = ("9090880","admin@edify.com")

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
    elif choice == "3":
        print("Deleting Student")
    elif choice == "4":
        print("Listing Student")
    elif choice == "5":
        print("Exiting System")
        break
    else:
        print("Invalid Choice, Only (1-5) are valid")