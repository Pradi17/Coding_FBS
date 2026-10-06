class  Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def calsal(self):
        print(f"This is Employee Sal= {self.sal}") 
class Hr(Emp):
     def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
     def calsal(self):
        print(f"This is HR Sal= {self.sal+self.com}") 
class Devloper(Emp):
     def __init__(self,id,name,sal,ince):
        super().__init__(id,name,sal)
        self.incentive=ince
     def calsal(self):
        print(f"This is Devloper  Sal= {self.sal+self.incentive}") 
        
d1=Devloper(1,"Rahul",4444444,1234)   
d1.calsal()
     
dh=Hr(1,"Pratiksha",4444,1234)   
dh.calsal()     
        