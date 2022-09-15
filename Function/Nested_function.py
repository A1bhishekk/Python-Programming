def outer():
    def inner():
        print( "I am Inner Function")
    print( "outer function")
    inner()
outer()


def day(greet):
    def night():
        return "i am night "
    result=night() + greet+" day "
    return result

print(day("good"))


# pass a function as parameter

def disp(sh):
    print("Disp Function " + sh())

def show():
    return " Show Function"

disp(show)


# function return another function 
def good():
    def bad(st):
        return "Bad Function"+st
    print("Good Function")
    return bad 

result=good()
print(result(" not"))