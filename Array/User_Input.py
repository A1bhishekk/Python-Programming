# input from usser using for loop 
from array import *
stu_roll=array('i',[])
n=int(input("Enter the number of Elements :"))

for i in range(n):
    stu_roll.append(int(input("Enter the elements : ")))

for el in stu_roll:
    print(el)


# input from usser using while loop 

from array import *
stu_roll=array('i',[])
n=int(input("Enter the number of Elements :"))
i=0
while(i<n):
    stu_roll.append(int(input("Enter the elements : ")))
    i+=1

for el in stu_roll:
    print(el)