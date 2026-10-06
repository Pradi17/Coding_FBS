# print(" I am from fIrstbit solution")
# print("I have completed my BCA ")
# print("i am from Buldhana. ")
# print("I Like RCB...")
# def add():
#     a=10
#     d=11
#     c=a+d
#     print(f"Addition is ={c}")
# add()
# Types of function ->1] Inbuild function , 2]User Define Function
# 1]Inbuild Function ?-> The function which is alredy define in python 
# 2].User define Function->the function which is written by the programer for their Special Task

# 1.Simple function ,2Recursive function, lambda function

#According to the number of parmater and wht value its Return
# 1.without passing parameter without returning value
# 2. with parameter without returning value
# 3. without PArameter with return value
# 4. with parameter with returning valus

# def functionName(Paramater if any ):
            # function ki body

# def greet():
#     print("wellCome Sir i am from XYZ Mall, and my Nam is ABC  please Keep your Bag in the cuboard ")
# no=int(input("enter the Number of visiter = "))
# # age=int(input("Enter the age of one Person "))
# for i in range(no):
#     a=input("Enter ")
#     greet()
 
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(6)
