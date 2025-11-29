# Working With Files & Folders(Directories)
# Using Permanent Storage 

# syntax 1 
file = open("14_file_manage/file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: '14_file_manage/file.txt'
print(file)
print(file.closed)
file.close() # explicitly close
print(file.closed)

# syntax 2
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data)
print(file_data.closed)

# reading data from file - whole file 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())

# reading data from file - read character based
with open("14_file_manage/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)

# reading data from file - read word based  
with open("14_file_manage/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)
    
# reading data from file - read one line 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readline())
        
# reading data from file - read one line 
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.readlines())

# reading data from file - read one line and extract from List
with open("14_file_manage/file.txt","r") as file_data:
    list_data = file_data.readlines()
    for line in list_data:
        print(line.strip())

# Create files can be done with "w" mode 

# write mode and create file 
with open("14_file_manage/write.txt","w") as file_data:
    print(file_data)
    
# write mode and update file 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("hello")
    
# write mode and update file with multiple lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['hello there\n', 'how are you\n', 'python class started'])

# write mode and update file with multiple lines
with open("14_file_manage/write.txt","w") as file_data:
    file_data.writelines(['line 4\n', 'line 5\n', 'line 6\n'])
    
# append mode and update file with multiple lines preserving previous line
with open("14_file_manage/write.txt","a") as file_data:
    file_data.writelines(['line 7\n', 'line 8\n', 'line 9'])