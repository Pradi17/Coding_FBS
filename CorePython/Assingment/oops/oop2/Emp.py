from abc import ABC,abstractmethod
class Emp(ABC):
    def __init__(self,id,name,sal):
        self._id=id
        self.__name=name
        self.sal=sal
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
    def __str__(self):
        return f"id= {self._id}\tname={self.__name}\t sal={self.sal}"
    @abstractmethod
    def claSal():
        pass
    
 # class Emp end here...........
class Hr(Emp):
    def __init__(self, id, name, sal,com=120):
        super().__init__(id, name, sal)
        self.com=com
    def setCom(self,com):
        self.com=com
    def getCom(self):
        return self.com
    def __str__(self):
        return super().__str__()+"\tCommition= "+str(self.com)
    def claSal(self):
        print(f"Total Sal={self.sal+self.com}")
h=Hr(7,"Rich",12121,121)
# e1=Emp(17,"ABD",12346)
h.claSal()
# h.display()
# e1.display()
# print(e1)





