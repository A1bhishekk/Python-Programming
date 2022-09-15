a=20

def myfun():
    a=50
    print("local variable a:" ,a)
    x=globals()['a']
    print("global variable a:" ,x)   #no impact on global variables
    print(a+x)
myfun()
print(a)

