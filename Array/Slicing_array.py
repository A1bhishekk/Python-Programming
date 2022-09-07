from array import *
stu_roll=array('i',[101,102,103,104,105])
# a=stu_roll[1:5]
# a=stu_roll[:5]
# a=stu_roll[1:]
# a=stu_roll[-3:]
# a=stu_roll[-4:-3]
a=stu_roll[0:5:2]
print(a)
for i in a:
    print(i)