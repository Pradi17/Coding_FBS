# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
# ch=input("Enter the chareter ")
# if ch=='a' or ch=='e' or ch=='i' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=="U":
#     print(f"{ch} is vowel ")
# else:
#     print(f"{ch} is Consonent ")

# Write a program to input angles of a triangle and check whether triangle is valid or not.
# a1=int(input("enter the angle 1 "))
# a2=int(input("enter the angle 2 "))
# a3=int(input("Enter the angle 3 "))
# if a1+a2+a3==180:# sum of angle of trianle is 180 
#     print("The triangle is valid")
# else:
#     print("The triangle is not valid")

# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)    
# import random 
# userId=input("Enter the user id= ")
# password=input("Enter the Password = ")
# if userId=="admin" and password=="virat@123":
#     captch=random.randint(1000,9999)
#     print(f"Your Captcha= {captch}")
#     chuser=int(input("Enter the Captcha=> "))
#     if chuser==captch:
#         print("User Login Successfully..  ")
#     else:
#         print("Invalid Captcha.... ")    
# else:
#     print("User is Invalid ")



# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.       

ag1=int(input("enter the age of First person= "))
tkprice1=float(input("Enter the Ticket Price of First person= "))
totalPrice=0
if ag1<12:
    totalPrice=totalPrice+(tkprice1*0.30)
elif ag1>59:
    totalPrice=totalPrice+(tkprice1*0.50)
else:
    totalPrice=totalPrice+tkprice1
# First person Ends here...........


ag2=int(input("enter the age of second person= "))
tkprice2=float(input("Enter the Ticket Price of Second person= "))
if ag2<12:
    totalPrice=totalPrice+(tkprice2*0.30)
elif ag2>59:
    totalPrice=totalPrice+(tkprice2*0.50)
else:
    totalPrice=totalPrice+tkprice2
# Second person Ends here...........
 

ag3=int(input("enter the age of third person= "))
tkprice3=float(input("Enter the Ticket Price of third person= "))
if ag3<12:
    totalPrice=totalPrice+(tkprice3*0.30)
elif ag3>59:
    totalPrice=totalPrice+(tkprice3*0.502)
else:
    totalPrice=totalPrice+tkprice3
# third person Ends here...........

ag4=int(input("enter the age of 4th person= "))
tkprice4=float(input("Enter the Ticket Price of 4th person= "))
if ag4<12:
    totalPrice=totalPrice+(tkprice4*0.30)
elif ag4>59:
    totalPrice=totalPrice+(tkprice4*0.502)
else:
    totalPrice=totalPrice+tkprice4
# third person Ends here...........

ag5=int(input("enter the age of 5th person= "))
tkprice5=float(input("Enter the Ticket Price of 5th person= "))
if ag5<12:
    totalPrice=totalPrice+(5*0.30)
elif ag5>59:
    totalPrice=totalPrice+(tkprice5*0.502)
else:
    totalPrice=totalPrice+tkprice5
# third person Ends here...........

print(f"Total price to pay for th e Trip of Five people is {totalPrice}")