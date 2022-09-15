# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

add_sub=lambda x,y=2 : (x+y, x-y)
a,s=add_sub(5,4)
print(a)
print(s)


# nested lambda functions
add =lambda x:(lambda y:x+y)
a=add(10)(20)
print(a)

# passing lambda function to another function
def show(a):
    print(a(8))

show(lambda x:x)

# returning lambda function
def mul(x):
    return (lambda y:x*y)

ans=mul(20)(30)
print(ans)