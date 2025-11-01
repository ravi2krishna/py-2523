# Simulate ATM Pin Functionality (ATM/OTP/Passwords etc)

actual_otp = 2345

# import random
# actual_otp = random.randint(1000,9999)
# print(f"OTP Generated sent to mobile {actual_otp}")

attempts = 3

# print(len(actual_otp))

while attempts > 0:
    print(f"You have {attempts} Attempts left")
    user_otp = int(input("Enter OTP: "))
    
    # check for 4 digit number
    if (len(str(user_otp))) != 4:
        print("OTP Must be 4 Digit")
        attempts -= 1
        continue
    
    if user_otp == actual_otp:
        print("Correct OTP - Transaction Success")
        break
    else:
        print("Incorrect OTP - Transaction Failed")
        attempts -= 1

else:
    print("Maximum Attempts Reached, Try After 24 Hours")
    