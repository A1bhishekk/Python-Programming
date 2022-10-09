a={}
n=int(input("No of elements : "))

for i in range(n):
    k=input("Enter key :")
    v=input("Enter value :")
    a.update({k:v})

print(a)