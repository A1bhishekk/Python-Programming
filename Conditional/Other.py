# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

a=50
b=20
if a > b: print("a is greater than b")

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

print("A") if a > b else print("B")


# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:

print("A") if a < b else print("=") if a == b else print("B")


# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if(a>b):
    pass

print("goodbye!")