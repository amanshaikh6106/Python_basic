#write a program to find maximum between given three numbers

num1 = input("Enter first number:")
num2 = input("Enter second number:")
num3 = input("Enter third number:")
if (int(num1>num2) and int(num1>num3)):
    print("first number is max")
elif (int(num2>num3)):
    print("second number is max")
else :
    print("third number is max")


#write a program to check given year is leaper year or not

num1 = input("Enter a year:")
if (int(num1) % 4 == 0 and int(num1) % 100 != 0 or int(num1) % 400 == 0):
    print("it is leaper")
else:
    print("it is not")
    

#write a program to calculate discount on price if price is between greater than 5000 and less than 10000 then discount is 5% if price is between greater than 10000 and less than 15000 then discount is 10% if price is greater than 50000 then discount is 50% else no discount. print final price after discount

price = int(input("Enter price:"))
if ((price) > 5000 and (price) < 10000):
    discount = (price) * 5/100
    final_price = (price) - discount
    print("Final price after discount is:", final_price)
elif ((price) > 10000 and (price) < 15000):
    discount = (price) * 10/100
    final_price = (price) - discount
    print("Final price after discount is:", final_price)
elif ((price) > 50000):
    discount = (price) * 50/100
    final_price = (price) - discount
    print("Final price after discount is:", final_price)
else:
    print("No Discount")


#write a program to calculate electricity bill based on following condition if unit is between 0 to 100 then 2 rupees per unit if unit is between 100 to 250 then 4 rupees per unit if unit is above 250 then 6 rupees per unit take first unit and last unit from user and calculate total bill and print first unit and last unit and total bill

current_reading = int(input("Enter current reading:"))
last_reading = int(input("Enter last reading:"))
if (current_reading > last_reading):
            print("current reading is greater than last reading")
            unit_consumed = current_reading - last_reading
            if (unit_consumed > 0 and unit_consumed < 100):
                bill = unit_consumed * 2
                print("last reading:", last_reading)
                print("Current reading:", current_reading)
                print("Total bill:", bill)
            elif (unit_consumed >100 and unit_consumed <250):
                bill = unit_consumed * 4
                print("last reading:", last_reading)
                print("Current reading:", current_reading)
                print("Total bill:", bill)
            elif (unit_consumed >250):
                bill = unit_consumed * 6
                print("last reading:", last_reading)
                print("Current reading:", current_reading)
                print("Total bill:", bill)
else:    print("current reading is less than last reading")


#write a program to allow online exam access only if student is registered, fee is paid, system time is within exam window condition: if student is not registered then access is denied if student is registered and fee is not paid then access is denied. if fee is paid and system time is valid then exam is started otherwise exam is not started.

registered = input("Is student registered? (yes/no): ")

if registered == "no":
    print("Access is denied! Student is not registered.")

elif registered == "yes":
    fees_paid = input("Is student paid fee? (yes/no): ")

    if fees_paid == "no":
        print("Access is denied! Fee is not paid.")

    elif fees_paid == "yes":
        current_time = int(input("Enter current time: "))

        if current_time >= 9 and current_time <= 15:
            print("Exam is started")

        elif current_time < 9 or current_time > 15:
            print("Exam is not started")
