def chekArmstrong(no,power):
    if no==0:
        return 0
    digit=no%10
    return (digit**power) +chekArmstrong(no//10 ,power)
no =int(input("Enter the number = "))
power=len(str(no))
result =chekArmstrong(no,power)
if result==no:
    print(f"{no} is Armstrong ")
else:
    print(f"{no} is not Armstrong. ")
