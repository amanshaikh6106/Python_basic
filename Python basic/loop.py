# #write a program to print first n natural numbers in descending order 

n = int(input("Enter a number: "))
while n > 0:
      print(n ,end=" ")
      n -= 1
print("End")


# #write a program to print 2 table in following format: 2 * 1 = 2, 2 * 2 = 4, 2 * 3 = 6

n = 1
while n <= 10:
   print(f"2*{n} = {2*n}")
   n+= 1


#write a program to print even natural numbers upto 100

n=1
while n <= 100:
   if n % 2 == 0:
        print(n)
   n += 1
print("end")

        
#write a program to print addition of first n natural numbers

num = int(input("Enter a number: "))
sum = 0
i = 1
while i<=num:
    sum += i
    i += 1
print(sum)


#write a program to print addition of first n even numbers

n = int(input("Enter a number:"))
sum = 0
while n >= 1:
    if n % 2 == 0:
         sum += n
    n -= 1
print(sum)


#write a program to print A to Z

ch = 'A'
while ch <= 'Z':
   print(ch) 
   ch = chr(ord(ch)+1)


#write a program to print Aa Bb Cc....

ch = 65
while ch <= 90:
   print(chr(ch)+chr(ch+32),end=" ")
   ch += 1


#write a program to display which are divisible by 13 but not by 3 between 100 to 500

num = 100
while num <= 500:
   if num % 13 == 0 and num % 3 != 0:
       print(num)
   num += 1


#write a program to find sum of digit in given number for example: 324 = 9

num = int(input("Enter a number: "))
sum = num
total = 0

while num > 0:
    digit = num % 10     
    total += digit       
    num = num // 10       

print(f"Sum of digits of {sum} = {total}")


#write a program to enter numbers till user wants and at the end it should display sum of all the number enters

total = 0

while True:
   num = int(input("Enter a number: "))
   total += num

   choice = input("Do you want to enter more numbers? (yes/no):")
   if choice == "no":
       break
print(f"Sum of all numbers: {total}")


