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
        self.students = {}
    def addStudent(self):
        print("\n1. Engineering Student")
        print("2. Medical Student")
        choice = int(input("Enter Choice : "))
        rollNo = int(input("Enter Roll No : "))
        if rollNo in self.students:
            print("Student Already Exists")
            return
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        if choice == 1:
            branch = input("Enter Branch : ")
            cgpa = float(input("Enter CGPA : "))
            obj = EngineeringStudent(rollNo, name, age, branch, cgpa)
        elif choice == 2:
            specialization = input("Enter Specialization : ")
            hospital = input("Enter Hospital : ")
            obj = MedicalStudent(rollNo, name, age, specialization, hospital)
        else:
            print("Invalid Choice")
            return
        self.students[rollNo] = obj
        print("Student Added Successfully")
    def view_students(self):
        if len(self.students) == 0:
            print("No Student Found")
            return
        for student in self.students.values():
            print(student)
    def search_student(self):
        rollNo = int(input("Enter Roll No : "))
        if rollNo in self.students:
            print(self.students[rollNo])
        else:
            print("Student Not Found")
    def update_student(self):
        rollNo = int(input("Enter Roll No : "))
        if rollNo not in self.students:
            print("Student Not Found")
            return
        student = self.students[rollNo]
        student.set_name(input("Enter New Name : "))
        student.set_age(int(input("Enter New Age : ")))
        if isinstance(student, EngineeringStudent):
            student.set_branch(input("Enter New Branch : "))
            student.set_cgpa(float(input("Enter New CGPA : ")))
        elif isinstance(student, MedicalStudent):
            student.set_specialization(input("Enter New Specialization : "))
            student.set_hospital(input("Enter New Hospital : "))
        print("Student Updated Successfully")
    def delete_student(self):
        rollNo = int(input("Enter Roll No : "))
        if rollNo in self.students:
            del self.students[rollNo]
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")


class Login:

    def login(self):

        user_id = input("Enter ID : ")
        password = input("Enter Password : ")

        if user_id == "admin" and password == "1234":

            obj = StudentManagement()

            while True:

                print("\n===== STUDENT MANAGEMENT =====")
                print("1. Add Student")
                print("2. View All Students")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6. Exit")

                choice = int(input("Enter Choice : "))

                if choice == 1:
                    obj.addStudent()

                elif choice == 2:
                    obj.view_students()

                elif choice == 3:
                    obj.search_student()

                elif choice == 4:
                    obj.update_student()

                elif choice == 5:
                    obj.delete_student()

                elif choice == 6:
                    print("Thank You... Visit Again!")
                    break

                else:
                    print("Invalid Choice")

        else:
            print("Invalid ID or Password")
obj = Login()
obj.login()