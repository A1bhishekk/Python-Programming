# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:



# Creating a List:
my_list=[25,"Abhishek",3.6,-5]
print(my_list)
my_list[0]=30
print(my_list[-1])


# list item accesing using for loop
# without index

print("Using For Loop")
for i in my_list:
    print(i)

# with index 
n=len(my_list)
print(n)
for i in range(n):
    print(f"Element at index {i} : {my_list[i]}")

# list item accesing using for loop
print("Using While Loop")
l=len(my_list)
i=0
while i<l:
    print(f"Element at index {i} : {my_list[i]}")
    i+=1
