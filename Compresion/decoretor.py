# def login():
#     print("Authentication")
#     print("Logging")
#     print("Timer Start")
#     print("Login Successful")
#     print("Timer End")
# login()
# def hello():
#     print("I am good")
# v=hello
# print(type(v ))
# def outer():
#     def inner():
#         print("Hello")
#     return inner
# x=outer()
# x()
# def outer():

#     name = "FirstBit"

#     def inner():
#         print(name)
#     return inner
# x=outer()
# x()

def decorator(fun):
    def wrapper():
        print("Before")
        fun()
        print("After")
    return wrapper
def hello():
    print("Hello")
d=decorator(hello)
d()