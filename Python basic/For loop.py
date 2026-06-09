#write a program to take input from user and print n natural in descending order using for loop

num = int(input("Enter a number: "))
for i in range (num,0,-1):
    print(i)


#write a program to print fibonacci series

num = int(input ("Enter a number: "))
a= 0
b= 1
for i in range(num):
    print(a)
    a,b = b,a+b


#write a prgram to check given number is prime or not

num = int(input("Enter a number:"))
n = 1 
for i in range(2,num):
    if(num%i == 0):
        n = 0
        break
if(n==1):
    print("Number is prime")
else:
    print("Number is not prime")


#write a program to print name

s = input("Enter a name:")
for i in s:
    print(i)


#write a program of factorial calculator with input validation

choice = input("Enter yes: ")
while choice == 'yes':
    num = int(input("enter a number: "))
    a = 1
    if(num<0):
            print("Enter a positive number")
    else:
            for i in range(1,num+1):
                a *= i
            print("Factorial of number is",a)

    choice = input("Do you want to enter more numbers? (yes/no):")
    if choice == "no":  
        print("End")
        break   
