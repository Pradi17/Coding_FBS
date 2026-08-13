# num1=int(input("enter the number 1 "))
# num2=int(input("enter the number 2 "))
# if num2!=0:
#     print(num1/num2)
# else:
#     print("bhai zero se divide nahi kar sakta... ")
# print("I am done... .")
# print(num1)
# li=[12,22,33,44,55]
# print(li[10])



# num1=int(input("enter the number 1 "))
# num2=int(input("enter the number 2 "))
# try:
#     print(num1//num2)
#     no=int(input("Enter the Number "))
#     print(f"Your No ={no}")
#     li=[12,10]
#     print(li[1])
# except ZeroDivisionError as z:
#     print(z)
#     print("Denomenetor mai zero nahi ho skata ")
# except ValueError as v:
#     print(v)
#     print("Plese Enter number in it ")
# except IndexError as i:
#     print(i)
#     print("I am in index errr  ")
# except Exception as e :
#     print(e)
#     print("Generlize")
# else:
#     print("all good.........................  ")
# finally:
#     print("I am in finaly block ")


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("You are not eligible")

    print("Eligible")

except ValueError as e:
    print(e)