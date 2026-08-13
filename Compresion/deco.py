# def login():
#     print("timer Start")
#     print("Session Start")
#     print("Logs aadded ")
#     print("Log in  properly... ")
#     print("Session stop ")
#     print("tIMER Stop ")
# login()
# def logout():
#     print("timer Start")
#     print("Session Start")
#     print("Logs aadded ")
#     print("Logout in  properly... ")
#     print("Session stop ")
#     print("tIMER Stop ")
# logout()
# def demo():
#     print("I am in demo")
# x=demo
# # print(type(x))
# # demo()
# x()
# def outerfun():
#     name="FBS"
#     print("Outer")
#     def innerfun():
#             print(name)
#     return innerfun
# # a=outerfun()
# # print("++++++++++++++++++++")
# # a()
# outerfun()
def decoretor1(fun):
    print("I am in decoretor")
    def  wrapper():
        print("Before Function call")
        # fun()
        add()
        print("After function call ")
    return wrapper
# def fun():
#     print("I am from function")
# x=decoretor(fun)
# x()
@decoretor1
def fun():
    print("I am from function")
@decoretor1
def add():
    a=10
    b=20
    print(f"Addition= {a+b}")
fun()
add()


