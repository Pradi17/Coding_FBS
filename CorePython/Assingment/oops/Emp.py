class Emp:
    def __init__(self,id,name, sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getName(self):
            return self.name
    def setName(self,nm):
            self.name=nm
    def getId(self):
            return self.id
    def setId(self,nm):
            self.id=nm
    def getSal(self):
            return self.sal
    def setSal(self,nm):
            self.sal=nm
    def calSal(self):
        totalSal=self.sal
        return totalSal
    def display(self):
        print(f"Id={self.id}\t Name={self.name}\t Sal={self.sal}")        
# Emp Class Ends here......................

class Hr(Emp):
    def __init__(self, id, name, sal,cm):
          super().__init__(id, name, sal)
          self.com=cm
    def getCom(self):
        return self.com
    def setCom(self,cm):
        self.com=cm
    def calSal(self):
          return super().calSal()+self.com
    def display(self):
          super().display()
          print(f"Comision= {self.com}")
#HR End Here................................................................... 
    
e1.display()
# e1.id=10#but is way se nahi karan ahi qki real life mai aise nahi hota
e1.setId(10)
e1.display()
h1=Hr(18,"Smriti",12345,1234)
h1.display()