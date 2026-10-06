class Emp:
    cName="FBS"
    @staticmethod
    def empPoly(name):
        print(f"{name} is good Employee.........")
        
        
    def __init__(self,id1,name1,sal1):
        self.id=id1
        self.name=name1
        self.sal=sal1
    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setSal(self,id):
        self.sal=id
    def getSal(self):
        return self.sal
    def display(self):
        print(f"id= {self.id}\tname={self.name}\t sal={self.sal} Compony name={self.cName}")
e1=Emp(10,"sachin",789)
e1.display()
e2=Emp(12,"Vishal",15000)
e2.display()
e2.setName("Gaurav")
print(e2.getName())
print(f"Emp company name= {e1.cName}")
print(f"Emp company name= {Emp.cName}")

Emp.empPoly(e1.getName())
Emp.empPoly(e1.getName())
