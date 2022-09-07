
from numpy import *
a=array([100,200,300,400,500])
b=array([100,200,300,400,500])
c=a==b
print(all(c))   #if all true return true
print(any(c))    #if one or more are true return true
