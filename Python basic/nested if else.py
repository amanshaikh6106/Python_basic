#write a program to find discount depends on following conditions: if festival sale is on and user having member ship then 30% discount if user having non member ship then 20% discount. if festival sale is off and if user having member ship and card value is greater than equals to 5000 than 20% discount if user having member ship and card value is less than 5000 than 10% discount if user does not have member ship than no discount

festival_sale = "on"
membership = "yes"
card_value = 0

festival_sale = input("Is festival sale is on or off?: ")
membership = input("Do you have membership?: ")
card_value = int(input("Enter card value: "))

if (festival_sale == "on"):
    if (membership == "yes"):
        print("You get 30% discount")
    else:
        print("You get 20% discount")

else:
    if (membership == "yes" and card_value >= 5000):
        print("You get 20% discount")
    elif (membership == "yes" and card_value < 5000):
        print("You get 10% discount")
    else:
        print("You get no discount")


#write a program to allow online exam access only if student is registered,fee is paid, system time is within exam window conditions:
#  if student is not registered then access is denied
#  if student is registered and fee is not paid then access is denied.
#  if fee is paid and system time is valid then exam is started otherwise exam is not started.

registered = input("Is student registered? (yes/no): ")
if registered == "yes":
    fee_paid = input("Is fee paid? (yes/no): ")
    if fee_paid == "yes":
        current_hour = int(input("enter current time: "))
        if current_hour >= 9 and current_hour <= 15:
            print("Exam is started ")
        else:
            print("Exam is not started")
    else:
        print("Access Denied! Fee is not paid.")
else:
    print("Access Denied! Student is not registered.")
