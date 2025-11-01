# Requirement

# -> Create a python application to calculate the fee discount for students
# based on their grade levels and academic Performance

student_name = input("Enter Name: ")
student_grade = int(input("Enter Grade: "))
student_fee = int(input("Enter Course Fee: "))
is_academic_topper = input("Are You Topper? (yes/no): ")

# initial discount = 0
discount = 0.0

# validation of grade 
if 1 <= student_grade <= 12:
    print("========= Processing Fee Calculation =========")
    
    # discount for 9 to 12
    if student_grade >=9 and student_grade <=12:
        if is_academic_topper == "yes":
            discount = 0.2 # 20% discount as he is topper 
            print("Academic Topper Discount Applied")
        else:
            discount = 0.1 # 10% discount as high school
            print("High School Discount Applied")
    
    elif student_grade >=6 and student_grade <=8:
        discount = 0.05
        print("Middle School Discount Applied") 
    else:
        discount = 0.0
        print("No Discount For other grades")
        
    # Additional Discounts
    match student_grade:
        case 10:
           discount += 0.03 
        case 12:
            discount += 0.05
        case _:
            pass
    
    # discount amount 
    discount_amount = student_fee *  discount
    fee_to_pay = student_fee - discount_amount
    
    # display results
    print(f"Student Name: {student_name}")
    print(f"Student Grade: {student_grade}")
    print(f"Tuition Fee: {student_fee}")
    print(f"Total Discount: {discount_amount}")
    print(f"Final Fee: {fee_to_pay}")

else:
    print("Invalid Grade only grades (1-12) allowed")
