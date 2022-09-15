# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:

# Example
from ast import arguments
from inspect import Parameter


def my_function():
  print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()


# function with Parameter & arguments
def sum(x,y):
    sum=x+y
    return sum

print(sum(20,30));