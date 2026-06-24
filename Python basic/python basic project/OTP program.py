#wap to create 6 digit OTP number. accept OTP from user and validate if OTP is correct then print login successful only 3 attempt will be allowed to enter a OTP

import random

otp = random.randint(100000, 999999)
print("Your OTP is:", otp)

attempts = 0
max_attempts = 3
user_otp = 0

while attempts < max_attempts:
    user_otp = int(input("Enter the OTP: "))
    attempts = attempts + 1

    if user_otp == otp:
        print("Login Successful")
        break
    else:
        print("Incorrect OTP")
        print("Attempts remaining:", max_attempts - attempts)

else:
    print("Login Failed. No attempts remaining.")