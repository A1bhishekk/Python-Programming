# This method is used to append another array or iterable object at the end of the array.
from array import *
stu_roll=array('i',[101,101,103,104,105])
stu_roll2=array('i',[106,107,108])
stu_roll.extend(stu_roll2)
for student in stu_roll:
    print(student)