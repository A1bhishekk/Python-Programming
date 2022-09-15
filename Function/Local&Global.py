#Local Variables:
x=20   #global variable
def local():
    x=10
    print("local",x)

local()
print(x)


#Global Variables:
i=0
def globals():
    i=0
    i=i+1
    print("my functions",i)

globals()


# global keyword 
a=50
def abhi():
    global a
    a=a+10
    print("abhi",a)
abhi()
print(a)


j=0
def glob():
    global j
    while j<10:
        j+=1
        print("j",j)
glob()
print(j)
