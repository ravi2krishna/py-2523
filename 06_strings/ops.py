# String Methods / Operations 

# Simulate Gmail Functionality 
# RAvi2KRisHnA -> ravi2krishna@gmail.com 
email = input("Enter Your Email ID: ")
format_email = email.lower().strip()+"@gmail.com"
print("Original Email: "+email)
print("Formatted Email: "+format_email)

# Simulate PAN Functionality 
# https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm

pan = input("Enter PAN ID: ")
# print(pan.isalnum())
if pan.isalnum():
    format_pan = pan.upper()
    print("Given PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("Invalid PAN ID")
    
# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png

mobile_number = input("Enter Phone Number With ISD Code: ")

if mobile_number.startswith("+91"):
    print("Calling India Number - Charged In Rupees")
elif mobile_number.startswith("+1"):
    print("Calling USA Number - Charged In Dollars")
elif mobile_number.startswith("+33"):
    print("Calling France Number - Charged In Euros")
else:
    print("Calling Support To Only - India, USA & France")

# Simulate Email Synchronization
source_email = input("Enter Source Email ID: ")   
destination_email = input("Enter Destination Email ID: ")   

if source_email.endswith("@gmail.com") and destination_email.endswith("@gmail.com"):
    print("Email Synchronization Started")
else:
    print("Email Synchronization Failed")
    
# Simulate CSV Data from a file and perform operations
# Name, Email, Age, City, Job_Role
emp_john_data = "John,john@gmail.com,25,hyderabad,developer"
print(emp_john_data)

# Req : Display Only Emp Name & Emp Job Role
print("Name: "+emp_john_data[0])
print("Job Role: "+emp_john_data[-1])

data_parts = emp_john_data.split(",")
print(data_parts)

print("Name: "+data_parts[0])
print("Job Role: "+data_parts[-1])

# Simulate Amazon Order Email Confirmation
order_template = "Hello, your order with {order_id} has been shipped"
order_ids = "AMZ-IN-8909,AMZ-IN-7530,AMZ-IN-2312"
order_print = order_ids.split(",")

for order_id in order_print:
    user_email = order_template.replace("{order_id}",order_id)
    print(user_email)