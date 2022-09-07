from numpy import *
a=array([100,200,300,400,500])
b=array([100,200,3000,400,500])
c=where(a>b,a,b)
print(c);