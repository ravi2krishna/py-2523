# Student Grade Tracker 

student_id = input("Enter ID: ")
student_name = input("Enter Name: ")
student_attendance = int(input("Enter Attendance : "))

total_score = 0 # 80
number_of_subjects = 0 # 1

continue_input = "yes"

while continue_input == "yes":
    current_score = int(input(f"Enter Score for Subject {number_of_subjects+1}: ")) # 80
    continue_input = input("Do you want to enter with another score ? (yes/no): ") # yes
    number_of_subjects += 1 # number_of_subjects = 1
    total_score += current_score # total_score + 80 -> 80

# Average Score
average_score = total_score / number_of_subjects

# Grade 
if average_score >= 85:
    print("You Got A Grade")
elif average_score >= 70:
    print("You Got B Grade")
elif average_score >= 50:
    print("You Got C Grade")
else:
    print("You Got D Grade")

# attendance 
attendance_status = "WARNING - LOW ATTENDANCE" if student_attendance < 75 else "OK - GOOD ATTENDANCE"

# App Output
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Total Score: {total_score}")
print(f"Number Of Subjects: {number_of_subjects}")
print(f"Average Score: {average_score}")
print(f"Attendance Status: {attendance_status}")