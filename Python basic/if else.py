#write a program to check enter number is multiple of 5 or not

num = input("Enter a number:")
if (int(num) % 5 == 0):
    print("It is a multiple of 5")
else:
    print("It is not a multiple of 5")


#write a program to check number is positive or not

num = input("Enter a number:")
if (int(num) >= 0):
    print("It is a positive number")
else:
    print("It is not a positive number")


#write a program to check sale price and cost price of user and check user get profit or loss

cost_price = input("Enter the cost price:")
sale_price = input("Enter the sale price:") 
if (int(sale_price) > int(cost_price)):
    print("User got profit.")
else:
    print("User got loss.")


#write a program to check given shape us rectangle or square

length = input("Enter the length of the shape:")
breadth = input("Enter the breadth of the shape:")
if (int(length) == int(breadth)):
    print("The shape is a square.")
else:
    print("The shape is a rectangle.")


#write a program to check given number is multiple of 3 and 5 

num = input("Enter a number:")
if (int(num) % 3 == 0 and int(num) % 5 == 0):
    print("The number is a multiple of 3 and 5.")
else:   print("The number is not a multiple of 3 and 5.")


#Example of if statement
a=10
if a==10:
    print(a)
if(a>=10):
    print(-a)
if(a!=9):
    print(a*a)
else:
    print(a**3)
print("end")


#2 Example of if statement
n=20
if n%3!=0:
    print(n)
print("end")
if n&3:
    print(n*n)
print("end1")


#3 Example of if statement
print(2**3 + (5+6) ** (1+1))

