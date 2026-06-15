#write a program to take string from user and iterate using for loop, for with range function, while loop 

s = input("enter a name: ")
for i in s:
    print(i, end="")
print()

for i in range (len(s)):
    print(s[i], end="")
print()

i=0
while i<len(s):
    print(s[i],end="")
    i +=1


#write a program to take string from user and check given string is palindrome or not

s = input("enter a name: ")
if s ==s[::-1]:
    print("Name is palindrome")
else:
    print("Name is not palindrome")


#write a program to check both string are anagram or not

s = input("enter a first name: ")
a = input("enter a second name: ")
 
s = sorted(s)
a = sorted(a)

if s == a:
    print("it is anagram")
else:
    print("it is not anagram")


#write a program to count number of alphanbet, digit, special symbol in given string and also count of upper case and lower case

s = input("enter a name: ")
A = 0
D = 0
S = 0
U = 0
L = 0

for i in s:
    if i.isalpha():
        A += 1
        if i. isupper():
            U += 1
        else:
            L += 1
    elif i.isdigit():
        D += 1
    else:
        S += 1
print("Alpha:" ,A)
print("Upper:" ,U)
print("Lower:" ,L)
print("Digit:" ,D)
print("Symbol:" ,S)


#write a program to take two string from user. if both string are equal then convert it in upper case and replace first string with second string. if they are not equal then convert it in lower case and join first string with second string

s1 = input("enter a first name:")
s2 = input("enter a second name:")

if s1 == s2:
    print("upper case is:",s1.upper())
    print("upper case is:",s2.upper())
    print("result:",s1.replace("s1","s2"))
else:
    
    print("lower case is:",s1.lower())
    print("lower case is:",s2.lower())
    print("result",s1+s2)

