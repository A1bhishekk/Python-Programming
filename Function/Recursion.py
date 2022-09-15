# RECURSION FUNCTION 
import sys
sys.setrecursionlimit(5000)   #set the recursion limit
print(sys.getrecursionlimit())


i=0
def greet():
    global i
    i+=1
    print("Good Morning",i)
    while i<20:
        greet()

greet()