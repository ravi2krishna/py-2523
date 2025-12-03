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
        # print(row) # showing me all students from all cities - in List Format
        # print(row[3]) # showing me Hyderabad students 
        if row[3] == filter_by_city:
            print(row)

print("=" * 50)

# Assume we have 10k student records like in csv file 
# Customer Requirement: Fetch me all the records of students from Hyderabad

# Using DictReader 
filter_by_city = "Hyderabad"
with open("14_file_manage/sample.csv","r") as file_data: 
    csv_reader = csv.DictReader(file_data) 
    for row in csv_reader:
        # print(row) # showing me all students from all cities - in Dictionary Format
        if row["address"] == filter_by_city:
            print(row)

print("=" * 50)

# Assume we have 10k student records like in csv file 
# Customer Requirement: Fetch me all the records of students who uses gmail 
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data: 
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row["email"].endswith(filter_by_email):
            print(row)

print("=" * 50)

# Writing data to CSV File - Overwrite 
with open("14_file_manage/emp.csv","w") as file_data: 
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Ravi', 'ravi624@gmail.com', '9693547237', 'Coimbatore'])
    csv_writer.writerows([['Suresh', 'suresh602@gmail.com', '9578381099', 'Hyderabad'],
                        ['Lokesh', 'lokesh489@gmail.com', '9879744557', 'Hyderabad'],
                        ['Ajay', 'ajay280@gmail.com', '9205777629', 'Mumbai']])

print("=" * 50)
    
# Writing data to CSV File - Append 
with open("14_file_manage/test.csv","a") as file_data: 
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'email', 'mobile', 'address'])
    csv_writer.writerow(['Ravi', 'ravi624@gmail.com', '9693547237', 'Coimbatore'])
    csv_writer.writerows([['Suresh', 'suresh602@gmail.com', '9578381099', 'Hyderabad'],
                        ['Lokesh', 'lokesh489@gmail.com', '9879744557', 'Hyderabad'],
                        ['Ajay', 'ajay280@gmail.com', '9205777629', 'Mumbai']])

print("=" * 50)

# Writing data to CSV File - DictWriter with write mode
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/new.csv","w") as file_data: 
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader() # write the column headers to the first row of the CSV
    csv_writer.writerow({'name': 'Naveen', 'email': 'naveen959@gmail.com', 'mobile': '9956567915', 'address': 'Bangalore'})
    csv_writer.writerows([{'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
                            {'name': 'Ajay', 'email': 'ajay280@gmail.com', 'mobile': '9205777629', 'address': 'Mumbai'},
                            {'name': 'Ravi', 'email': 'ravi624@gmail.com', 'mobile': '9693547237', 'address': 'Coimbatore'}])

# Writing data to CSV File - DictWriter with append mode
fieldnames = ['name', 'email', 'mobile', 'address']
with open("14_file_manage/demo.csv","a") as file_data: 
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader() # write the column headers to the first row of the CSV
    csv_writer.writerow({'name': 'Naveen', 'email': 'naveen959@gmail.com', 'mobile': '9956567915', 'address': 'Bangalore'})
    csv_writer.writerows([{'name': 'Lokesh', 'email': 'lokesh489@gmail.com', 'mobile': '9879744557', 'address': 'Hyderabad'},
                            {'name': 'Ajay', 'email': 'ajay280@gmail.com', 'mobile': '9205777629', 'address': 'Mumbai'},
                            {'name': 'Ravi', 'email': 'ravi624@gmail.com', 'mobile': '9693547237', 'address': 'Coimbatore'}])