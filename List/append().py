# APPEND()
my_list=[25,"Abhishek",3.6,-5]
for i in my_list:
    print(i)

# Appending an element to the list
my_list.append("Monika")

n=len(my_list)
print(n)
for i in range(n):
    print(f"Element at index {i} : {my_list[i]}")
