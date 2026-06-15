#write a program to declare list of integer. then take declare list of floating point number. create a new list from list of integer which contain positive number

l1 = [1,2,3,4,5,6,7,-8,9,-7,-3]
print("list:",l1)

l2 = [1.2,2.4,3.6,4.2,5.7,6.9,7.4,8.0,9.3]
print("floating point list:",l2)

l3 = [l for l in l1 if l>0]
print("Positive list:",l3)


#write a program to check enter number is present in list or not

l1 = [5,4,1,3,8,0,2,7]
s = int(input("enter a number:"))
print("Number is present in list:",s in l1)


#i/p = [1,2,10,3,4,5]
#o/p = [2,10,4]
#o/p = [3,5,1]

l1 = [1,2,10,3,4,5]
l2 = [i for i in l1 if i %2 == 0]
print(l2)
l3 = [i for i in l1 if i %2 != 0]
print(l3)


#write a program to take element of list from the user

n = int(input("enter number of list: "))
l1 = []
for _ in range(n):
    j = input("list:")
    l1.append(j)


#i/p = [1,10,2,4]
#o/p = [4,1,10,2]

l1 = [1,10,2,4]
print(l1)
print(l1[-1:]+l1[:-1])
print([4]+[1,10,2])