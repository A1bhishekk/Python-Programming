a=20
b=20
c=30

# Q1
if(a>b):
    print("a is greater than b")
elif(a>=b):
    print("a is greater than b or equal to b")
else:
    print("a is smaller than b")


# Q2
if(a>b):
    print("a is greater than b")
elif(a>=c):
    print("a is greater than c or equal to c")
else:
    print("a is smaller than c")

# Q3
age=int(input("Enter your age :"))
if(age>=18):
    print(f"you can drive a 🚗car because your age is {age}")
elif(age>10 and age<18 ):
    print("you can try a 🚲bycycle..")
else:
    print("you can go with Amul cool🍼")
