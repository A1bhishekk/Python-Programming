# A Python Array is a collection of common type of data structures having elements with same data type.
# creating array 1
# import array
# stu_roll=array.array('i',[101,102,103,104,105])

from array import *
stu_roll=array('i',[101,102,103,104,105])
# stu_roll=array('f',[101.2,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Accesing array using for loop
for student in stu_roll:
    print(student)

# using range function
n=len(stu_roll)
for i in range(n):
    # print(stu_roll[i])
    print(f"element at index {i} : {stu_roll[i]}")

# Accesing array using while loop
print("while loop")
n=len(stu_roll)
i=0
while(i<n):
    print(f"element at index {i} : {stu_roll[i]}")
    i+=1

    

