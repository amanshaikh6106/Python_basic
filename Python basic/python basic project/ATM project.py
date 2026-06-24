balance = 500.0

while True:
    print("===Welcome to ATM===")
    print("===ATM menu===")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        print(f"your current balance:{balance:.6f}")

    elif choice == 2:
        amount = float(input("enter amount to deposite:"))
        if amount > 0:
            balance += amount
            print("successfully deposited")
            print(f"new balance:{balance:.6f}")
        else:
            print("invalid deposite amount:")

    elif choice == 3:
        amount = float(input("enter amount to withdraw:"))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("withdraw successfully")
            print(f"new balance:{balance:.6f}")
        else:
            print("insufficient balance!")
            print("invalid withdrawal amount")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("invalid choice,please try again")