from u2 import Userexception
def emp(id, name, age):
    try:
            if not (age > 0 and age < 121):
                raise Userexception(age)
    except Exception as e:
        print(e)
    print("ID:", id)
    print("NAME:", name)
    print("AGE:", age)
id = int(input("Enter ID:"))
nm = input("Enter name:")
age = int(input("Enter age:"))
emp(id, nm, age)