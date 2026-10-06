class Student:
    collage="FBS"
    totalStudent=0;
    def __init__(self,rollNo,name,age):
        Student.totalStudent+=1
        self.rollNo=rollNo
        self.name=name
        self.age=age
    @staticmethod
    def getTotalStudent():
        return Student.totalStudent
      
    def getRollNo(self):
        return self.rollNo
    
    def setRollNo(self,rono):
        self.rollNo=rono
        
    def getName(self):
        return self.name
    
    def setName(self,nm):
        self.name=nm
    
    def getAge(self):
        return self.age
    
    def setName(self,ag):
        self.name=ag
        
    def display(self):
        print(f"RollN0= {self.rollNo} \t Name= {self.name} \t Age= {self.age}")     
# Student class Ends Here

class PlStudent(Student):
    def __init__(self,rollNo,name,age,sal):
        super().__init__(rollNo,name,age)
        self.sal=sal
    def getSal(self):
        return self.sal
    def setRollNo(self,sal):
        self.sal=sal
    def display(self):
        super().display() 
        print(f"Sal ={self.sal} ") 
        
#Placed Student ends here...........

p1=PlStudent(12,"Sachin",23,30000)
p2=Student(45,"Rohit",23)
print(f"TotalStudet= {Student.totalStudent}")
print(p1.sal)