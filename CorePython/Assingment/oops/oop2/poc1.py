class A:
    def display(self):
        print(" I am from A ")
class A1(A):
    pass
    # def display(self):
    #     print("I am from A1")
class A2(A):
    def display(self):
        print("I am from A2")
class B(A1):
    pass
    # def display(self):
    #     print("I am from B ")
class C(A2):
    pass
    # def display(self):
    #     print("I  am from c")
class D(B,C ):
    pass
    # def display(self):
    #     print("I am from D")
d=D()
d.display()