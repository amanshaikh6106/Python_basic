#write a program to print pattern
#* 
#* * 
#* * * 
#* * * * 

for i in range (4):
    for j in range (i+1):
        print("*",end = " ")
    print()


#write a program to print pattern
#1 
#1 2 
#1 2 3 
#1 2 3 4 

for i in range (1,5):
    for j in range (1,i+1):
        print(j, end=" ")
    print()
    

#write a program to print pattern
#1 
#2 2 
#3 3 3 
#4 4 4 4 

for i in range (1,5):
    for j in range (1,i+1):
        print(i,end=" ")
    print()

#write a program to print pattern 
#* * * * 
#* * * 
#* * 
#* 

for i in range (4,0,-1):
    for j in range (i,0,-1):
        print("*", end=" ")
    print()


#write a program to print pattern
#1 1 1 1 
#2 2 2 
#3 3 
#4 

for i in range (1,5):
    for j in range (i,5,+1):
        print(i, end=" ")
    print()


#write a program to print pattern
#1 2 3 4 
#1 2 3 
#1 2 
#1 

for i in range (1,5):
    for j in range (1,6-i):
        print(j, end=" ")
    print()


#write a program to print pattern
#1
#2 3
#4 5 6
#7 8 9 10

z=1
for i in range (1,5):
    for j in range(1,i+1):
        print(z ,end=" ")
        z += 1
    print()


#write a program to print pattern
#A
#B C
#D E F
#G H I J

k = 65
for i in range (1,5):
    for j in range(1,i+1):
        print(chr(k) ,end=" ")
        k += 1
    print()


    
#write a program to print pattern
#A
#B B
#C C C 
#D D D D

k = 65
for i in range (1,5):
    for j in range(1,i+1):
        print(chr(k) ,end=" ")
    k += 1
    print()


#write a program to print pattern
#C C C
#B B
#A

k=67
for i in range (1,4):
    for j in range (1,5-i):
        print(chr(k), end=" ")
    k -= 1    
    print()



#write a program to print pattern
#    *
#  * *
#* * *

for i in range (1,4):
    for k in range (3-i):
        print(" ",end=" ")
    for j in range (i):
        print("*",end=" ")
    print()


#write a program to print pattern
#* * * *
#  * * *
#    * *
#      *

for i in range (4,0,-1):
    for o in range (4-i):
        print(" ",end=" ")
    for j in range (i):
        print("*", end=" ")
    print()



#write a program to print pattern
#      *
#    * * *
#  * * * * *
#* * * * * * *

for i in range (1,5):
    for k in range (4-i):
        print(" ",end=" ")
    for j in range (2*i-1):
        print("*",end=" ")
    print()


#write a program to print pattern
#      *
#    * * *
#  * * * * *
#* * * * * * *
#  * * * * *
#    * * *
#      *

for i in range (1,4):
    for k in range (4-i):
        print("  ",end="")
    for j in range (2*i-1):
        print("*",end=" ")
    print()

for i in range (4,0,-1):
    for k in range (4-i):
        print("  ",end="")
    for j in range (2*i-1):
        print("*",end=" ")
    print()


#write a program to print pattern
#* * * * * * *
#  * * * * *
#    * * *
#      *

for i in range (4,0,-1):
    for k in range (4-i):
        print("  ",end="")
    for j in range (2*i-1):
        print("*",end=" ")
    print()


#write a program to print pattern
#A
#b C
#d E f
#G h I j

ch = 65      
for i in range (1,5):
    for j in range(1,i+1):
        if ch %2 == 0:
            print(chr(ch).lower(), end=" ")
        else:
            print(chr(ch).upper(), end=" ")
        ch += 1
    print()



#write a program to print pattern
#*
#*
#*
#*
#* * * * * *

for i in range(1,6):
    if i < 5:
        print("*")
    else:
        print("* "*6)


#write a program to print pattern
# * * * * *
#     * 
#     *
#     *
#     *
#     *
#     *

for i in range(1,6):
    if i == 1:
        print("* "*5)
    else:
        for k in range (5-i):
            print("   ","*")