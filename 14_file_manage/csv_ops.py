# Working With CSV Files 

import csv 

# Read Data 
with open("14_file_manage/students.csv","r") as file_data: 
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Assume we have 10k student records like in csv file 
# Customer Requirement: Fetch me all the records of students from Hyderabad
filter_by_city = "Hyderabad"
with open("14_file_manage/students.csv","r") as file_data: 
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        # print(row) # showing me all students from all cities 
        # print(row[3]) # showing me Hyderabad students 
        if row[3] == filter_by_city:
            print(row)
 
print("=" * 50)
            
# Assume we have 10k student records like in csv file 
# Customer Requirement: Fetch me all the records of students who uses gmail 
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data: 
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        if row[1].endswith(filter_by_email):
            print(row)

print("=" * 50)

# Assume we have 10k student records like in csv file 
# Customer Requirement: Fetch me all the records of students from Hyderabad
filter_by_city = "Hyderabad"
with open("14_file_manage/sample.csv","r") as file_data: 
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        # print(row) # showing me all students from all cities 
        # print(row[3]) # showing me Hyderabad students 
        if row[3] == filter_by_city:
            print(row)