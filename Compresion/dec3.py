def decoretr(fun):
    def inner(*args):
        print("Before calling functanality is added ")
        fun(*args)
        print("After calling functanality is added ")
    return inner

@decoretr
def add(a,b):
    print(f"Addition = {a+b}")
@decoretr
def add3(a,b,c):
    print(f"Addition3 = {a+b+c}")

@decoretr
def sub(a,b):
    print(f"substraction= {a-b}")
@decoretr
def logIn():
    print("I am  in log in")
x=int(input("Enter the number 1 "))
y=int(input("Enter the number 2 "))
add(x,y)
print("++++++++++++++++++++++++++++++++++++++++++")
sub(x,y)
print("++++++++++++++++++++++++++++++++++++++++++")
add3(12,2,3)
print("++++++++++++++++++++++++++++++++++++++++++")
logIn()
    