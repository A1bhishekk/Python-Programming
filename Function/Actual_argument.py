from ast import arguments, keyword


# positional arguments

def power(x,y):
    z=x**y
    print(z)

power(5,5)

# keyword arguments.

def fullname(name,age):
    print(name,age)

fullname(age=23,name="Abhishek")

# default arguments.

def fname(name="Abhishek",age="20"):
    print(name,age)
fname("monika")

# variable length arguments.
def  add(x,*num):
    z=x+num[0]+num[1]
    print(z)
add(2,3,5,7)

#keyword variable length arguments.
def mul(**x):
    b=x['a']*x['b']*x['c']*x['d']
    print(b)

mul(a=2,b=3,c=4,d=5)