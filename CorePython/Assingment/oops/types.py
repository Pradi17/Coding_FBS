# 1.Single Level inheretence
# 1 based Class and -> derived class
# class Emp:
#     def __init__(self,id,name,sal):
#         self.id=id
#         self.name=name
#         self.sal=sal
#     def disply(self):
#         print(f"id= {self.id} name= {self.name}  sal= {self.sal}")
# class devloper(Emp):
#     def __init__(self, id, name, sal,com):
#         super().__init__(id, name, sal)
#         self.incentive=com
#     def disply(self):
#         print(f"Incetive= {self.incentive}")
#         return super().disply()    
# d1=devloper(12,"Jayash",120000,12122)
# d1.disply()

# class ScalceManager(Emp):
#     def __init__(self, id, name, sal,com):
#         super().__init__(id, name, sal)
#         self.com=com
#     def disply(self):
#         print(f"Comission= {self.com}")
#         return super().disply()    

# class AreaSm(ScalceManager):
#     def __init__(self, id, name, sal, com,area):
#         super().__init__(id, name, sal, com)    
#         self.area=area
#     def disply(self):
#         print(f"Area Name= {self.area}")
#         super().disply()    
# am=AreaSm(1,"Rahul",123456,23,"Bangluru")
# sm=ScalceManager(7,"MSD",1232,70)
# am.disply()
# sm.disply()    


class Mec:
    def __init__(self):
        print("I am from  mecanical ")
class Electrical:
    def __init__(self):
        print("I am from  Electrical ")
class Mectronix(Mec,Electrical):
    def __init__(self):
        super().__init__()
        print("I am from Mactronix")
 
Mec=Mectronix()     
        