#write a program to print '' 

print("''")


#write a program to calculate addition, multiplication, subtraction of complex numbers 

num1 = int(input("Enter the real part: "))
num2 = int(input("Enter the imaginary part: "))
addition = (num1 + num2)
multiplication = (num1 * num2)
subtraction = (num1 - num2)
print("Addition: ", addition)
print("Multiplication: ", multiplication)   
print("Subtraction: ", subtraction)


#write a program to check 2 object refers to the same memoery location or not

a = 5
b = 3
print(" ",id(a) == id(b))
 

#write a program to print emojis using unicode

print("")  #happy face


#write a program to take student name from user and a single character. check given character is present in student name or not
student_name = input("Enter the student name: ")
character = input("Enter a single character: ") 
print(character in student_name)


#write a program to output the sqaure using multiplication operator of number from 1 to 5

print("1 - ", 1*1)
print("2 - ", 2*2)
print("3 - ", 3*3)
print("4 - ", 4*4)
print("5 - ", 5*5)


