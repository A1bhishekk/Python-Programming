# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
a="good morning"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
poem=   '''
        Twinkle, twinkle, little star
        How I wonder what you are
        Up above the world so high
        Like a diamond in the sky
        '''

print(poem)

name="ABHISHEKKUMAR"
print(f"length of my name is :{len(name)}")
for i in name:
    print(i)

for i in range(len(name)):
    print(f"element at index {i} :{name[i]}")


# Repetition Operators
str1="Abhishek Kumar "
print(str1*5)
print(str1[:8]*5)