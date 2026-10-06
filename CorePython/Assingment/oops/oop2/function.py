# 1.without paramater wothout return value
# def add():
#     a=int(input("Enter the No1 "))
#     b=int(input("Enter the No2 "))
#     c=a+b
#     print(c)
# add()

# def add(a,b):
#     c=a+b
#     print(c)
    
# y=int(input("Enter the No1 "))
# x=int(input("Enter the No2 "))   
# add(y,x)

# def add():
#     a=int(input("Enter the No1 "))
#     b=int(input("Enter the No2 "))
#     return a+b
# result=add()
# print(f"Result= {result}")


# def add(a=0,b=1):
#     return a+b

# no1=int(input("Entr the number1 "))
# no2=int(input("Entr the number2 "))
# result=add()
# print(f"Result= {result}")

# keyword Argument

# def greet(name,msg):
#     print(f"{msg}  {name}")
# greet(msg="Hi",name="Sachin")

# 2.variable length argument
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(f"Addition= {sum}")
# add(12,4,12,4,22)

# 3. keword Length Argument
def greet(**agrs):
    for i,j in agrs.items():
        print(f"{i} = {j}")
greet(msg="Hi",name="Sachin",id=123,sal=2121)