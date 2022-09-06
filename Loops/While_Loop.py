# Python has two primitive loop commands:
# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 0
while i <= 100:
    print(i)
    i += 1

print("Rest of the Code")

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

a = 1
while (a <= 10):
    print(a)
    a += 1
else:
    print("while condition no longer true")
print("Rest of the Code")

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

a = 0
while True:
    a += 1
    print(a)
    if (a == 5):
        break
print("Rest of the Code")

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
b = 0
while b <= 10:
    b += 1

    if (b == 5):
        continue
    print(b)
print("Rest of the Code")


# Nested While Loop
i = 1
while i <= 5:
    print(f"outer loop: {i} ")
    i += 1
    j = 1
    while j <= 5:
        print(f"inner loop: {j} ")
        j += 1
print("Nested While Loop")


# infinite loop
c=10
while c>5:
    print("Infinite Loop")
