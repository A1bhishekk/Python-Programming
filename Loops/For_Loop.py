# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

name = "ABHISHEK"
for ch in name:
    print(ch)
n = len(name)

# with range
for i in range(n):
    print(f"{i}:{name[i]}")


for i in range(1, 10, 2):
    print(i)

# break statement
for i in range(8):
    print(i)
    if (i == 5):
        break

# continue statement
for i in range(8):
    if (i == 5):
        continue
    print(i)

# nested forloop with else
for i in range(2):
    print("outer for loop", i)
    for j in range(4):
        print("inner for loop", j)
else:
    print("else part executed")