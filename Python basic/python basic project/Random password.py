#wap to create a secure password of user define length the password must contain atleast 1 uppercase, 1 lowercase, 1 digit, 1 special digit the remaining character should be selected randomly and print the final password

import random
import string

length = int(input("Enter the password length: "))

if length < 4:
    print("Length must be atleast 4.")
else:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%&*"

    password = []

    password.append(random.choice(uppercase))
    password.append(random.choice(lowercase))
    password.append(random.choice(digits))
    password.append(random.choice(special))

    all_characters = uppercase + lowercase + digits + special

    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)
    print("Generated Password:", final_password)