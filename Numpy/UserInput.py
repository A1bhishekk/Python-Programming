from numpy import *
n=int(input("Enter the number of elements :"))
a=zeros(n,dtype=int)

# using for loop
for i in range(n):
    x=int(input("Enter the elements :"))
    a[i]=x

for el in a:
    print(el)

# using while loop
print("using while loop")
n=int(input("Enter the number of elements :"))
b=zeros(n,dtype=int)
j=0
while(j<n):
    x=int(input("Enter the elements :"))
    b[j]=x
    j+=1

print(b)