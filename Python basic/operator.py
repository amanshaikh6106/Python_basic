#write a program to 2 no. from users and convert it into integer

s1= input("Enter first number: ")
s2= input("Enter second number: ")
print ( "First number is: " , int(s1) )
print ( "Second number is: " , int(s2) )

print ( "addition:" , int(s1) + int(s2) )
print ( "subtraction:" , int(s1) - int(s2) )
print ( "multiplication:" , int(s1) * int(s2) )
print ( "division:" , int(s1) / int(s2)  )
print ( "modulus:" , int(s1) % int(s2)  )
print ( "floor division :" , int(s1) ** int(s2)  )
print ( " float division :" , int(s1) // int(s2)  )


#write a program to find square of given number
num = input("Enter a number: ")
print ( "Square of the number is: " , int(num) ** 2 )


#write a program to find area of square
side = input("Enter the number : ")
area = ("Area of the square is:", int(side) * int(side) )
print ( area )


#write a program to convert temperature from celsius to fahrenheit
celsius = input("Enter temperature in Celsius: ")
fahrenheit = (int(celsius) * 9/5) + 32
print ( "Temperature in Fahrenheit: " , fahrenheit )


#write a program to convert temperature from fahrenheit to celsius
fahrenheit = input("Enter temperature in Fahrenheit: ")
celsius = (int(fahrenheit) - 32) * 5/9
print ( "Temperature in Celsius: " , celsius )


#swap two numbers without using third variable
a = input("Enter first number: ")
b = input("Enter second number: ")
print ( "Before swapping: a =", a, "b =", b )
a, b = b, a
print ( "After swapping: a =", a, "b =", b )


#swap two numbers using third variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print ( "After swapping: a =", a, "b =", b )


#swap two numbers using bitwise operators(homework)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a ^ b
b = a ^ b           
a = a ^ b
print ( "After swapping: a =", a, "b =", b )


#write a program to take two numbers from user and shift first number by second number to left
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) << int(num2)
print ( "Result of left shift: " , result ) 
