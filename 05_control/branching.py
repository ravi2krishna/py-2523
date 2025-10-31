# Branching Statements

# loop without break 
for num in range(1,11):
    print(num)

# loop with break 
for num in range(1,11):
    if num == 5:
        break # stop 
    print(num)
    
# loop with continue 
for num in range(1,11):
    if num == 5:
        continue # skip 
    print(num)
    
# req to perform some "future" operations 
# when the emp salary is above 25000 

emp_salary = 30000
if emp_salary > 25000:
    pass # acts as a placeholder for my future code

# some other functionality to work 
print("Working with Next Functionalities")    