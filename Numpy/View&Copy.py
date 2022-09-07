
# View(): make copy of existing array but share different memory location

from numpy import *
a=array([100,200,300,400,500])
b=a.view()
print(a,id(a))
print(b,id(b))
a[0]=10
b[1]=20
print(a,id(a))
print(b,id(b))

# Copy():make copy of existing array but share different memory location but changges not affected
print("copy():copy")
from numpy import *
a=array([100,200,300,400,500])
b=a.copy()
print(a,id(a))
print(b,id(b))
a[0]=10
b[1]=20
print(a,id(a))
print(b,id(b))