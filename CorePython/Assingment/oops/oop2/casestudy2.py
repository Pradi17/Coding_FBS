class Student:
    def __init__(self, roll, name, age):
        self.__roll = roll
        self.__name = name
        self.__age = age
    def get_roll(self):
        return self.__roll
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_roll(self, roll):
        self.__roll = roll
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def __str__(self):  
        return f"Roll No = {self.__roll}\tName = {self.__name}\tAge = {self.__age}"
    # ===============================================================================================
class EngineeringStudent(Student):
    def __init__(self, roll, name, age, branch, cgpa):
        super().__init__(roll, name, age)
        self.__branch = branch
        self.__cgpa = cgpa
    def get_branch(self):
        return self.__branch
    def get_cgpa(self):
        return self.__cgpa
    def set_branch(self, branch):
        self.__branch = branch
    def set_cgpa(self, cgpa):
        self.__cgpa = cgpa
    def __str__(self):
        return super().__str__() + f"\tBranch = {self.__branch}\tCGPA = {self.__cgpa}"
    # ===============================================================================================

class MedicalStudent(Student):
    def __init__(self, roll, name, age, specialization, hospital):
        super().__init__(roll, name, age)
        self.__specialization = specialization
        self.__hospital = hospital
    def get_specialization(self):
        return self.__specialization
    def get_hospital(self):
        return self.__hospital
    def set_specialization(self, specialization):
        self.__specialization = specialization
    def set_hospital(self, hospital):
        self.__hospital = hospital
    def __str__(self):
        return super().__str__() + f"\tSpecialization = {self.__specialization}\tHospital = {self.__hospital}"
# =========================================================================================================

class StudentManagement:
    def __init__(self):
        self.students={}
    def addStudent(self):
        print("1.Add Engineering Student")
        print("2.Add Medical Student")
        ch=int(input("Enter the Choice= "))
        rollNo=int(input("Enter the RollN0 "))
        if rollNo in self.students:
            print("Student is Allready Present with this Roll No")
            return
        name=input("Enter Student Name=")
        age=int(input("Enter Student age="))
        if ch==1:
            branch=input("Branch Name= ")
            cgpa=input("Enter the CGPA ")
            obj=EngineeringStudent(rollNo,name,age,branch,cgpa)
        elif ch==2:
            spe=input("Enter Specilization = ")
            hop=input("Enter the Hospital ")
            obj=MedicalStudent(rollNo,name,age,spe,hop)
        else:
            print("Invalid choice ")
            return
        self.students[rollNo] =obj
        print(f"{self.students[rollNo]} added sussefully...")
            
        
    
    
    
    
class Login:
    def logIn():
       obj=StudentManagement()
       uId=input("Enter the User Id= ")
       passs=input("Enter the Password= ")
       if uId=="admin" and passs=="1234":
            while True:
                print("==WellCome To Student Management System===")
                print("1.Add Student")
                print("2.Disply All Students ")
                print("3.Serch Student ")
                print("4.Update Students ")
                print("5.Delete Student ")
                print("6.Exit.......")
                choice=int(input("Enter the choice= "))
                if choice==1:
                    obj.addStudent()
                elif choice==2:
                    print("display")
                elif choice==3:
                    print("Serch ")
                elif choice==4:
                    print("Update ")
                elif choice==5:
                    print("Delete ")
                elif choice==6:
                    print("Exit")
                    break
                else:
                    print("invalide Choice..... enter the choice again..")
       else:
           print("Inavalid ID and Password...")   
           
Login.logIn()
        