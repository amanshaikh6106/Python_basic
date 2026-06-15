#write a program to check if all elements in tuple are same or not

t = (1,2,3,4,5,6)
s = set(t)
print(s)
if len(s) == 1:
    print("Element are same")
else:
    print("element are not same")


#write a program to remove duplicate element from given list and accept element of a list from user

n = int(input("enter number of list: "))
l1 = []
for _ in range(n):
    j = int(input("enter a list :"))
    l1.append(j)
print("Before removing duplicate: ",l1)
print("After removing duplicate: ", set(l1))


#write a program to create a dictonary for employee details

d = {'Name':'Amit','age':'30','salary':'300000'}
print(d)

d['Name'] = 'Aman'
print(d)

for (i,j) in d.items():
    print(i,j)

del d ['Name']
print(d)


d1 = dict(a = 'one', b = 'two')
print(d1) 
print(d1.keys())
print(d1.values())
print(d1.items())
print(d1.get('a')) 
print(d1['a'])
d1.popitem()
print(d1)
print(d1.pop('a'))
print(d1)
d1['a'] ="Two"
print(d1)
d1['a'] = "one"
print(d1)
d1.clear()
print(d1)


#how many times word came
#i/p = s="Python is very easy. Python is programming language"
#o/p = python:2

s = "Python is very easy Python is programming language"                    
print(s)
#d={}
words = s
for i in set(words):
    print(f"{i}=",words.count(i), end=" ")
    #d[i] = words.count(i)
#print(d)
