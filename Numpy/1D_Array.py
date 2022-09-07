
# crating 1D Array using array()
# import numpy
# animal=numpy.array(["dog", "cat", "tiger"])

from numpy import *
animal=array(["dog", "cat", "tiger"])
print(animal)
print(animal.dtype)


# using for loop without index 
for el in animal:
    print(el)

# using for loop without index 
for i in range(len(animal)):
    print(f"animal at index {i} : {animal[i]}")


# using for loop without index 
i=0
while (i<len(animal)):
    print(f"animal at index {i} : {animal[i]}")
    i+=1
