class BankAccount:
    def __init__(self,name,acNo,bal):
        self.cName=name
        self.acNo=acNo
        self.bal=bal
    def getcName(self):
        return self.cName
    def setcName(self,nm):
        self.cName=nm      
        
    def getacNo(self):
        return self.acNo
    def setacNo(self,nm):
        self.acNo=nm   
           
    def getBal(self):
        return self.bal
    def setBal(self,nm):
        self.bal=nm      
        
    def calAmount(self):
        print(f"Account balance= {self.bal}")
    
    def __str__(self):
        return f"Name= {self.cName}\tAccount No={self.acNo}\tBank Balance={self.bal}"  
# Bank aacount ends here..........................................................  

class CurrentAcc(BankAccount):
    def __init__(self, name, acNo, bal,ovrdrftLmt):
        super().__init__(name, acNo, bal)
        self.overdraftLmt=ovrdrftLmt
    def getOverDraftLmt(self):
        return self.overdraftLmt
    def setOverdraftLmt(self,lmt):
        self.overdraftLmt=lmt
    def calAmount(self):
        finalamount=self.bal+self.overdraftLmt
        print(f"Account balance= {finalamount}")
    def __str__(self):
        return super().__str__() +"\tOverdraft Limit= "+ str(self.overdraftLmt)

# Cuurent account ends here..................
class SavingAcc(BankAccount):
    def __init__(self, name, acNo, bal,iRate):
        super().__init__(name, acNo, bal)
        self.iRate=iRate
        
    def getIrate(self):
        return self.iRate
    def setIrate(self,rate):  
        self.iRate=rate
    def calAmount(self):
        si=self.bal*(self.iRate/100)
        finalamount=self.bal+si
        print(f"Account balance= {finalamount}")
    def __str__(self):
        return super().__str__() +"\t Rate of intrest= "+str(self.iRate)


a1=CurrentAcc("Vishal",1232222,15624,100)
a2=SavingAcc("Nayan",1456987,2523,6)
print("current = ",a1)
print(f"Saving= {a2}")
a2.calAmount()