#write a program to create a new turple which contain element which are multiple of 7 given tuple

t1 = (7,14,21,25,28,30,35,42,49,51,56,70)
t2 = (i for i in t1 if i %7 == 0 )
print(list(t2))


#WAP to print second highest number

t = (10,100,30,500)
print("second max:", sorted(t)[-2])


