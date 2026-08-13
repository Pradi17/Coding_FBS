from userdefineExp import FbsException
try :
    age=int(input("Enter the AGE "))
    if age<18:
        raise FbsException("Not Eligibal ")
except ValueError as e:
    print(e)        
except Exception as e:
    print(e)         
print("Ayse hi teri age check kar  Rahe the... ")